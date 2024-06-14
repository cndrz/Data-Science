import importlib

def select_section():

    print("Welcome To XXX Mailing Company")
    print("Select Your Designated Section")
    print("A. Mail Sorting Sect.")
    print("B. Delivery Sect.")
    print("C. Customer Service Sect.")

    while True:

        user_input = input("--> ").upper()

        match user_input:

            case "A":

                try:
                    module = importlib.import_module("FUNCTIONS")
                    module.mailing()

                except ImportError:
                    print("Error: The FUNCTIONS.py file could not be found.")

                except AttributeError:
                    print("Error: The FUNCTIONS.py file does not contain a mailing() function.")

                break

            case "B":

                try:
                    module = importlib.import_module("FUNCTIONS")
                    module.delivery()

                except ImportError:
                    print("Error: The FUNCTIONS.py file could not be found.")

                except AttributeError:
                    print("Error: The FUNCTIONS.py file does not contain a delivery() function.")

                break

            case "C":

                try:
                    module = importlib.import_module("FUNCTIONS")
                    module.css()

                except ImportError:
                    print("Error: The FUNCTIONS.py file could not be found.")

                except AttributeError:
                    print("Error: The FUNCTIONS.py file does not contain a css() function.")

                break

            case _:

                print("Invalid selection. Please choose A, B, or C.")


select_section()