### git internals
https://git-scm.com/book/en/v2/Git-Internals-Git-Objects

to see object content:
```bash
git cat-file -p <object-hash>
```

to see raw object:
```bash
cat <git-object-file> | python -c "import sys;print repr(sys.stdin.read().decode('zip'))"
```
