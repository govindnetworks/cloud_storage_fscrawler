#
# Apache License 2.0
#
import os
from collections import namedtuple
from multiprocessing import Process

Stat = namedtuple('stat', ['name', 'mode', 'path', 'uid', 'gid', 'size', 'atime', 'mtime', 'ctime'])


class Base(object):

    def __init__(self, *args, **kwargs):
        pass

    def get_meta_info(self):
        pass

    def __repr__(self):
        return os.path.join(self.path, self.name)

    def __str__(self):
        return os.path.join(self.path, self.name)


class File(Process):

    def __init__(self, *args, **kwargs):
        super(File, self).__init__()
        self.stat = kwargs.get('stat')
        # print(self.stat.stat())

    def run(self):
        #st = self.stat.stat()
        # st_val = Stat(self.stat.name, st.st_mode, self.stat.path, st.st_uid, st.st_gid, st.st_size,
        #              st.st_atime, st.st_mtime, st.st_ctime)
        pass
        return


class Directory(object):
    pass
# class Directory(Base):
#     directory_count = 0

#     def __init__(self, *args, **kwargs):
#         super(Directory, self).__init__(self, *args, **kwargs)
#         self.children = []
#         self.stat = Stat()

#     def update_stat(self, stat):
#         self.stat = stat

#     def append_child(self, child, directory=False):
#         self.children.append(child)
#         if directory:
#             directory_count = directory_count + 1

#     def remove_child(self, child):
#         self.children.remove(child)

#     def component_function(self):
#         self.meta_info = Stat()


if __name__ == '__main__':
    file = File()
    print(file)
