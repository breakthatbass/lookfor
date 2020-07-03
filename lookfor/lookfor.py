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
    count = 0 #keep track of number of found files
    for root, dirs, files in os.walk('.'):
        for name in files:
            if name.endswith(ext):
                # if found, print path to file
                print(os.path.join(root, name))
                count += 1
    return 'found {} {} files'.format(count, ext)


def find_ext_in_dir(ext):
    '''search for all files with ext only in current directory. Does not go into subdirectories'''
    count = 0 # keep track of number of found files
    for root, dirs, files in os.walk('.'):
        dirs.clear()
        for name in files:
            if name.endswith(ext):
                # if found, print path to file
                print(os.path.join(root, name))
                count += 1
    return 'found {} {} files'.format(count, ext)


def find_file(file):
    pass
