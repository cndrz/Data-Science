def main_menu():

    import BRC_sectors
    import BRC_Oops
    import BRC_awes
    import BRC_Dinfo

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
                    BRC_sectors.sector_select()
                    break

                case "B":
                    BRC_Oops.Oops_select()
                    break

                case "C":
                    BRC_awes.awes_select()
                    break
                
                case "D":
                    BRC_Dinfo.dossier_info()
                    break

                case _:
                    print("Invalid choice. Please enter a valid option (A, B, C, D)")

        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")


main_menu()