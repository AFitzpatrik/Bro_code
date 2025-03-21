#format specifiers = {VALUE:flags} format a value based on what flags are inserted
#
#. (number)f = round to that many decimal places (fixed point)
#. (number) = allocate that many spaces
#:03 = allocate and zero pad that many spaces
#:< = left justify
#:> = right justify
#:^ = center align
#+ = use a plus sign to indicate positive value
#- = place sign to leftmost position
# (space) = insert a space before positive numbers
#, = comma separator


'''
price1 = 9.514528
price2 = - 97.41255
price3 = 12.34
print(f"Price 1 is {price1:.2f}") #kolik zobratit desetinných čísel
print(f"Price 2 is {price2:.2f}")
print(f"Price 3 is {price3:.2f}")
'''

price1 = 9.514528
price2 = - 97.55
price3 = 12.34
price4 = 3000000.14589
price5 = - 9870.65
price6 = 1200.34

print(f"Price 1 is {price1:10}") #přidá mezery aby byl string 10 míst dlouhý
print(f"Price 2 is {price2:010}") #přidá 0 místo mezery
print(f"Price 3 is {price3:<010}") #přida symbol z prava
print(f"Price 3 is {price3:^010}") #vycentruje číslo
print(f"Price 3 is {price3:+}")  #+ indikuje pozitivní value, přidá před positivní value +
print(f"Price 2 is {price2:+}")
print(f"Price 2 is {price2: }")# (mezera) přidá mezeru před positivní číslo, aby bylo zarovnáno s negativním
print(f"Price 4 is {price4:,}")# , přidá po každém tisíci čárku
print(f"Price 4 is {price4:+,.2f}") #lze specifery kombinovat
