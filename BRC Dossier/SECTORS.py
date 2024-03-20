def sector_select():

    print("A. Executive Sector")
    print("B. Containment Sector")
    print("C. Investigations Sector")
    print("D. Maintenance Sector")
    print("E. Research Sector")

    A = r"C:\Users\admin\Desktop\Python\BRC Dossier\BRC Sectors\Executive Sector.txt"
    B = r"C:\Users\admin\Desktop\Python\BRC Dossier\BRC Sectors\Containment Sector.txt"
    C = r"C:\Users\admin\Desktop\Python\BRC Dossier\BRC Sectors\Investigations Sector.txt"
    D = r"C:\Users\admin\Desktop\Python\BRC Dossier\BRC Sectors\Maintenance Sector.txt"
    E = r"C:\Users\admin\Desktop\Python\BRC Dossier\BRC Sectors\Research Sector.txt"

    while True:
        try:
            
            choice = input("Enter your choice: ")
            
            match choice:
                case "A":
                     with open(A, "r") as Executive_Sector:
                        file_1 = Executive_Sector.read()
                        print(file_1)
                        break

                case "B":
                     with open(B, "r") as Containment_Sector:
                        file_2 = Containment_Sector.read()
                        print(file_2)
                        break

                case "C":
                     with open(C, "r") as Investigations_Sector:
                        file_3 = Investigations_Sector.read()
                        print(file_3)
                        break
                
                case "D":
                     with open(D, "r") as Maintenance_Sector:
                        file_4 = Maintenance_Sector.read()
                        print(file_4)
                        break

                case "E":
                     with open(E, "r") as Research_Sector:
                        file_5 = Research_Sector.read()
                        print(file_5)
                        break

                case _:
                    print("Invalid choice. Please enter a valid option (A, B, C, D, E)")

        except Exception as x:
            print(f"An error occurred: {x}. Please try again.")