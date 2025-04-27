#Decorator = A function  that extends the behavior of another function
#            w/o modifying the base function
#            Pass the base function as an argument to the decorator

#            @add_sprinkles
#            get_ice_cream("vanilla")

def add_sprinkles(func):
    def wrapper():
        print("Adding sprinkles!")
        func()
    return wrapper

def add_fudge(func):
    def wrapper():
        print("Adding fudge!")
        func()
    return wrapper

@add_fudge
@add_sprinkles #extends the behavior of get_ice_cream
def get_ice_cream():
    print("Here is your ice cream!")


get_ice_cream()
