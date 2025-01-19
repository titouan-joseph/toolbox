# MTU Finder

## Summary

Tool who finds the MTU with no fragmentation in a network.

## Usage

You can use in cli with Linux or Windows. The two binary are in ``dist`` folder.  

```bash
$ cd dist
# Linux
$ sudo ./MTUfinder <ip or FQDN>
# Windows
$ MTUfinder.exe <ip or FQDN>
```

You can use the ``-d`` option to see debug with MTU size who is tested.

## Dev

To improve the script, you can change it.  
All requirements are in ``requirements.txt``. You can install with ``pip install -r requirements.txt``.  
And for make binary, you can use ``pyinstaller``.

```bash
pip install pyinstaller
pyinstaller --onefile --name=MTUfinder MTU-finder.py
```

For make a binary in linux you can use WLS. Pyinstaller have not cross-platform support.
