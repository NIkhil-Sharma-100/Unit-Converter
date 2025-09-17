# Class contain all functions 
class Unit_Conv:
    def dis(self,n,from_unit):
        if from_unit == "meter":
            return f"{n} m = {n/1000} km"
        elif from_unit == "kilometer":
            return f"{n} km = {n*1000} m"
        else:
            return "Please Enter Valid Input"

    def weight(self,n,from_unit):
        if from_unit == "gram":
            return f"{n} g = {n/1000} kg"
        elif from_unit == "kilogram":
            return f"{n} kg = {n*1000} g"
        else:
            return "Please Enter Valid Input" 

    def temp(self,n,from_unit):
        if from_unit == "fahrenheit":
            return f"{n} °F = {(n-32)*5/9} °C"
        elif from_unit == "celsius":
            return f"{n} °C = {(n*9/5)+32} °F"
        else:
            return "Please Enter Valid Input"


obj = Unit_Conv()                  
            
# Task menu
print("choose number which one do you want")
print("1. Distance   2. Weight   3.Temperature     0. Exit")    

while True:
    # Error handling
    try :       
        user_choice = int(input("\nYour choice : "))
        

        if user_choice == 1:
            while True:
                from_unit = input("\"meter/kilometer\" or 0 to exit: ").strip().lower()
                
                
                if from_unit  == "0":
                    break

                n = int(input("Enter convertible units : "))
                result = obj.dis(n,from_unit)
                if result:
                    print(result)
                else:    
                    print("Enter meter/kilometer")            

        elif user_choice == 2:
            while True:
                from_unit = input("\"gram/kilogram\" or 0 to exit: ").strip().lower()
                    

                if from_unit  == "0":
                    break

                n = int(input("Enter convertible units : "))
                result = obj.weight(n,from_unit)
                if result:
                    print(result)
                else:
                    print("Enter gram/kilogram") 

        elif user_choice == 3:
            while True:
                from_unit = input("\"celsius/fahrenheit\" or 0 to exit : ").strip().lower()


                if from_unit  == "0":
                    break

                n = int(input("Enter convertible units : "))
                result = obj.temp(n,from_unit)
                if result:
                    print(result)
                else:
                    print("Enter celsius/fahrenheit")    

        elif user_choice == 0:
            break                            
        
        else:
            print("*Choose from given options(1-3)*")


    except ValueError as e:
        print("PLease enter valid integral input")                    



