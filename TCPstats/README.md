# TCPstats

## Summary

Tool who display some TCP stats.

## Usage

You can use in cli with Linux

```bash
$ cd dist
# Linux
$ sudo ./tcpstats
```

You can use the `--help` option to know more.  
You can write in a file and use the `--log` option and graph the results with the `makeGraph` script.

## Dev

To improve the script, you can change it.  
All requirements are in ``requirements.txt``. You can install with ``pip install -r requirements.txt``.  
And for make binary, you can use ``pyinstaller``.

```bash
pip install pyinstaller
pyinstaller --onefile --name=tcpstats tcpStats.py
pyinstaller --onefile --name=makeGraph makeGraph.py
pyinstaller --onefile --name=networkSpeed networkSpeed.py
```
