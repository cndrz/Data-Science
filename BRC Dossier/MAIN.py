def main_menu():

    import SECTORS
    import OOPS
    import AWES
    import INFO

    print("--- Welcome to the BRC Dossier ---")
    print("A. BRC Sectors")
    print("B. Objects of Power")
    print("C. Altered World Events")
    print("D. What is the BRC Dossier?")

    while True:
        try:
            choice = input("Enter your choice: ")
            
            match choice:
                case "A":
                    SECTORS.sector_select()
                    break

                case "B":
                    OOPS.Oops_select()
                    break

                case "C":
                    AWES.awes_select()
                    break
                
                case "D":
                    INFO.dossier_info()
                    break

                case _:
                    print("Invalid choice. Please enter a valid option (A, B, C, D)")

        except Exception as x:
            print(f"An error occurred: {x}. Please try again.")


main_menu()