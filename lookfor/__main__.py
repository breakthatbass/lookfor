import sys
from argparse import ArgumentParser
from .lookfor import find_dir, find_ext_all, find_ext_in_dir, find_file, search_file, repstr

def print_usage():
    print('\nUsage: lookfor <command> [arguments]\n')
    print('--usage, -u:     Show this message and quit')
    print('--file, -f:      Searches for file recursively')
    print('--dir, -d:       Searches for directory recursively')
    print('--extall, -ea:   Searches for all files with ext recursively')
    print('--extin, -ei:    Searches for all files with ext in current directory')
    print('--search, -s:    Searches file for a string. Returns an object')
    print('--replace, -r:   Search a file for a string and replace it')


def main():

    argparser = ArgumentParser(description='Look for things...')
    argparser.add_argument("--file", "-f", help="search for filei n all directories recursively")
    argparser.add_argument("--dir", "-d", help="search for dir in all directories recursively")
    argparser.add_argument("--extall", "-ea", help="searches for all files with ext in all directories recursively")
    argparser.add_argument("--extin", "-ei", help="search for all files with ext only in current directory")
    argparser.add_argument("--search", "-s", nargs=2, help="search a file for a string. Returns an object")
    argparser.add_argument("--replace", "-r", nargs=3, help="search a file for a string and replace it")
    argparser.add_argument("--usage", "-u", action='store_true', help="shows better usage")

    results = argparser.parse_args()
    
    # FILE
    if results.file:
        find_file(results.file)
    # DIR
    elif results.dir:
        find_dir(results.dir)
    # EXT ALL DIRS
    elif results.extall:
        print(find_ext_all(results.extall))
    # EXT IN DIR
    elif results.extin:
        print(find_ext_in_dir(results.extin))
    # SEARCH FOR STRING
    elif results.search:
        print(search_file(results.search[0], results.search[1]))
    # REPLACE STRING
    elif results.replace:
        repstr(results.replace[0], results.replace[1], results.replace[2])
    # USAGE  ...better usage in my opinion
    elif results.usage:
        print_usage()
    # don't think it'll reach this but have it just in case
    else:
        print_usage()


if __name__ == "__main__":
    main()
