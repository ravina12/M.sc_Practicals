seq1=list(input("enter the first sequence:"))
seq2=list(input("enter the second sequence:"))

#for identity
score=[]
def identity(a,b):
    value=0
    length=len(a)
    for i in range(0,length):
        if(a[i]==b[i]):
            score.append('1')
            value=value+1
        else:
            score.append('0')
    return value

#for similarity
how_many=int(input("how many elements for similarity condition?:"))
similarities=[]
for i in range(0,how_many):
    a=input("enter an element:")
    c=int(input("how many elements is it similar to?:"))
    similarities.append([])
    similarities[i].append(a)

    for j in range(0,c):
        b=input("what is it similar to?:")
        similarities[i].append(b)

def compare(o,t,s):
    print(o)
    print(t)
    print(s)
    #checking if similar
    score=0
    for i in range(len(o)):
        for j in range(len(s)):
            if o[i] in s[j] and t[i] in s[j] and o[i]!=t[i]:
                score+=1
    #calculating similarity
    similarity=score
    return similarity

identi=(identity((seq1),(seq2)))
simi=(compare((seq1),(seq2),similarities))
print("similarity of the sequences:",simi)
print("identity of the sequences:",identi)
total=identi+simi

#counting
gap_in_sequence1=seq1.count('-')
gap_in_sequences2=seq2.count('-')
total_gap=gap_in_sequence1+gap_in_sequences2
print("gap in the sequences",total_gap)

percentage_of_sequence=(total/(len(seq1)-total_gap))*100
print("percentage of the sequence are:",percentage_of_sequence,"%")
