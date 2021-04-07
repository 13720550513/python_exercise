def gettext():
    txt=open("1.txt","r").read()
    txt=txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_{}`~':
        txt=txt.replace(ch," ")
    return txt

newtxt=gettext()
words=newtxt.split()
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print("{:.<10}--{:>5}".format (word,count))
