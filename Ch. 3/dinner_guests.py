guests = ['Bertrand Russell', 'Elon Musk', 'Claude Shannon']

print(f"Dear Mr. {guests[0]}, are you available to attend a dinner at my home this weekend?")
print(f"Dear Mr. {guests[1]}, are you available to attend a dinner at my home this weekend?")
print(f"Dear Mr. {guests[2]}, are you available to attend a dinner at my home this weekend?")

popped_guest = guests.pop(1)
new_guests = guests.append('Lex Fridman')

print(f"Unfortunately, it seems that Mr. {popped_guest} will not be able to attend. We are happy to announce that Mr. {guests[-1]} will be attending.")

print(f"Dear Mr. {guests[0]}, are you available to attend a dinner at my home this weekend?")
print(f"Dear Mr. {guests[1]}, are you available to attend a dinner at my home this weekend?")
print(f"Dear Mr. {guests[2]}, are you available to attend a dinner at my home this weekend?")

print(f"There will be {len(guests)} guests attending the dinner.")