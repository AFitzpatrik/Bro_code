#Python quiz game

otazky = (
    "What is the capital of Germany?",  # Otázka 1
    "How many fingers on humans hand?",  # Otázka 2
    "Kdo honí?",  # Otázka 3
    "Who wrote 'Romeo and Juliet'?",  # Otázka 4
    "Co se učim?"  # Otázka 5
)
moznosti = ( #Možnosti jsou 2D Tuple
    ("A. Berlin", "B. Paris", "C. Madrid", "D. Rome"),  # Možnosti pro otázku 1
    ("A. 16", "B. 5", "C. 4", "D. 16"),  # Možnosti pro otázku 2
    ("A. Zeme", "B. Mars", "C. Jupiter", "D. Saša"),  # Možnosti pro otázku 3
    ("A. Mark Twain", "B. William Shakespeare", "C. Charles Dickens", "D. J.K. Rowling"),  # Možnosti pro otázku 4
    ("A. Indian Ocean", "B. Atlantic Ocean", "C. Python", "D. Pacific Ocean")  # Možnosti pro otázku 5
)
odpovedi = ("A", "B", "D", "B", "C")
pokusy = []
score = 0
question_num = 0 #Tato proměnná zjištuje v jaké otázce zrovna jsme, začínáme na indexu 0

for otazka in otazky:
    print("--------------------------------")
    print(otazka)
    for moznost in moznosti[question_num]:
        print(moznost)