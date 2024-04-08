import WEBSITES

def main():

    while True:

        print("CHOOSE YOUR WEBSITE")
        print("A. Google")
        print("B. Facebook")
        print("C. YouTube")
        print("D. Instagram")
        choice = input(">>> ")

        try:

            match choice:

                case "A": 
                    WEBSITES.google_url()

                case "B": 
                    WEBSITES.facebook_url()
                    
                case "C": 
                    WEBSITES.youtube_url()

                case "D":
                    WEBSITES.instagram_url()

                case _ : 
                    print("Invalid choice. Please choose again.")
                    continue

        except Exception as e:
            print("An error occurred:", e)
            continue

    

if __name__ == "__main__":
    main()