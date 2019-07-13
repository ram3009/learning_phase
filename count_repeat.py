#Fucntion to find the maximum repeated character
def d_find_repeated(d_sequence):
     max_occurence=0
     d_repeated_list=[]
     d_unique=set(d_sequence)
     for i in d_unique:
         if d_sequence.count(i)>=max_occurence:
             max_occurence=d_sequence.count(i)
             d_repeated_list.append(i)
     #returns the char only if it is the maximum
     #if more than one char has same count it returns none
     return d_repeated_list if len(d_repeated_list)==1 else None

#Enter the character with space to split
d_sequence=input("Plese enter the characters with space: ").split()
#Just printing the input after split
print(d_sequence)
print(d_find_repeated(d_sequence))
