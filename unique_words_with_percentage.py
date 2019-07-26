## find the unique words and its percentage
ur_input=input("Enter your sentence : ").split()
uniq_words=[]
print(ur_input)
for word in ur_input:
    if word not in uniq_words:
        uniq_words.append(word)
print(uniq_words)        
print(f"Total words are {len(ur_input)} and unique words are {len(uniq_words)}")
perc=(len(uniq_words)/len(ur_input))*100
print(f"The Percentage of Unique words among total is :{perc}")