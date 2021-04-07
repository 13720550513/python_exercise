from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
han=open('E:/序列文件/ath_circ_026074.result')
datals=[]
finaldata=[]
for line in han:
    line=line.replace('\n','')
    line=line.replace('\t',',')
    datals.append(list(line.split(','))[0])
han.close()
print(datals)
print(len(datals))
'''
for i in range(len(datals)):
    if datals[i][1]=='IRES':
        finaldata.append(datals[i])
print(finaldata)
print(len(finaldata))
'''





#提取含有IRES的信息
