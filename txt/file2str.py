import glob

files = glob.glob("*.txt")



text = '`,`'

for file in files:
    with open(file, 'r', encoding='latin1') as f:
        text += f.read()


with open('filename.txt', 'w',encoding='latin1') as filew:
    filew.write(text)