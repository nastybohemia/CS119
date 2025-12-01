# Letters to Digits Telephone Number Translator
# Author: Sofia Popova
# LACC CS119

# Enter a 10-character telephone number

# Telephone Number Translator + Formatter + Name
# User enters letters or digits and the contct name

def get_input():
    name = input("Enter a Contact Name: ")

    while True:
        phone = input("Enter a 10-character phone number: ")
        cleaned = phone.replace("-", "").strip() #remove dashes if any exist

        #check that the phonr number is 10-characters
        if len(cleaned) == 10:
            return name, cleaned
        else:
            print("Error: Not a 10-Character Phone Number!\n")


def translate_and_format(cleaned):

    # Mapping of letters to numbers
    mapping = {
        "A":"2", "B":"2", "C":"2",
        "D":"3", "E":"3", "F":"3",
        "G":"4", "H":"4", "I":"4",
        "J":"5", "K":"5", "L":"5",
        "M":"6", "N":"6", "O":"6",
        "P":"7", "Q":"7", "R":"7", "S":"7",
        "T":"8", "U":"8", "V":"8",
        "W":"9", "X":"9", "Y":"9", "Z":"9"
    }

    translated = ""
    for ch in cleaned.upper():
        if ch.isalpha():
            translated += mapping[ch]
        else:
            translated += ch

    # Format to XXX-XXX-XXXX
    formatted = translated[:3] + "-" + translated[3:6] + "-" + translated[6:]
    return formatted


def display(name, formatted_number):
    print("\n------ CONTACT SAVED ------")
    print(f"{name}: {formatted_number}")
    print("---------------------------\n")


def main():
    name, phone = get_input()
    formatted = translate_and_format(phone)
    display(name, formatted)


# Run the program
main()


# Terminal Output
"""
CS119 python3 phoneTranslator.py
Enter a Contact Name: Chris
Enter a 10-character phone number): 555-GET-FOOD

------ CONTACT SAVED ------
Chris: 555-438-3663
---------------------------

➜  CS119 python3 phoneTranslator.py
Enter a Contact Name: 6478YWCA478
Enter a 10-character phone number): 6478YWCA478
Error: Not a 10-Character Phone Number!

Enter a 10-character phone number): 6478YWCA47 

------ CONTACT SAVED ------
6478YWCA478: 647-899-2247
---------------------------

➜  CS119 python3 phoneTranslator.py
Enter a Contact Name: Liza
Enter a 10-character phone number: 376TOTLACC

------ CONTACT SAVED ------
Liza: 376-868-5222
---------------------------

➜  CS119 python3 phoneTranslator.py
Enter a Contact Name: KC
Enter a 10-character phone number: 674-GODODGE

------ CONTACT SAVED ------
KC: 674-463-6343
---------------------------

"""
