import sys
from argparse import ArgumentParser
from .lookfor import find_dir, find_ext_all, find_ext_in_dir, find_file, search_file


def main():

    argparser = ArgumentParser(description='Look for things...')
    argparser.add_argument("--file", "-f", help="search for file in all directories starting with the current directory")
    argparser.add_argument("--dir", "-d", help="searches for dir in all directories starting with current directory")
    argparser.add_argument("--extall", "-ea", help="searches for all files with ext in all directories starting with current directory")
    argparser.add_argument("--extin", "-ei", help="search for all files with ext only in current directory. Does not go into subdirectories")
    argparser.add_argument("--search", "-s", nargs=2, help="search a file for a string. Returns an object")

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
    else:
        print('nope!')

if __name__ == "__main__":
    main()
    



