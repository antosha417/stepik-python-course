class Error:
    def __init__(self, name, parents):
        self.name = name
        self.parents = parents
        
    def is_parent(self, name, errors):
        if name in self.parents:
            return True
        else:
            return any([errors[par].is_parent(name, errors)
                        for par in self.parents])

ERRORS = {}
n = int(input())
for elem in range(n):
    line = input().split(' : ')
    line.append('')
    ERRORS[line[0]] = Error(line[0], line[1].split())
res = []
true_res = []
n = int(input())
for i in range(n):
    temp = input()
    if any(ERRORS[temp].is_parent(j, ERRORS) for j in res):
        true_res.append(temp)
    else:
        res.append(temp)

for i in true_res:        
    print(i)
