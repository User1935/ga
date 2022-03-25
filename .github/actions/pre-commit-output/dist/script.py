import html2text
import sys
import os

# This script will format arg[1] text to a valid markdown language
# [INPUT] : arg1 -- html file
# [OUTPUT] : will be written to the same file

h = html2text.HTML2Text()

#if (sys.argv[1] != ''):
path2file = os.environ['GITHUB_WORKSPACE'] + "/something.txt"
print(path2file)
with open (path2file, "r") as myfile:
    data=myfile.readlines()

##bodydata = h.handle(data)
#bodydata = bodydata.replace('\n\n', '\n')
#arraydata = bodydata.split('\n')

finalstring = '# Pre-Commit Log 📈\n'
flag = False
for s in data:
    #s = h.handle(s)
    if('</style>' in s):
        flag = True
    if(flag):
        print(s)
        if not ('[INFO]' in s):
            if('Failed' in s or 'Passed' in s or 'Skipped' in s ):
                finalstring += '</pre></details><summary>' + s + '</summary><pre>'
            else:
                finalstring += s
finalstring += '</pre></details>'

with open (path2file, "w") as myfile:
    myfile.write(finalstring)
#else:
 #   print('Please add the file as argument. script.py [FILE_NAME]')
