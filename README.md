# lookfor

```lookfor``` is a simple command line tool to find things: files, directories, files by extension, and strings within files.

It's like ```find``` and ```grep``` built into one program only it's slower and way less powerful.

### Installation

```git clone https://github.com/breakthatbass/lookfor.git```

```cd lookfor```

```pip install .```


### Usage

```lookfor <command> [arguments]```

#### Commands:
```
--file, -f file                 search for <file> in all directories starting with current directory
--dir, -d  directory            search for <dir> in all directories starting with current directory
--extall, -ea .ext              search for all files with <.ext> in all directories starting with current directory
--extin, --ei .ext              search for all files with <.ext> only in current directory
--search, -s str file           search a file for a string. Returns an object
--replace, -r file str newstr   search a file for a string and replace it
```

### Examples:

```lookfor -f file.py``` 
- returns ```path/to/file``` or ```None```.

```lookfor -d directory``` 
- returns ```path/to/dir``` or ```None```.

```lookfor -ea .py``` 
- returns ```path/to/file.py``` for every ```.py``` file found with count or ```found 0 .py files``.

