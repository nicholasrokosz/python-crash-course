hearts = []

for number in range(1,11):
	hearts.append(f'\u2665{number}\u2665')

face_hearts = ['Jack', 'Queen',
		'King', 'Ace']
for face_heart in face_hearts:
	hearts.append(f'\u2665{face_heart}\u2665')

for heart in hearts:
	print(heart)
	
print(hearts[:10])
print(hearts[10:])