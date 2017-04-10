import time
import crawler_config
import sys
import os
import time
import platform


def win_daemon():
    while True:
        for entry in os.scandir(crawler_config.data_in_dir):
            if entry.is_file() and entry.name.endswith('.json'):
                print(entry.name)
        time.sleep(60)

if __name__ == '__main__':
    if platform.system() == 'Windows':
        win_daemon()
