class employee_1:

    name = "Mark"
    gender = "Male"

    mother = "Matilda"
    father = "Joseph"

    sister = "Mary"
    brother = "Mario"

    animal = "Dog"

    def intro(x):
        print(f"My name is {x.name}")
        print(f"My gender is {x.gender}")
    
    def parents(x):
        print(f"My mother is {x.mother}")
        print(f"My father is {x.father}")
    
    def siblings(x):
        print(f"My sister is {x.sister}")
        print(f"My brother is {x.brother}")
    
    def pet(x):
        print(f"We have a pet {x.animal}")

employee = employee_1()

employee.intro()
employee.parents()
employee.siblings()
employee.pet()



