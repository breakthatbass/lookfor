import os, sys

def find_dir(dir):
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
    '''search for file in all directories starting with the current directory'''
    for root, dirs, files in os.walk('.'):
        for name in files:
            if name == file:
                return os.path.join(root, name)
    return None


def search_file(str, file):
    '''search a file for a string. Returns an object'''    
    found = False       # false by default
    count = 0           # keep track of each time str is found
    line_num = 1        # to keep track of what line the loop is on, needs to start at one
    lines_found = []    # keep a list of the lines that the str was located on

    if not os.path.exists(file):
        return 'Error opening file'
    else:
        f = open(file, 'r')
        for line in f:
            if str.lower() in line.lower(): # lower() for case insensitivity
                found = True
                count += 1
                lines_found.append(line_num)
            line_num += 1
        
        if count == 0:
            f.close()
            return 'Not Found'
        else:
            f.close()
            return {'string': str, 'count': count, 'found on lines': f"{lines_found}"}


def repstr(file, string, newstr):

    try:
        fp = open(file, 'r')
        filedata = fp.read()
        fp.close()

        newdata = filedata.replace(string, newstr)
        fp = open(file, 'w')
        fp.write(newdata)
        fp.close()

        print(f'{string} has been replaced with {newstr}')
        return 0
    except:
        return 1
