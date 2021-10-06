# Using f-strings, print out the name, last name,
# and quote of each person in the given dictionary,
# formatted like so:
#
# "The inspiring quote" - Lastname, Firstname

famous_quotes = [
    {"full_name": "Isaac Asimov", "quote": "I do not fear computers. I fear lack of them."},
    {"full_name": "Emo Philips", "quote": "A computer once beat me at chess, but it was no match for me at "
                                          "kick boxing."},
    {"full_name": "Edsger W. Dijkstra", "quote": "Computer Science is no more about computers than astronomy "
                                                 "is about telescopes."},
    {"full_name": "Bill Gates", "quote": "The computer was born to solve problems that did not exist before."},
    {"full_name": "Norman Augustine", "quote": "Software is like entropy: It is difficult to grasp, weighs nothing, "
                                               "and obeys the Second Law of Thermodynamics; i.e., it always increases."},
    {"full_name": "Nathan Myhrvold", "quote": "Software is a gas; it expands to fill its container."},
    {"full_name": "Alan Bennett", "quote": "Standards are always out of date.  That’s what makes them standards."}
]

# Seperates the first name from the last name- incomplete

# Not sure how to do this if there is a middle initial, can i still use split?

# Loop through each dictionary in the list
for dicts in famous_quotes:
    # Loop through each value in full name
    print(famous_quotes.values["full_name"])
    # If it's a letter add it to a new list ?
    # If the value is a space, stop


# Prints the quote and the name
for dicts in famous_quotes:
    print(f"{dicts.get('quote')} - {dicts.get('full_name')}")
    print(i)