letters='ABCBC'
count=0
for i in range(len(letters)):
    rec_l=i
    for j in range(i+1,len(letters)):
        if count==0:
            if letters[j]==letters[rec_l]:
                print(letters[rec_l],letters[j])
                count=count+1
        
