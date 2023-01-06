import pandas as pd
import matplotlib.pyplot as plt

book_num = [1,2,3,4,5,6,7]

# Get the word count in each book, excluding front and back matter
word_count = 0
titles = []
totals = []
for n in book_num:
    with open("narnia_books/book_%s.txt" % n, 'r') as file:
        for line in file:
            # Make a list of the book titles
            if "[Transcriber's note:" in line:
                for line in file:
                    if line != "\n":
                        titles.append(line)
                        break
            # Get the word count in each book
            if "CHAPTER I\n" in line or "Chapter I\n" in line:
                for line in file:
                    if '[End of' in line:
                        break
                    words = line.split()
                    word_count += len(words)
    totals.append(word_count)
    word_count = 0
titles = [label.replace(' ', '\n') for label in titles]
df = pd.DataFrame({' ':titles, 'Word Count': totals})
ax = df.plot.bar(x=' ', y='Word Count',rot=0, title='Word Count By Book', color='Purple')
plt.tight_layout()
plt.show()

