# lookfor

```lookfor``` is a simple command line tool to find things: files, directories, files by extension, and strings within files.

It's not as powerful as ```find``` or ```grep``` but it's way simpler to use. 

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