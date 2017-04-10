import os
import asyncio
import argparse
import json
from datetime import datetime

cur_dir = os.path.dirname(os.path.realpath(__file__))
stats = dict()


async def produce(queue, path):
    for root, dirs, files in os.walk(path, topdown=True):
        for file in files:
            item = os.path.join(root, file)
            # put the item in the queue
            await queue.put(item)


async def consume(queue):
    while True:
        # wait for an item from the producer
        item = await queue.get()
        st = os.stat(item)
        stats.update({st.st_ino: {'name': item, 'mode': st.st_mode, 'uid': st.st_uid,
                                  'gid': st.st_gid, 'size': st.st_size, 'atime': st.st_atime,
                                  'mtime': st.st_mtime, 'ctime': st.st_ctime}})
        # Notify the queue that the item has been processed
        queue.task_done()

async def run(path):
    queue = asyncio.Queue()
    # schedule the consumer
    consumer = asyncio.ensure_future(consume(queue))
    # run the producer and wait for completion
    #db_consume = asyncio.ensure_future(insert_db(queue))
    await produce(queue, path)
    # wait until the consumer has processed all items
    await queue.join()
    # the consumer is still awaiting for an item, cancel it
    consumer.cancel()


def write_json_file():
    now = datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
    filename = "crawled_data_{0}.json".format(now)
    json_file = os.path.join(cur_dir, '../../data/In', filename)
    with open(json_file, 'w') as fp:
        json.dump(stats, fp)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='cloud storage crawler')
    parser.add_argument('--path', required=True)
    args = parser.parse_args()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(args.path))
    loop.close()
    write_json_file()
    # for st in stats:
    #    print(st)
