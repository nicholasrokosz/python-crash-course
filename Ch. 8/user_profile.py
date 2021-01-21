def build_profile(first, last, **user_info):
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

my_profile = build_profile('nick', 'rokosz', age=27,
	city='phoenix', fav_lang='python')

print(my_profile)