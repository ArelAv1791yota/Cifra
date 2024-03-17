List = [-5, 1, 2, 3, 4, 5, 35]


def function(List):
    Out = []

    start = fin = List[0]
    for ind in List[1:]:
        if ind == fin + 1:
            fin = ind
        else:
            Out.append((start, fin))
            start = fin = ind
    Out.append((start, fin))

    return (Out)


result = function(List)

# Два варианта:
print([(f"[{start} - {fin}]") if start != fin else f"[{start}]" for start, fin in result])

for i in result:
    if i[0] != i[1]:
        print(f"[{i[0]} - {i[1]}] ", end="")
    else:
        print(f"[{i[0]}] ", end="")