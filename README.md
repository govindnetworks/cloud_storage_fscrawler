# cloud_storage_crawler
1. cloud_storage_crawler will have GUI interface
2. cloud_storage_crawler periodically crawl meta data and store in the database
3. It will help storage admin/User to maintain file for archive or compress and backup

#Pattern design
    1.Producer and consumer design pattern used for cloud_storage_fscrawler
        a. Producer put file name in the queue
        b. Consumer get file name run os.stat and store stats in json
        c. Json dumped in data/In folder
        d. Json file will be processed by db_populate daemon and inserted into Rethinkdb database
        e. Once processed Json file will be moved into data/Out folder
        f. If any error comes json file will be moved into data/Fail folder
        g. Later check the error message and moved backed into data/In folder

two different type of child either it is directory or file
directory will have child of directory or file
file do not have child

                     ---------
                    |directory|
                  /  ---------
                 /        |
             ------     ---------
    .  ..   |file  |   | directory|
             ------     ----------


fs_crawler --path <crawl>

usage: fscrawler.py [-h] --path PATH

cloud storage crawler

optional arguments:
  -h, --help   show this help message and exit
  --path PATH


