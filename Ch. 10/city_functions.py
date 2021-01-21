def format_city(city, country, population = ''):
	"""Neatly formats given city and country names."""

	if population:
		return f"{city.title()}, {country.title()} - population {population}"
	else:
		return f"{city.title()}, {country.title()}"