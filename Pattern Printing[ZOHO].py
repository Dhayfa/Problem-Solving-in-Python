S = list(input().strip()) #gets input
new_S = []
Space = (len(S) -2) 
mid = S[(len(S)//2)] #finds the mid value and seprates it

for i in range(len(S)//2 +1): #creates a list with proper spacing in between words and segregates words
    if Space < 0:
        break
    new_S.append(S[i]+" "*Space+S[-i-1])
    Space -= 2

final_S = [] #saves the output so it could reverse it later

for i , j in enumerate(new_S): #prints the first half of output
    final_S.append(" "*i+j)
    print(' '*i +j)
    
print(" "*(len(S)//2)+mid) #print the mid value

for i in final_S[::-1]: #prints the second half of the input which is just reverse of the first half
    print(i)
