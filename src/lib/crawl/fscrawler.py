#
# Apache License 2.0
#

import os
import glob
from multiprocessing import Pool
from collections import deque

# Global variable
SKIP_PATTERN = []
Stat = namedtuple('stat', ['mode', 'path', 'uid', 'gid', 'size', 'atime', 'mtime', 'ctime'])


class Crawler(object):
    """docstring for Crawler"""

    def __init__(self, *args, **kwargs):
        super(Crawler, self).__init__()

    def _scandir(self, path):
        with os.scandir(path) as root:
            for entry in root:

                if entry.is_file():
                	entry.stat()
                    File()
                if entry.is_dir():
                    Directory()
