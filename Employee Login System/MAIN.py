import importlib

def handle_section(function_name):

    try:

        module = importlib.import_module("FUNCTIONS")
        function = getattr(module, function_name)
        function()

    except ImportError:

        print("Error: The FUNCTIONS.py file could not be found.")

    except AttributeError:

        print(f"Error: The FUNCTIONS.py file does not contain a function named '{function_name}'.")

def display_menu():

    print("Welcome To XXX Mailing Company")
    print("Select Your Designated Section")
    print("A. Mail Sorting Sect.")
    print("B. Delivery Sect.")
    print("C. Customer Service Sect.")

def select_section():

    display_menu()
    
    while True:

        user_input = input("--> ").upper()

        if user_input in ['A', 'B', 'C']:
            
            break

        else:

            print("Invalid selection. Please choose A, B, or C.")

    if user_input == "A":

        handle_section("mailing")

    elif user_input == "B":

        handle_section("delivery")

    elif user_input == "C":

        handle_section("css")

if __name__ == "__main__":

    select_section()
