guests = ['Bertrand Russell', 'Elon Musk', 'Claude Shannon']

print(f"Dear Mr. {guests[0]}, are you available to attend a dinner at my home this weekend?")
print(f"Dear Mr. {guests[1]}, are you available to attend a dinner at my home this weekend?")
print(f"Dear Mr. {guests[2]}, are you available to attend a dinner at my home this weekend?")
print("\nIt Seems we've found a bigger table.")

guests.insert(0, 'Alan Turing')
guests.insert(3, 'Richard Hamming')
guests.append('Lex Fridman')

print(f"Dear Mr. {guests[0]}, are you available to attend a dinner at my home this weekend?")
print(f"Dear Mr. {guests[1]}, are you available to attend a dinner at my home this weekend?")
print(f"Dear Mr. {guests[2]}, are you available to attend a dinner at my home this weekend?")
print(f"Dear Mr. {guests[3]}, are you available to attend a dinner at my home this weekend?")
print(f"Dear Mr. {guests[4]}, are you available to attend a dinner at my home this weekend?")
print(f"Dear Mr. {guests[5]}, are you available to attend a dinner at my home this weekend?")

print("\nUnfortunately, we can only host two guests.")

not_guest = guests.pop()
print(f"Sorry {not_guest}, I hope to meet you another time.")

not_guest = guests.pop()
print(f"Sorry {not_guest}, I hope to meet you another time.")

not_guest = guests.pop()
print(f"Sorry {not_guest}, I hope to meet you another time.")

not_guest = guests.pop()
print(f"Sorry {not_guest}, I hope to meet you another time.")

print(f"Dear {guests[0]}, I'm looking forward to meeting you.")
print(f"Dear {guests[1]}, I'm looking forward to meeting you.")

del guests[0]
del guests[0]

print(guests)