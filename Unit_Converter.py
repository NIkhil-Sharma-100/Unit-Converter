# Class contain all functions 
class Unit_Conv:
    def length(self,n,order):
        if order == "meter":
            return f"{n} km = {n*1000} m"
        elif order == "kilometer":
            return f"{n} m = {n/1000} km"
        else:
            print("Please Enter Valid Input")

    def weight(self,n,order):
        if order == "gram":
            return f"{n} kg = {n*1000} g"
        elif order == "kilometer":
            return f"{n} kg = {n/1000} g"
        else:
            print("Please Enter Valid Input")  

    def temp(self,n,order):
        if order == "farenheit":
            return f"{n} C = {(n*9/5)+32} F"
        elif order == "celsius":
            return f"{n} F = {(n-32)*5/9} C"


obj = Unit_Conv()                  
            
# Task menu
print("choose number which one do you want")
print("1. Length    2. Weight   3.Temperature     0. Exit")    

while True:
    # Error handling
    try :       
        user_choice = int(input("\nYour choice : "))
        

        if user_choice == 1:
            while True:
                order = input("In (meter/kilometer) or 0 to exit: ").strip().lower()
                
                
                if order  == "0":
                    break

                n = int(input("Enter convertable units : "))
                result = obj.length(n,order)
                if result:
                    print(result)
                else:    
                    print("Enter meter/kilometer")            

        elif user_choice == 2:
            while True:
                order = input("In (gram/kilogram) or 0 to exit: ").strip().lower()
                    

                if order  == "0":
                    break

                n = int(input("Enter convertable units : "))
                result = obj.length(n,order)
                if result:
                    print(result)
                else:
                    print("Enter gram/kilogram") 

        elif user_choice == 3:
            while True:
                order = input("In (celsius/fehrenheit) or 0 to exit : ").strip().lower()


                if order  == "0":
                    break

                n = int(input("Enter convertable units : "))
                result = obj.length(n,order)
                if result:
                    print(result)
                else:
                    print("Enter celsius/fehrenheit")    

        elif user_choice == 0:
            break                            
        
        else:
            print("*Choose from given options(1-3)*")


    except ValueError as e:
        print("PLease enter valid integral input")                    










