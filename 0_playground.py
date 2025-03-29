def get_phone(country_code, area_code, firstd, lastd):
  return f"{country_code}-{area_code}-{firstd}-{lastd}"

phone_num = get_phone(country_code=1, area_code=123, firstd=456, lastd=7890)
print(phone_num)