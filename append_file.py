__author__ = 'CombineFile'

fo = open("file1.txt", "r")

for line in fo.readlines():
    print line

fo.close()
