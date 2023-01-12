from datetime import datetime

if __name__ == '__main__':
    """
    used for formatting
    Put the f before the first quote.
    """
    name = "Mike"
    age = 33
    print(f"{name} is {age} now") # Mike is 33 now

    today = datetime.today()
    # I don't understand the %B, %d and %y formats yet, even though it's clear they are for month, day and year.
    print(f"today date is {today:%B %d, %Y}") # today date is January 08, 2023