import os
selected_library_array = []
score_of_books = []
score = 0
signup = 0
books_scanned = []
no_of_days = -1


class Library:
    def __init__(self, id, nobooks, signup_days, shipping, list_of_books, active_days=0):
        self.id = id
        self.nobooks = nobooks
        self.shipping = shipping
        self.signup_days = signup_days
        self.list_of_books = list_of_books
        self.active_days = active_days
        self.books_processed = []
        self.books_shipped = nobooks
        for i in range(0, self.nobooks):
            for j in range(i+1, self.nobooks):
                if(score_of_books[self.list_of_books[i]] < score_of_books[self.list_of_books[j]]):
                    temp = self.list_of_books[i]
                    self.list_of_books[i] = self.list_of_books[j]
                    self.list_of_books[j] = temp

    def __str__(self):
        return str(self.id)+" "+str(self.books_shipped)+"\n"+str(self.books_processed)


def solve(filename):

    global signup
    global no_of_days
    global books_scanned
    global selected_library_array
    global score_of_books
    global score
    selected_library_array = []
    score_of_books = []
    score = 0
    signup = 0
    books_scanned = []
    no_of_days = -1
    libraryArray = []

    # input
    fp = open(filename, 'r')
    no_of_books, no_libraries, no_of_day_for_scanning = list(
        map(int, fp.readline().strip().split()))
    # second line input
    no_of_days = no_of_day_for_scanning
    score_of_books = list(map(int, fp.readline().strip().split()))
    for i in range(no_libraries):
        no_of_books_in_curr_library, no_of_day_to_signup, no_of_books_shipped = list(
            map(int, fp.readline().strip().split()))
        books_in_curr_library = list(map(int, fp.readline().strip().split()))
        libraryArray.append(Library(i, no_of_books_in_curr_library,
                                    no_of_day_to_signup, no_of_books_shipped, books_in_curr_library))

    # solve
    libraryArray.sort(key=lambda x: x.signup_days)
    for library in libraryArray:
        library.active_days = no_of_days - signup
        library.active_days = library.active_days - library.signup_days
        signup += library.signup_days
        if(signup >= no_of_days):
            break
        if(library.books_shipped > library.active_days*library.shipping):
            library.books_shipped = library.active_days*library.shipping
        # print("id "+str(library.id)+"no of books shipped " +
        #       str(library.books_shipped))
        index = 0
        for i in range(0, library.books_shipped):
            while library.list_of_books[index] in books_scanned:
                if(index < library.nobooks):
                    index += 1
            library.books_processed.append(library.list_of_books[index])
            index += 1

        selected_library_array.append(library)
        # for day in range(0,library.active_days):
        #     book =  library.list_of_books[day]
        #     if book not in books_scanned:
        #         books_scanned.append(book)
        # print(library.list_of_books)


if __name__ == '__main__':
    file_names = list()
    for root, dirs, files in os.walk(os.curdir):
        for file in files:
            if file.endswith(".txt"):
                file_names.append(os.path.join(root, file))
    for file_name in file_names:
        solve(file_name)
        output_file = open(file_name[:-4] + 'output.txt', 'w')
        output_file.write(str(len(selected_library_array))+"\n")
        for library in selected_library_array:
            output_file.write(str(library.id)+" " +
                              str(library.books_shipped)+"\n")
            for book in library.books_processed:
                output_file.write(str(book) + ' ')

            output_file.write('\n')
