import copy
poem = [["Haha", "??"], ["Nono", "Yes yes"]]
c = copy.deepcopy(poem)
c[0][1] = "Gago"

print(poem, c)

c.append(["tanga ka", "bobo ka pa"])

print(c)

c[2][0] = "tarantado"
print(c)