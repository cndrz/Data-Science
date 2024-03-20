def Oops_select():

    print("A. The Service Weapon")
    print("B. The Hotline")
    print("C. The Floppy Disk")
    print("D. The Home Safe")
    print("E. The Benicoff TV")
    print("F. The Merry-Go-Round Horse")
    print("G. The Slide Projector")
    print("H. The Songmaster Jukebox")
    print("I. The X-Ray Light Box")
    print("J. The Ashtray and Cigarette")

    A = 
    B = 
    C = 
    D = 
    E = 
    F = 
    G = 
    H = 
    I = 
    J = 

    while True:
        try:

            choice = input("Enter your choice: ")
            
            match choice:
                case "A":
                     with open(A, "r") as Service_Weapon:
                        file_1 = Service_Weapon.read()
                        print(file_1)
                        break

                case "B":
                     with open(B, "r") as Hotline:
                        file_2 = Hotline.read()
                        print(file_2)
                        break

                case "C":
                     with open(C, "r") as Floppy_Disk:
                        file_3 = Floppy_Disk.read()
                        print(file_3)
                        break
                
                case "D":
                     with open(D, "r") as Home_Safe:
                        file_4 = Home_Safe.read()
                        print(file_4)
                        break

                case "E":
                     with open(E, "r") as Benicoff_TV:
                        file_5 = Benicoff_TV.read()
                        print(file_5)
                        break
                     
                case "F":
                     with open(F, "r") as Horse:
                        file_6 = Horse.read()
                        print(file_6)
                        break
                     
                case "G":
                     with open(G, "r") as Slide_Projector:
                        file_7 = Slide_Projector.read()
                        print(file_7)
                        break

                case "H":
                     with open(H, "r") as Jukebox:
                        file_8 = Jukebox.read()
                        print(file_8)
                        break    
                     
                case "I":
                     with open(I, "r") as X_Ray:
                        file_9 = X_Ray.read()
                        print(file_9)
                        break

                case "J":
                     with open(J, "r") as Ash_Cig:
                        file_10 = Ash_Cig.read()
                        print(file_10)
                        break 
                    

                case _:
                    print("Invalid choice. Please enter a valid option (A, B, C, D, E)")

        except Exception as x:
            print(f"An error occurred: {x}. Please try again.")