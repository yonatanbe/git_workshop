#! /usr/bin/python 

CONTENT_FILE = "../user_data/content"

f = open(CONTENT_FILE)
data = f.read().encode("rot13")
f.close()
f = open(CONTENT_FILE, 'w')
f.write(data)
f.close()

print 'git commit -am "changed content of file"'

