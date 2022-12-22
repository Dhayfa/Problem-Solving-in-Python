S = list('tiger')
new_S = []
Space = (len(S) -2)
mid = S[(len(S)//2)]

for i in range(len(S)//2 +1): 
    if Space < 0:
        break
    new_S.append(S[i]+" "*Space+S[-i-1])
    Space -= 2

final_S = []
for i , j in enumerate(new_S):
    final_S.append(" "*i+j)
    print(' '*i +j)
print(" "*(len(S)//2)+mid)
for i in final_S[::-1]:
    print(i)