def sector_select():

    print("A. Executive Sector")
    print("B. Containment Sector")
    print("C. Investigations Sector")
    print("D. Maintenance Sector")
    print("E. Research Sector")

    while True:
        try:
            choice = input("Enter your choice: ")
            
            match choice:
                case "A":
                     with open(r"C:\Users\admin\Desktop\Python\BRC Dossier\BRC Sectors", "r") as Executive_Sector:
                        file_1 = Executive_Sector.read()
                        print(file_1)
                        break

                case "B":
                     with open("file_A.txt", "r") as Containment_Sector:
                        file_2 = Containment_Sector.read()
                        print(file_2)
                        break

                case "C":
                     with open("file_A.txt", "r") as Investigations_Sector:
                        file_3 = Investigations_Sector.read()
                        print(file_3)
                        break
                
                case "D":
                     with open("file_A.txt", "r") as Maintenance_Sector:
                        file_4 = Maintenance_Sector.read()
                        print(file_4)
                        break

                case "E":
                     with open("file_A.txt", "r") as Research_Sector:
                        file_5 = Research_Sector.read()
                        print(file_5)
                        break

                case _:
                    print("Invalid choice. Please enter a valid option (A, B, C, D, E)")

        except Exception as x:
            print(f"An error occurred: {x}. Please try again.")