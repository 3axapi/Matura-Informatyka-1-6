i = 0

with open("./src/pracownik.txt", "r") as file:
    employee_data = file.readlines()
    del employee_data[0]
    for line in employee_data:
        employee_data[i] = line.split(";")
        employee_data[i][3] = line.split(";")[3][0]
        i+=1
    i = 0

with open("./src/zatrudnienie.txt", "r") as file:
    employment_data = file.readlines()
    del employment_data[0]
    for line in employment_data:
        employment_data[i] = line.split(";")
        try:
            employment_data[i][4] = line.split(";")[4][:-1]
        except IndexError:
            employment_data[i][3] = line.split(";")[3][:-1]
        i+=1
    i = 0

with open("./src/dziecko.txt") as file:
    child_data = file.readlines()
    del child_data[0]
    for line in child_data:
        child_data[i] = line.split(";")
        child_data[i][3] = line.split(";")[3][0]
        i+=1
    i = 0