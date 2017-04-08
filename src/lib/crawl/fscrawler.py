#
# Apache License 2.0
#

import os
from multiprocessing import Pool
from collections import namedtuple
from base.composite import File, Directory

# Global variable
SKIP_PATTERN = []
Stat = namedtuple('stat', ['name', 'mode', 'path', 'uid', 'gid', 'size', 'atime', 'mtime', 'ctime'])


class Crawler(object):
    """docstring for Crawler"""

    def __init__(self, *args, **kwargs):
        super(Crawler, self).__init__()

    def _scandir(self, *, path):
        with os.scandir(path) as root:
            for entry in root:
                if entry.is_file():
                    print("Name is {0} ".format(entry.name))
                    st = entry.stat()
                    st_val = Stat(entry.name, st.st_mode, entry.path, st.st_uid, st.st_gid, st.st_size,
                                  st.st_atime, st.st_mtime, st.st_ctime)
                    fobject = File(stat=st_val)
                if entry.is_dir():
                    print("Dir is {0} ".format(entry.name))

if __name__ == '__main__':
    c = Crawler()
    c._scandir(path='c:\\')
