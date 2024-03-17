List = [-5, 1, 2, 3, 4, 5, 35]
Out = []
Flag = False
List.append(0)
for i in range(len(List)-1):
    if List[i]+1 == List[i+1]:
        if Flag == False:
            Out.append(f'[{List[i]}')
        Flag = True
    else:
        if Flag:
            Out.append(f'{List[i]}]')
            Flag = False
    if (List[i-1]+1 != List[i]) and (List[i] != List[i+1]-1):
        Out.append(f'[{List[i]}]')
print(Out)
