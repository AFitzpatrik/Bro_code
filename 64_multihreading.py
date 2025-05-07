#Multithreading = Used to perform multiple tasks concurrently (multitasking)
#                 Good for I/O(input,output) bound tasks like reading file or festching data from API
#                 threading.Thread(target=m_function)


import threading
import time

def walk_dog(first, last):
    time.sleep(8)
    print(f"You finish walking the {first} {last} dog")

def take_out_trash():
    time.sleep(2)
    print("You finish taking out the trash")

def get_mail():
    time.sleep(4)
    print("You finish getting the mail")

chore1 = threading.Thread(target=walk_dog, args =("Scooby","Doo"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()


print("all chores are completed")



'''
walk_dog()
take_out_trash()
get_mail()
- Když to udělám takto, na jednom threadu, první se dokončí walking_dog, pak taking out trash a nakonec getting the mail
pokud bych to udělal přes multithreading, tak se první dokončí taking out trash, pak getting the mail a nakonec walking dog
'''

