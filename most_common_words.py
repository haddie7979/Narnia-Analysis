import string
import numpy as np
import matplotlib.pyplot as plt
word_counts = dict()

book_num = [1,2,3,4,5,6,7]

for n in book_num:
    with open("narnia_books_cleaned/book_%s.txt" % n, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            line = line.lower()
            line = line.translate(line.maketrans("", "", string.punctuation))
            words = line.split(" ")
            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

word_counts = dict(sorted(word_counts.items(), key=lambda elem:elem[1], reverse=True)[:20])
plt.barh(list(word_counts.keys()), word_counts.values())
ax = plt.gca()
ax.invert_yaxis()
# plt.yticks([])
plt.xlabel("frequency")
plt.ylabel("words")
plt.title("Frequency of Most Common Words")
plt.show()


# Sources
# https://www.geeksforgeeks.org/python-n-largest-values-in-dictionary/