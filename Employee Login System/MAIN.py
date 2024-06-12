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
                    mailing_module = importlib.import_module("MAILING")
                    mailing_module.mailing()

                except ImportError:
                    print("Error: The MAILING.py file could not be found.")

                except AttributeError:
                    print("Error: The MAILING.py file does not contain a mailing() function.")

                break

            case "B":

                try:
                    delivery_module = importlib.import_module("DELIVERY")
                    delivery_module.delivery()

                except ImportError:
                    print("Error: The DELIVERY.py file could not be found.")

                except AttributeError:
                    print("Error: The DELIVERY.py file does not contain a delivery() function.")

                break

            case "C":

                try:
                    css_module = importlib.import_module("CSS")
                    css_module.css()

                except ImportError:
                    print("Error: The CSS.py file could not be found.")

                except AttributeError:
                    print("Error: The CSS.py file does not contain a css() function.")

                break

            case _:

                print("Invalid selection. Please choose A, B, or C.")


select_section()