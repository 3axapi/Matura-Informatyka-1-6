from YYY_data import employment_data

year, month, day = "", "", ""
D, N, P, Z = [], [], [], []

for employee in employment_data:
    if employee[1] != "N":
        up_to_date = employee[3][:10]

        if up_to_date < "2020-12-10":
            continue

    if employee[1] == "D":
        D.append(employee)
    elif employee[1] == "N":
        N.append(employee)
    elif employee[1] == "P":
        P.append(employee)
    elif employee[1] == "Z":
        Z.append(employee)