# variable scope = where a vriable is visible and accessible
# scope resolution = (LEGB) local -> Enclosed -> Global -> Built-in


'''
def func1():
    a = 1           #proměnné ve funci mají LOCAL scope, jedna funkce nevidí do jiných funkcí
    print(a)        #LOCAL scope


def func2():
    b = 2
    print(b)

func1()
func2()
'''


'''
def func1():
    print(x)


def func2():
   print(x)

x = 3   #vytiskne se 2x 3 pro funkci 1 a pro funci 2, x proměnná je global, jen pokud není proměnná localní
func1()
func2()
'''

'''
def func1():  #v tomto příkladu by se vytisklo 1 a 2, protože local mají přednost před global
    x = 1
    print(x)

def func2():
    x = 2
    print(x)
    
x = 3   
func1()
func2()
'''

'''
from math import e

def func1(): #zde se vytiskne 3 protože je zde global proměnná která má přednost před built in
    print(e)
e = 3
func1()
'''
