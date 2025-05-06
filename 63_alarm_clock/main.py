# Python Alarm Clock
import time
import datetime
import pygame

def set_alarm(alarm_time): #Funkce přijímá jeden argument, alarm_time což je čas, který uživatel zadá v inputu
    print(f"Alarm set for {alarm_time}!")
    sound_file = "my_music.mp3"  # Cesta na soubor ve složce
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")  # Získání aktuálního času ve formátu HH:MM:SS
        print(current_time)

        if current_time == alarm_time:
            print("Alarm ringing!🔔")

            is_running = False

        time.sleep(1)










if __name__ == "__main__":
    alarm_time = input("Enter the alarm time in 24 hour format (HH:MM:SS): ")
    set_alarm(alarm_time)


