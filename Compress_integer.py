N = list(input().strip())
new = []
print(N)
def cont(lst:list):
    global new
    new = []
    for i in range(len(lst)):
        if len(lst) == 1:
            print(new)
            break
        else:
            F = lst.pop(0)
            S = lst[0]
            FS = int(F) + int(S)
            if len(str(FS)) >= 2:
                FS = str(FS)
                FS = int(FS[0]) + int(FS[1])
            new.append(str(FS))
    if len(new) != 1:
        cont(new)

cont(N)
print(*new)