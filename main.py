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

def main ():
    print ("Python Fundamentals Project started")
    
    user_name = get_user_name()
    print ("Hello", user_name)

    user_age = get_user_age()
    print ("Your age is", user_age)
    
main()
