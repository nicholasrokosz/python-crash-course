def make_album(artist, album, no_of_songs=None):
	album_info = {'artist': artist, 'album': album}
	if no_of_songs:
		album_info['no_of_songs'] = no_of_songs
	return album_info

while True:
	artist_name = input("Enter the artist's name: ")
	album_title = input("Enter the album title: ")
	no_of_songs = input("Enter the number of songs (optional): ")

	album_info = make_album(artist_name, album_title, no_of_songs)
	print(album_info)
	
	repeat = input("\nWould you like to enter another album? Enter Y or N: ")
	if repeat == 'Y' or repeat == 'y':
		continue
	else:
		break