import os

def find_dir(dir):
    '''searches for dir in all directories starting with current directory'''
    for root, dirs, files in os.walk('.'):
        for name in dirs:
            if name == dir:
                return os.path.join(root, name)
                # if not found, it returns None


def find_ext_all(ext):
    '''searches for all files with ext in all directories starting with current directory'''
    pass