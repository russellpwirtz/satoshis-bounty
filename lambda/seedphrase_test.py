import seedphrase

seedphrase = seedphrase.generate_seedphrase(seedphrase.get_word_list())
assert(len(seedphrase) == 12)

wordlist = " ". join(seedphrase)
print(str(wordlist))
