def get_user_name ():
    name = input ("Enter your name: ")
    return(name)

def get_user_age ():
    while True:
        age = input("Enter your age: ")

        if age.isdigit():
            age = int(age)

            if age > 0:
                return age
            else:
                print("Age must be greater than 0.")
        else:
           print("Please enter a valid age.")     

def get_numbers():
    numbers = []

    while True:
        value = input("Enter a number (or 'q' to finish): ")

        if value.lower() == "q":
            if len(numbers) == 0:
                print("Please enter at least one number.")
            else:
                return numbers

        elif value.isdigit():
            numbers.append(int(value))
        else:
            print("Invalid input.")

def main ():
    print ("Python Fundamentals Project started")
    
    user_name = get_user_name()
    print ("Hello", user_name)

    user_age = get_user_age()
    print ("Your age is", user_age)

    numbers = get_numbers()
    print("You entered:", numbers)  

     print("Program finished successfully.")    

main()
