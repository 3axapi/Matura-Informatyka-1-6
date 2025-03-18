from YYY_data import employee_data, child_data

parents = []
parent_initials = []
has_child = False

# don't have own childs
for employee in employee_data:
    for parent in child_data:
        if employee[0] == parent[0]:
            has_child = True
            
    if has_child:
        has_child = False
    else:
        parents.append(employee)

# bubble sorting
for i in range(len(parents)):
    for j in range(len(parents)):

        if j == len(parents)-1:
            continue

        if parents[j][1] > parents[j+1][1]:
            following = parents[j+1]
            parents[j+1] = parents[j]
            parents[j] = following

for parent in parents:
    parent_initials.append(f"{parent[2]} {parent[1]}")