book_list = []
authors_set = set()
books_dict = {}
book_list.append("python programming")
authors_set.add("jhon smith")
books_dict["python programming"] = "jhon smith"

book_list.append("data structures and algorithems")
authors_set.add("jane doe")
books_dict["data structures and algorithems"] = "jane doe"

book_list.append("machine learning basics")
authors_set.add("alice johnson")
books_dict["machine learning basics"] = "alice johnson"

search_title =input("Enter name of book your searching:")
if search_title in book_list:
    print(f"book found:{books_dict[search_title]}")

else :
    print("book not found!")

print("list of books :")
for book in book_list:
    print(book)

remove_title = input("enter name to remove or skip:")
if remove_title in book_list:
    remove_author = books_dict[remove_title]
    book_list.remove(remove_title)
    authors_set.remove(remove_author)
    del books_dict[remove_title]
    print("book removed successful")
    print("book aviable:", book_list)
else :
    print("book not found!")
