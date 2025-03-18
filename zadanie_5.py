from YYY_data import employment_data, child_data, employee_data

YYY = 0
employees = []

for employee in employment_data:
    if employee[1] == "P" or employee[1] == "N":
        employees.append(employee)
                
for parent in employees:
    if parent[1] == "P":
        data = parent[3][:10]
        if data < "2020-12-20":
            continue

    isAlong = False
    for employee in employee_data:
        if parent[0] != employee[0]:
            continue
        if employee[3] == "S":
            isAlong = True
    
    salary = 0
    s = 0
    for employee in employment_data: # !
        if parent[0] == employee[0]:
            salary += int(employee[2])
            s += 1
    # if s > 1:
    #     print(men[0])

    for child in child_data:
        if parent[0] != child[0]:
            continue
        
        year = child[1][:2]
        month = child[1][2:4]
        day = child[1][4:6]
        data = None # YYYY-MM-DD
        if month >= "21": # -20 for who was borned after 2000
            month = f"{int(month[0])-2}{month[1]}"
            data = f"20{year}-{month}-{day}"
        else:
            data = f"19{year}-{month}-{day}"

        if data > "2020-12-20" and data <= "1999-12-20":
            continue

        if data > "1999-12-20" and data <= "2002-12-20":
            if child[3] == "N":
                continue

        if salary < 5000:
            YYY += 500
        elif salary >= 5000 and salary <= 10000:
            YYY += 300
        elif salary > 10000:
            YYY += 100
        if isAlong:
            YYY += 200