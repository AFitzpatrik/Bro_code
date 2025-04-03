#Python quiz game

questions = (
    "How many elements are in the periodic table?: ",
    "Which animal lays the largest eggs?: ",
    "What is the most abundant gas in Earth's atmosphere?: ",
    "How many bones are in the human body?: ",
    "Which planet in the solar system is the hottest?: "
)

options = options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars")
)

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0 #Tato proměnná zjištuje v jaké otázce zrovna jsme, začínáme na indexu 0


for question in questions:
    print("--------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter A, B, C, D: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1 # score = score + 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num = question_num + 1 # question_num = question_num + 1

print ("----------------------")
print ("--------RESULTS-------")
print ("----------------------")



print("Answers", end=" ")
for answer in answers:
    print(answer,end=" ")
print()

print("Guesses", end= " ")
for guess in guesses:
    print(guess, end=" ")
print()


score = int(score / len(questions) *100)
print(f"Your score is {score}%")




#Druhý pokus
#Python quiz game

'''
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

    for moznost in moznosti[question_num]: #moznosti [question_num] vybírá konkrétní tuple z moznosti na základě aktuální hodnoty question_num.
#např Pokud question_num je 0, možnosti [question_num] je ("A. BERLIN, B. PARIS, C. MADRID. D ROME)

        print(moznost)

    guess = input("Choose your option: A, B, C, D ").upper()
    pokusy.append(guess)

    if guess == odpovedi[question_num]:
        score += 1
        print("Correct!")
    else:

        print("Inccorect!")
        print(f"Correct answer is {odpovedi[question_num]}.") #[question_num] je index, dává to index a zvyšeuje se po každem ckylu
    question_num += 1

print("RESULTS")

print(f"Guesses: {pokusy}")
print(f"Correct: {odpovedi}")
print(f"Body: {score}")
'''
