
class Unit_Conv:
    def length(self,n):
        if order == "meter":
            return f"{n} km = {n*1000} m"
        elif order == "kilometer":
            return f"{n} m = {n/1000} km"
        else:
            print("Please Enter Valid Input")

    def weight(self,n):
        if order == "gram":
            return f"{n} kg = {n*1000} g"
        elif order == "kilometer":
            return f"{n} kg = {n/1000} g"
        else:
            print("Please Enter Valid Input")  

obj = Unit_Conv()                  
            

print("choose number which one do you want")
print("1. Length        2. Weight")    

while True:        
    user_choice = int(input("Your choice : "))
    

    if user_choice == 1:
        while True:
            order = input("In (meter/kilometer) : ").lower()
            if order in ["meter","kilometer"]:
                n = int(input("Enter convertable units : "))
                print(obj.length(n))
            else:    
                print("Enter meter/kilometer")            


    elif user_choice == 2:
        while True:
            order = input("In (gram/kilogram) : ").lower()
                
            if order in ["gram","kilogram"]:
                n = int(input("Enter convertable units  : "))
                print(obj.weight(n))   

            else:
                print("Enter gram/kilogram")  

    else:
        print("Choose 1/2")                  
                        






