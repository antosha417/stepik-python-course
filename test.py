class Class:
    def __init__(self, name, parents):
        self.name = name
        self.parents = parents

    def is_parent(self, name, classes_dict):
        if name in self.parents:
            return True
        else:
            return any([classes[par].is_parent(name, classes_dict)
                        for par in self.parents])

classes = {}
n = int(input())
for i in range(n):
    line = input().split(' : ')
    if len(line) == 1:
        classes[line[0]] = Class(line[0], [])
    else:
        classes[line[0]] = Class(line[0], line[1].split())
    
n = int(input())
for i in range(n):
    line = input().split()
    if line[1] in classes:
        if classes[line[1]].is_parent(line[0], classes) or line[1] == line[0]:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
