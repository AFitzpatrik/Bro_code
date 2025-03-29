#KEYWORD ARGUMENTS = an arguemnt preceded by and identifier
#                       helps with readability
#                       order of arguments doesnt matter
#                       1. positional 2. default 3.KEYWORD 4.arbitrary


'''
def hello(greeting, title, first, last):
    print(f" {greeting}, {title}. {first} {last}")


hello("Hello",title= "Mr", last = "Squarepants",first = "Spongebob", )
'''

"""
for x in range(1, 11):
    print(x, end = " ")             #end je keyword argument, místo toho, aby se ukončil řádek zadáváme keyword argument end =
"""


'''
print("1", "2", "3", sep = "-")  #sep keyword argument
'''


'''
def get_phone(country_code, area_code, firstd, lastd):
  return f"{country_code}-{area_code}-{firstd}-{lastd}"

phone_num = get_phone(country_code=1, area_code=123, firstd=456, lastd=7890)
print(phone_num)
'''