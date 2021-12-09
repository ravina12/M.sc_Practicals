se1=input("enter the first sequence:")
se2=input("enter the second sequence:")
how_many=int(input("how many elements for similarity condition:"))
similarities=[]
for i in range(0,how_many):
    a=input("enter an element:")
    c=int(input("how many elements is it similar to?:"))
    similarities.append([])
    similarities[i].append(a)

    for j in range(0,c):
        b=input("what is it similar to?:")
        similarities[i].append(b)

def campare(o,t,s):
    print(o)
    print(t)
    print(s)
    #checking if similar
    score=0
    for i in range(len(o)):
        for j in range(len(s)):
            if o[i] in s[j] and t[i] in s[j] and o[i]!=t[i]:
                score+=1
    #calculating similarities
    similarity=(score*100)/len(o)
    return similarity

print(campare(list(se1),list(se2),similarities),"%")
    
