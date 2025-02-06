#Write a function that accepts string from user,
# return a sentence with the words reversed.
# We are ready -> ready are We

def reversee(sentence):
    words=sentence.split()
    rev_words=words[::-1]
    return ' '.join(rev_words)
print(reversee("We are ready"))

#output ready are We