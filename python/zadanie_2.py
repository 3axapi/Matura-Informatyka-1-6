from YYY_data import employee_data
# dane do 2020-12-10 (Z, P, D)
from zadanie_1 import Z, P, D

employees = []

for employee in employee_data:
    employees_contracts = [[employee[1], employee[2]], []]
    for z in Z:
        if employee[0] == z[0]:
            employees_contracts[1].append("Z")
    for p in P:
        if employee[0] == p[0]:
            employees_contracts[1].append("P")
    for d in D:
        if employee[0] == d[0]:
            employees_contracts[1].append("D")
    
    employees.append(employees_contracts)

most_contracts = [[], []]

for employee in employees:
    if len(employee[1]) > len(most_contracts[1]):
        most_contracts = employee