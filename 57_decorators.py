#Decorator = A function  that extends the behavior of another function
#            w/o modifying the base function
#            Pass the base function as an argument to the decorator

#            @add_sprinkles
#            get_ice_cream("vanilla")

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Adding sprinkles!")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("Adding fudge!")
        func(*args, **kwargs)
    return wrapper

@add_fudge
@add_sprinkles #extends the behavior of get_ice_cream
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream!")


get_ice_cream("vanilla")
get_ice_cream("Chocolate")
