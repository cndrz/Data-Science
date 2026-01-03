import pandas as pd

employee_data = {

    "Employee" : ["Ally", "JM", "Zowi", "Cookie"],
    "Department" : ["Marketing", "IT", "HR", "Sales"],
    "Salary" : [25000, 20000, 55000, 45000]

}

df = pd.DataFrame(employee_data)
dept_average = df.groupby("Department")["Salary"].mean()
max_salary = df["Salary"].max()

print("Average Salary Per Department")
print(dept_average)