se1=input("enter the first sequence:")
se2=input("enter the second sequence:")
seq1=list(se1)
seq2=list(se2)
def find_identity(a,b):
    gap(a,b)
    print(a)
    print(b)
    score=0
    length=len(a)
    total_elements=len(a)*len(b)
    for i in range(0,length):
        for j in range(0,length):
            if(a[i]==b[j]):
                score=score+1
    identity=(score/total_elements)*100
    print("matching score=",score)
    print("identity of the sequences=",identity)

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
find_identity(seq1,seq2)
    
