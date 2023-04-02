# Cameron Medsker

# GPA.py

# This application will determine if a student is has made the Dean's List or
# Honor Roll. It will not accept the last name 'ZZZ' and will not tell the student
# if they make neither the Dean's List or Honor Roll



# A while True loop to continue indefinitely
while True:
    # Asking the user for their last name
    last_name = input("What is your last name?:\n")

    # It will continue if the last name is not ZZZ, and otherwise exit
    if last_name != 'ZZZ':
        # Asking the user for their first name
        first_name = input("What is your first name?:\n")

        # Asking the user for their GPA
        gpa = float(input("What is your GPA?:\n"))

        # Checking if the user has made the Dean's List, or the Honor Roll.
        if gpa >= 3.5:
            print(f"Congrats {first_name} {last_name} you have made the Dean's List!")
        elif gpa >= 3.25:
            print(f"Congrats {first_name} {last_name} you have made the Honor Roll!")
    else:
        exit