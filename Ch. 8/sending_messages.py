def send_messages(texts, sent_texts):
	while texts:
		texting = texts.pop()
		print(f"\n{texting}")
		sent_texts.append(texting)

txts = ['lol', 'hey', 'how are you?', 'ttyl']

sent_messages = []

send_messages(txts, sent_messages)
print(txts)
print(sent_messages)