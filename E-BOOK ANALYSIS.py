import requests
from bs4 import BeautifulSoup
import operator


# WRITING CONTENT TO THE TEXT FILE
def writing_file(content, book):
    file = open(book+".txt", "w", encoding="utf-8")
    file.write(content)
    file.close()


# READING CONTENT TO THE TEXT FILE
def reading_file(book_name):
    book = open(book_name+".txt", "r", encoding="utf-8")
    content = book.read()
    book.close()
    return content


# REGULATES THE WORDS AND RETURNS SIMPLEST FORM OF WORDS
def regulation(all_words):
    simple_words = []
    non_punctuation = []
    non_numbers = []
    punctuations = "∀æß~¨´`!'^+%&/()=?_-*|{}][{½$#£\"><@.⋅,;’:\\" + chr(775)
    numbers = "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
    stop_words = ["←", "name", "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
     "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
     "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
     "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
     "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as",
     "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through",
     "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off",
     "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how",
     "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not",
     "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should",
     "now", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
     'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', '⋅', '∀']

    # DELETING ALL PUNCTUATIONS
    for punctuation in punctuations:
        if punctuation in all_words:
            all_words = all_words.replace(punctuation, " ")
            non_punctuation = all_words.split()

    # DELETING ALL NUMBERS
    for word in non_punctuation:
        for number in numbers:
            if number in word:
                word = word.replace(number, "")
        if len(word) > 0:
            non_numbers.append(word)

    # DELETING ALL STOPWORDS
    for word in non_numbers:
        for stop_word in stop_words:
            if word in stop_word:
                word = word.replace(stop_word, "")
        if len(word) > 0:
            simple_words.append(word)
    return simple_words


