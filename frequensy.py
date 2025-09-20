n="hello kia hal ha mia sb  hello hello is kia hal ha mia sb"
words=n.split()
frequency={}
for word in words:
    if word in frequency:
        frequency[word]+=1
    else:
         frequency[word]=1
         
for word,count in frequency.items():
    print(f"{word}",count)         
         