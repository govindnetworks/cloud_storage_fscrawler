#
# Apache License 2.0
#
from collections import namedtuple


class Base(object):

    def __init__(self, *args, **kwargs):
        pass

    def get_meta_info(self):
        pass

    def __repr__(self):
        print(self.name, self.path)

    def __str__(self):
        print(self.name, self.path)


class File(base):

    def __init__(self, *args, **kwargs):
        super(File, self).__init__(*args, **kwargs)
        self.stat = Stat()

    def component_function(self):
        print "some function"


class Directory(Base):
    directory_count = 0

    def __init__(self, *args, **kwargs):
        super(Directory, self).__init__(self, *args, **kwargs)
        self.children = []
        self.stat = Stat()

    def update_stat(self, stat):
        self.stat = stat

    def append_child(self, child, directory=False):
        self.children.append(child)
        if directory:
            directory_count = directory_count + 1

    def remove_child(self, child):
        self.children.remove(child)

    def component_function(self):
        self.meta_info = Stat()


if __name__ == '__main__':
    file = File()
    print(file)