# COUNTING WORD FREQUENCIES , REVERSE THEM IN THE DICTIONARY AND RETURN THE LIST FORM
def freq_dictionary(simple_words):
    word_frequency = {}

    for word in simple_words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    sorted_frequency_1 = sorted(word_frequency.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_frequency_1


def main():
    link2 = ""
    book2 = ""
    sorted_frequency_2 = []

    # ASKING TO USER THAT HOW MANY BOOKS DOES HE\SHE WANTS TO EXAMINE
    book_number = int(input("How many books do you want to examine (1 or 2) : "))
    link_type = input("Which one do you prefer Wikibooks or Wikisource : ")

    # ASKING TO USER WHETHER HE\SHE WANTS TO ENTER FREQUENCY OR NOT
    answer = input("Do you want to enter a word frequency you wish to see ?(DEFAULT: 20) (Y or N) : ")

    if answer == 'Y' or answer == 'y':
        frequency = int(input("How many word frequency you wish to see : "))
    else:
        frequency = 20

    # IF USER WANTS TO EXAMINE ONE BOOK
    if book_number == 1:
        # GETTING THE BOOK NAME AND CREATING LINK VARIABLE
        book1 = input("Please enter the book name : ")

        if "'" in book1:
            book1 = book1.replace("'", "%27")

        # ASKING SOURCE WHICH DOWNLOAD THE BOOK
        if link_type == "Wikibooks" or "wikibooks":
            link1 = ("https://en.wikibooks.org/wiki/" + book1)

            # GETTING LINK OF PRINT VERSION OF BOOK FOR PREVENT SOME ERRORS
            request = requests.get(link1)
            soup = BeautifulSoup(request.content, "html.parser")
            path = soup.find_all("td", {
                "style": "color:black; text-align:left; vertical-align:middle; padding:0.5em; padding-left:0em; border:none;"})

            for link in path:
                links = link.find("a")
                p = links.get_text()
                if p == "printable version":
                    link_version = links.get("href")
                    link1 = ("https://en.wikibooks.org" + link_version)
                    break

        else:
            link1 = ("https://en.wikisource.org/wiki/" + book1)
        # SOME CORRECTIONS
        book1 = book1.replace("/", " ")
        book1 = book1.replace("%27", "'")
        book1 = book1.replace("\"", " ")

    # IF USER WANTS TO EXAMINE TWO BOOKS
    else:
        # GETTING BOOK NAMES AND CREATING LINK VARIABLES
        # BOOK1
        book1 = input("Please enter the first book's name : ")

        if "'" in book1:
            book1 = book1.replace("'", "%27")

        if link_type == "Wikibooks" or "wikibooks":
            link1 = ("https://en.wikibooks.org/wiki/" + book1)

            # GETTING LINK OF PRINT VERSION OF BOOK FOR PREVENT SOME ERRORS
            request = requests.get(link1)
            soup = BeautifulSoup(request.content, "html.parser")
            path = soup.find_all("td", {
                "style": "color:black; text-align:left; vertical-align:middle; padding:0.5em; padding-left:0em; border:none;"})

            for link in path:
                links = link.find("a")
                p = links.get_text()
                if p == "printable version":
                    link_version = links.get("href")
                    link1 = ("https://en.wikibooks.org" + link_version)
                    break

        else:
            link1 = ("https://en.wikisource.org/wiki/" + book1)

        # SOME CORRECTIONS
        book1 = book1.replace("/", " ")
        book1 = book1.replace("%27", "'")
        book1 = book1.replace("\"", " ")

        # BOOK2
        book2 = input("Please enter the second book's name : ")

        if "'" in book2:
            book2 = book2.replace("'", "%27")

        if link_type == "Wikibooks" or "wikibooks":
            link2 = ("https://en.wikibooks.org/wiki/" + book2)

            # GETTING LINK OF PRINT VERSION OF BOOK FOR PREVENT SOME ERRORS
            request = requests.get(link2)
            soup = BeautifulSoup(request.content, "html.parser")
            path = soup.find_all("td", {
                "style": "color:black; text-align:left; vertical-align:middle; padding:0.5em; padding-left:0em; border:none;"})

            for link in path:
                links = link.find("a")
                p = links.get_text()
                if p == "printable version":
                    link_version = links.get("href")
                    link2 = ("https://en.wikibooks.org" + link_version)
                    break

        else:
            link2 = ("https://en.wikisource.org/wiki/" + book2)

        # SOME CORRECTIONS
        book2 = book2.replace("/", " ")
        book2 = book2.replace("%27", "'")
        book2 = book2.replace("\"", " ")

    # GETTING DATA FROM THE LINK BY USING SOME MODULES
    data1 = requests.get(link1)
    beautiful_data1 = BeautifulSoup(data1.content, "html.parser")

    # GET DATA TO TEXT CONTENT
    content1 = beautiful_data1.find("body")
    content1 = content1.text

    # CALLING TO WRITE_FILE FOR WRITE CONTENT TO THE TEXT FILE
    writing_file(content1, book1)

    # CALLING TO READ FUNCTION FOR READING BOOK FROM THE TEXT FILE
    read1 = reading_file(book1)

    # CALLING REGULATION FUNCTION AND SETTING THE APPROPRIATE FORM OF WORDS
    all_words1 = read1.lower()
    simple_words1 = regulation(all_words1)

    # CALLING FREQ_DICTIONARY FUNCTION AND PRINT FREQUENCY OF WORDS
    sorted_frequency_1 = freq_dictionary(simple_words1)

    # IF THERE ARE 2 BOOKS DO THE SAME PROCESSES TO SECOND BOOK
    if book_number == 2:
        data2 = requests.get(link2)
        beautiful_data2 = BeautifulSoup(data2.content, "html.parser")
        content2 = beautiful_data2.find("body")
        content2 = content2.text
        writing_file(content2, book2)
        read2 = reading_file(book2)
        all_words2 = read2.lower()
        simple_words2 = regulation(all_words2)
        sorted_frequency_2 = freq_dictionary(simple_words2)

    counter = 1
    # FOR ONE BOOK
    if book_number == 1:
        print()
        print("BOOK 1 : ", book1, "\nCOMMON WORDS")
        print(f"NO   WORD        FREQ_1")
        # FINDING FREQUENCIES OF WORD\WORDS AND SHOW THEM TO THE SCREEN
        for i, j in sorted_frequency_1:
            print(f"{counter:<3}  {i:<12}{j:<5}")
            counter += 1
            # IF COUNTER REACHES FREQUENCY THAT USER WANTS, EXIT THE LOOP
            if counter == frequency + 1:
                break

    # FOR TWO BOOKS
    if book_number == 2:
        # FINDING SUM OF FREQUENCIES OF WORD\WORDS
        freq_sum = {}
        for i, j in sorted_frequency_1:
            for k, l in sorted_frequency_2:
                if i == k:
                    # CREATING DICTIONARY ABOUT SUM OF FREQUENCIES
                    freq_sum[i] = j+l

        # SORT ITEMS AND CHANGE THE VARIABLE TYPE DICTIONARY TO LIST
        freq_sum_list = sorted(freq_sum.items(), key=operator.itemgetter(1), reverse=True)

        # PRINT THE WORDS AND FREQUENCIES TO THE SCREEN
        print()
        print("BOOK 1 : ", book1, "\nBOOK 2 : ", book2, "\nCOMMON WORDS")
        print(f"NO   WORD        FREQ_1  FREQ_2   FREQ_SUM")
        for m, n in freq_sum_list:
            for i, j in sorted_frequency_1:
                for k, l in sorted_frequency_2:
                    # PRINTING THE WORD THAT THE MOST REPEATED
                    if i == k and i == m:
                        print(f"{counter:<3}  {i:<12}{j:<5}   {l:<5}    {n:<5}")
                        counter += 1
            # IF COUNTER REACHES FREQUENCY THAT USER WANTS, EXIT THE LOOP
            if counter == frequency+1:
                break

        print()
        # FINDING DISTINCT WORDS FREQUENCIES FOR EACH BOOK AND SHOW THEM TO THE SCREEN
        # FOR FIRST BOOK
        counter = 1
        print("BOOK 1 : ", book1, "\nDISTINCT WORDS")
        print(f"NO   WORD            FREQ_1")
        for i, j in sorted_frequency_1:
            distinct_control = 0
            for k, l in sorted_frequency_2:
                if i == k:
                    break
                else:
                    distinct_control += 1
                # IF CONTROL COUNT SAME AS SECOND BOOK'S WORD COUNT, IT MEANS THE WORD IS DISTINCT AND PRINT IT
                if i != k and distinct_control == len(sorted_frequency_2):
                    print(f"{counter:<3}  {i:<12}    {j:<5}")
                    counter += 1
            # IF COUNTER REACHES FREQUENCY THAT USER WANTS, EXIT THE LOOP
            if counter == frequency+1:
                break

        print()
        # FOR SECOND BOOK
        counter = 1
        print("BOOK 2 : ", book2, "\nDISTINCT WORDS")
        print(f"NO   WORD            FREQ_2")
        for i, j in sorted_frequency_2:
            distinct_control = 0
            for k, l in sorted_frequency_1:
                if i == k:
                    break
                else:
                    distinct_control += 1
                # IF CONTROL COUNT SAME AS SECOND BOOK'S WORD COUNT, IT MEANS THE WORD IS DISTINCT AND PRINT IT
                if i != k and distinct_control == len(sorted_frequency_1):
                    print(f"{counter:<3}  {i:<12}    {j:<5}")
                    counter += 1
            # IF COUNTER REACHES FREQUENCY THAT USER WANTS, EXIT THE LOOP
            if counter == frequency + 1:
                break


main()
