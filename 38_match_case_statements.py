# Match-case statement (switch): An alternative to using many 'elif' statements:
#                                Execute some code if a value matches a 'case'
#                                Benefits: cleaner and syntax is more readable
#switches v jiných jazycích

#KLASICKÝ ZÁPIŠ SKRZ IF, ELIF, ELSE
'''
def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _: #WILDCARD
            return "Not a valid day"

print(day_of_week(1))
'''
#ZÁPIS IF
'''
def day_of_week(day):
    if day == 1:
        return "It is Sunday"
    elif day == 2:
        return "It is Monday"
    elif day == 3:
        return "It is Tuesday"
    elif day == 4:
        return "It is Wednesday"
    elif day == 5:
        return "It is Thursday"
    elif day == 6:
        return "It is Friday"
    elif day == 7:
        return "It is Saturday"
    else:
        return "Not a valid day"

print(day_of_week(1))
'''

# ZÁPIS SKRZ CASE

def is_weekend(day):
    match day:
        case "Sunday" | "Saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":  # | tato čára znamená OR
            return False
        case _:
            return False

print(is_weekend("Monday"))

