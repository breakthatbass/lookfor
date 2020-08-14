import sys
from argparse import ArgumentParser
from .lookfor import find_dir, find_ext_all, find_ext_in_dir, find_file, search_file, repstr

def print_usage():
    print('\nUsage: lookfor <command> [arguments]\n')
    print('--file, -f:      Searches for file recursively')
    print('--dir, -d:       Searches for directory recursively')
    print('--extall, -ea:   Searches for all files with ext recursively')
    print('--extin, -ei:    Searches for all files with ext in current directory')
    print('--search, -s:    Searches file for a string. Returns an object\n')
    print('--replace, -r:   Search a file for a string and replace it')


def main():

    argparser = ArgumentParser(description='Look for things...')
    argparser.add_argument("--file", "-f", help="search for filein all directories starting with the current directory")
    argparser.add_argument("--dir", "-d", help="search for dir in all directories starting with the current directory")
    argparser.add_argument("--extall", "-ea", help="searches for all files with ext in all directories starting with current directory")
    argparser.add_argument("--extin", "-ei", help="search for all files with ext only in current directory. Does not go into subdirectories")
    argparser.add_argument("--search", "-s", nargs=2, help="search a file for a string. Returns an object")
    argparser.add_argument("--replace", "-r", nargs=3, help="search a file for a string and replace it")

    results = argparser.parse_args()
    
    if results.file:
        print(find_file(results.file))
    elif results.dir:
        print(find_dir(results.dir))
    elif results.extall:
        print(find_ext_all(results.extall))
    elif results.extin:
        print(find_ext_in_dir(results.extin))
    elif results.search:
        print(search_file(results.search[0], results.search[1]))
    elif results.replace:
        repstr(results.replace[0], results.replace[1], results.replace[2])
    else:
        print_usage()


if __name__ == "__main__":
    main()
    



