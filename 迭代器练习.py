from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import time
han=open('E:/序列文件/试验小数据/新建文本文档.txt')
seqs =SeqIO.parse(han,'fasta')
while True:
    try:
        seq_record=next(seqs)
        print(seq_record)
    except StopIteration:
        break
