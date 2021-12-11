# Motif discovery is one of the sequence analysis
# problems under the application layer and it is one
# of the significant difficulties in bioinformatics applications.
# A DNA sequence motif is a subsequence of DNA sequence that is a
# short similar recurring pattern of nucleotides, and it has many
# biological functions

# motif finding


import random
from Bio import Seq
from Bio import SeqUtils
I = int(input("enter the length of motif:-"))
file = open("h1n1.txt", "r")
r = file.read()
print("sequence:\n", r)
size = len(r)
print("size of the sequence:", size)
pos = random.randint(0, len(r)-I)
print("position", pos)
motif = r[pos:pos+I]
print("motif", motif)
results = SeqUtils.nt_search(str(r), motif)
print("Match motif:", results)

i = pos+1
while(i < size-1):
    if(motif == r[i:i+I]):
        str1 = r[i:i+I]
        print("match motif:", str1)
        file1 = open("motoutput.txt", "a")
        file1.write(str1+"")
    i += 1
