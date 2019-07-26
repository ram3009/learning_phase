
_input=int(input("Enter any three digit number : "))
sum=0
for x in range(100,_input+1):                     # search begins from 100 to User entered input
        l_digit=x%10                              # last digit is detected
        as_string=str(l_digit)                    # here i'm changing it as string 
        sum=x+x+x                                 # here i'm doing the addition of that number three times
        _sum=str(sum)                             # changing the result sum into string to check the length exceed 3 or not

        if _sum[0] == as_string and _sum[1] == as_string and _sum[2] == as_string :
            print(f"The Number we are searching for is {x}")                         
            print(f"Sum of that number is:{_sum}")

        sum_length=len(_sum)            
        if sum_length>3:
            print(f"Addition of {x} 3 times exceeds 4 digits : {sum} ")
            break
       



