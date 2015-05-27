import glob
import shutil

CONTENT = "content"

for name in glob.iglob("../user_data/*"):
    shutil.copyfile(CONTENT, name)

print 'git commit -am "changed content of ALL files"'

