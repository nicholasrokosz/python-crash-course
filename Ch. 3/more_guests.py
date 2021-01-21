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