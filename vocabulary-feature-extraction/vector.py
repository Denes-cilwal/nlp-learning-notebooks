vocabulary = ["I", "am", "happy", "because", "learning", "NLP", "is", "fun"]
tweet = "I am happy because I am learning NLP".split()

print("Vocabulary:", type(vocabulary))
print("Vocabulary:", vocabulary)
print("Tweet:", tweet)
print(type(tweet))

vector = []
for word in vocabulary:
    if word in tweet:
        vector.append(1)
    else:
        vector.append(0)

print(vector)
