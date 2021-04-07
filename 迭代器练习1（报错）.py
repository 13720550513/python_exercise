from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
han=open('E:/序列文件/试验小数据/新建文本文档.txt')
seqs=SeqIO.parse(han,'fasta')
try:
    while True:
        x=next(seqs)
	print(x)
except StopIteration:
    print('end')
