def city_country(city, country):
	name = f'"{city}, {country}"'
	return name.title()

city_1 = city_country('santiago', 'chile')
print(city_1)

city_2 = city_country('oslo', 'norway')
print(city_2)

city_3 = city_country('dublin', 'ireland')
print(city_3)