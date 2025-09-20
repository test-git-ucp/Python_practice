text=input("enter the string:")
n=text.split()
print(len(n))
print(n)
space_count = text.count(" ")
print("Spaces:", space_count)
cahr_count=len(text)
print("total character are in text is :",cahr_count)
fre={}
space=0
for word in n:
    if word in fre:
        fre[word]+=1

    else:
        fre[word]=1
print("frequency of words:")
for word,count in fre.items():
    print(f"{word}",count)  
    
withoutspace=cahr_count-space_count
print("words without space",withoutspace)

sentence=0
for char in text:
     if char in ".!?":
       sentence+=1       
    
print("number of sentence is:",sentence)