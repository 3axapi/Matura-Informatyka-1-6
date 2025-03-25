from YYY_data import employee_data, child_data

childless_parents = []
majority_children = [None, 0]

for parent in employee_data:
    if parent[3] == "S":
        childless_parents.append([parent, 0])

for i in range(len(childless_parents) - 1):
    for curr in child_data:
        # if costumer_PESEL = paren_PESEL
        if childless_parents[i][0][0] == curr[0]:
            childless_parents[i][1] = childless_parents[i][1] + 1

for s_parent in childless_parents:
    if s_parent[1] > majority_children[1]:
        majority_children = s_parent