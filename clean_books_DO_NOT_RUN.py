
# DO NOT RUN THIS FILE
# There are empty lines at end of books to preserve text if accidentally ran
# I don't want to make it read-only even though I could

book_num = [1,2,3,4,5,6,7]
# delete the front matter
for n in book_num:
    with open("narnia_books_cleaned/book_%s.txt" % n, 'r+') as file:
        for num, line in enumerate(file, 1):
            if "CHAPTER I\n" in line or "Chapter I\n" in line:
                lines = file.readlines()
                file.seek(0)
                file.truncate()
                file.writelines(lines[0:])
# delete the last line
for n in book_num:
    with open("narnia_books_cleaned/book_%s.txt" % n, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        file.writelines(lines[:-1])

