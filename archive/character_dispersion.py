from yellowbrick.text import DispersionPlot
from yellowbrick.datasets import load_hobbies

book_num = [1,2,3,4,5,6,7]
char_list = ["Lucy", "Edmund", "Aslan", "Tumnus", "Peter", "Susan"]
word_list = [[""]]
titles = []
for n in book_num:
    with open("narnia_books/book_%s.txt" % n, 'r') as file:
        for line in file:
            # Make a list of the book titles
            if "[Transcriber's note:" in line:
                for line in file:
                    if line != "\n":
                        titles.append(line)
                        break
for t in titles:
    print(t)

for n in book_num:
    with open("narnia_books/book_%s.txt" % n, 'r') as file:
        for line in file: 
            if "CHAPTER I\n" in line or "Chapter I\n" in line:
                for line in file:
                    if '[End of' in line:
                        break
                    words = line.split()
                    word_list.append(words)
visualizer = DispersionPlot(char_list, title="Dispersion of Main Character Mentions")
visualizer.fit(word_list)
visualizer.show()

