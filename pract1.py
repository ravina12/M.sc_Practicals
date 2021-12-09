se1=input("enter the first sequence:")
se2=input("enter the second sequence:")
seq1=list(se1)
seq2=list(se2)
score=[]

def pairwise_alignment(a,b):
    gap(a,b)
    print(a)
    print(b)
    value=0
    length=len(a)
    for i in range(0,length):
        if(a[i]==b[i]):
            score.append('1')
            value=value+1
        else:
            score.append('0')
    print(score)
    print(value)

def gap(a,b):
    if (len(a)==len(b)):
        print()
    else:
        k=int(input("enter the position to insert gap'_':"))
        if(len(a)<len(b)):
            a.insert(k,'_')
        else:
            b.insert(k,'_')
    return(a,b)

pairwise_alignment(seq1,seq2)
