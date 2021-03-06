# lookfor

```lookfor``` is a simple command line tool to find things: files, directories, files by extension, and strings within files. 
It can also be used replace strings in files with new strings.

It's like ```find``` and ```grep``` built into one program only it's slower and way less powerful.

### Installation

```git clone https://github.com/breakthatbass/lookfor.git```

```cd lookfor```

```pip install .```


### Usage

```lookfor <command> [arguments]```

#### Commands:
```
--file, -f file                     search for <file> in all directories recursively
--dir, -d  directory                search for <dir> in all directories recursively
--extall, -ea .ext                  search for all files with <.ext> in all directories recursively
--extin, --ei .ext                  search for all files with <.ext> only in current directory
--search, -s str file               search a file for <str>. Returns an object with info if <str> is in file.
--replace, -r file str newstr       search a file for <str> and replace it with <newstr> in each instance.
```

### Examples:

```
lookfor -f file.py                  returns path/to/file.py if file.py exists.

lookfor -d directory                returns path/to/directory if directory exists.

lookfor -ea .py                     returns path/to/file.py for every .py file found.

lookfor -ei .py                     returns path/to/file.py for every .py file found.

lookfor -s file.py hello            returns an object "{'string': hello, 'count': 1, 'found on lines': 21}" or "Not Found".

lookfor -r file.py coffee decaf     returns "coffee has been replaced with decaf" or returns nothing if "coffee" isn't in file.py.
```