# Count frequency of each word in a sentence

sentence = input("Enter a sentence: ")
words = sentence.split()

freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

output = []
for word in freq:
    output.append(word + ": " + str(freq[word]))

print(", ".join(output))
