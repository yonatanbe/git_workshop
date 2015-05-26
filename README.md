# git workshop
a workshop on git - how to create your PRs so others can merge them easily.

## Before You Start
Because we want everyone to use the same repository, please do this before doing anything else:

1. Click the '+' sign where it says: 'git_workshop/**_+_**'
1. that will create a fork for you automatically.
1. give your file the name of your team (or any other identifying name of your choice). try to make it special so there won't be clashes. also write some text in your file.
2. now click: create a pull-request, and then again, create a pull-request.
3. you're finished! thanks for doing this first before anything else. =)

### the git book
https://git-scm.com/doc

great source for all git users, be it first timer or savvy.







https://git-scm.com/book/en/v2/Git-Internals-Git-Objects

to see object content:
```bash
git cat-file -p <object-hash>
```

to see raw object:
```bash
cat <git-object-file> | python -c "import sys;print repr(sys.stdin.read().decode('zip'))"
```


