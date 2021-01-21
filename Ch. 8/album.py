def make_album(artist, album, no_of_songs=None):
	album_info = {'artist': artist, 'album': album}
	if no_of_songs:
		album_info['no_of_songs'] = no_of_songs
	return album_info

dsotm = make_album('pink floyd', 'dark side of the moon')
print(dsotm)

traveller = make_album('chris stapleton', 'traveller', 14)
print(traveller)