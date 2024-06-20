import importlib

def handle_section(section_name, function_name):

    try:

        module = importlib.import_module("FUNCTIONS")
        func = getattr(module, function_name)
        func()

    except ImportError:

        print("Error: The FUNCTIONS.py file could not be found.")

    except AttributeError:
        
        print(f"Error: The FUNCTIONS.py file does not contain a {function_name} function.")

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

                handle_section("Mail Sorting", "mailing")
                break

            case "B":

                handle_section("Delivery", "delivery")
                break

            case "C":
                handle_section("Customer Service", "css")
                break
            case _:

                print("Invalid selection. Please choose A, B, or C.")

select_section()
