import webbrowser

user_term = input("Please enter the term you would like to search for:")

webbrowser.open(f"https://www.youtube.com/results?search_query={user_term}")