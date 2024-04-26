import os
old = "old.txt"
new = "new.txt"

with open(old, 'r') as r:
    data = r.read()

with open(new, 'w') as r:
    r.write(data)

os.remove(old)
