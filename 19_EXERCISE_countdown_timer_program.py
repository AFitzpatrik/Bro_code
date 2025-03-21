#time.sleep(3) #Program na čas zadaný usne
import time



'''
my_time = int(input("Zadejte čas v sekundách: "))
for x in range(0, my_time): 
#my_time = 3, takže cyklus se provede od 0 - 3 takže 3x. Po každém provedení loopu se přičte 1 sekunda time.sleep(1), takže dohromady 3 sekundy.
#x je v tomto případě COUNTER, POČÍTADLO
    print(x)
    time.sleep(1)

print("ČAS VYPRŠEL!")
'''


my_time = int(input("Zadejte čas v sekundách: "))
for x in range(my_time, 0, -1):  #ALTERNATIVNÍ ZÁPIS - in reversed(range(0, my_time)), STEP (ZAČATEK - KONEC - STEP)
    minutes = int(x / 60) % 60
    seconds = x % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("ČAS VYPRŠEL!")