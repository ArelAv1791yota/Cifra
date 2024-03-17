List = [-5, 1, 2, 3, 4, 5, 35]

class Functionals():
    def __init__(self, List):
        self.List = List
        self.Out = []
        self.function()
        self.display_out()
    def function(self):
        start = fin = self.List[0]
        for ind in List[1:]:
            if ind == fin + 1:
                fin = ind
            else:
                self.Out.append((start, fin))
                start = fin = ind
        self.Out.append((start, fin))
        return self.Out

    def display_out(self):
        print([(f"[{start} - {fin}]") if start != fin else f"[{start}]" for start, fin in self.Out])


Started = Functionals(List)


# result = function(List)
#
# # Два варианта:
# print([(f"[{start} - {fin}]") if start != fin else f"[{start}]" for start, fin in result])
#
# for i in result:
#     if i[0] != i[1]:
#         print(f"[{i[0]} - {i[1]}] ", end="")
#     else:
#         print(f"[{i[0]}] ", end="")