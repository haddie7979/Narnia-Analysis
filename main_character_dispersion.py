from yellowbrick.text import DispersionPlot
from yellowbrick.datasets import load_hobbies
from nltk.corpus.reader.plaintext import PlaintextCorpusReader



book_num = [1,2,3,4,5,6,7]
char_list = ["Lucy", "Edmund", "Aslan", "Tumnus", "Peter", "Susan", "Witch"]
word_list = [[""]]


narnia_corpus = PlaintextCorpusReader('narnia_books', r'.\*.txt')
for n in book_num:
    book_words = narnia_corpus.words('book_%s.txt' % n)
    word_list.append(book_words)

visualizer = DispersionPlot(char_list, title="Dispersion of Main Character Mentions", annotate_docs=True)
visualizer.fit(word_list)
visualizer.show()


# Sources
# https://www.nltk.org/howto/corpus.html#plaintext-corpus-reader
# https://www.scikit-yb.org/en/latest/api/text/dispersion.html#