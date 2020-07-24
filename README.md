# lookfor

```lookfor``` is a simple command line tool to find things: files, directories, files by extension, and strings within files.

It's like ```find``` and ```grep``` built into one program only it's slower and way less powerful.

### Installation

```git clone https://github.com/breakthatbass/lookfor.git```

```cd lookfor```

```pip install .```


### Usage

```lookfor <command> [arguments]```

#### The commands are:
```
--file, -f file         search for <file> in all directories starting with current directory
--dir, -d  directory    search for <dir> in all directories starting with current directory
--extall, -ea .ext      search for all files with <.ext> in all directories starting with current directory
--extin, --ei .ext      search for all files with <.ext> only in current directory
--search, -s str file   search a file for a string. Returns an object
```

#### Examples:
```lookfor --file file.ext``` would return ```path/to/file.ext``` if it exists or ```None``` if it doesn't.

```lookfor --dir dir``` would return ```./path/to/dir``` if it exists or  ```None``` if it doesn't.

```lookfor --extall .ext``` would return the path to every ```.ext``` file starting from the current directory. It then prints the number of files found. If none exist, it would return ```found 0 .ext files```.

```lookfor --extin .ext``` only searches the current directory for the files. It then prints the number of files found. If none exist, it would return ```found 0 .ext files```.

```lookfor --search str file.ext``` would return an object like ```{'string': str, 'count': 6, 'found on lines': '[3, 12, 24, 37, 46, 49]'}``` if the str is in the file. Otherwise, it returns ```Not Found```.

### TODO
- add colors for files and directories
- do a null check after file open in search_file function
- create a replace function to replace strings in files
- add function to look for string in all files in directory