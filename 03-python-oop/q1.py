import re
import doctest

def analyze_emails(file_name: str):
    """
    This function gets as input a name of a file text and prints two lists:
    1. A list that contains all the valid emails 
    2. A list that contains all the invalid emails 

    >>> analyze_emails("emails_list.txt")
    valid
     ['abc-d@mail.com', 'abc.def@mail.com', 'abc@mail.com', 'abc_def@mail.com', 'abc.def@mail.cc', 'abc.def@mail-archive.com', 'abc.def@mail.org', 'abc.def@mail.com', 'a-b.a.b@mail.com', 'a@gmail.com']
    invalid
     ['abc-@mail.com', 'abc..def@mail.com', '.abc@mail.com', 'abc#def@mail.com', 'abc.def@mail.c', 'abc.def@mail#archive.com', 'abc.def@mail', 'abc.def@mail..com']
    """

    emails = convert_file_to_list(file_name)
    valid = []
    invalid = []
    pattern = '^[a-z\d]+(([._-]{1}[a-z\d]+)+|([a-z\d]*))@[a-z\d-]+\.[a-z]+[a-z]+'
    for email in emails:
        if (re.search(pattern, email)):
            valid.append(email)
        else:
            invalid.append(email)
    print("valid\n", valid)
    print("invalid\n", invalid)

def convert_file_to_list(file_name: str):
    """this function gets a file name an returns a list that contains the file lines as a list"""
    try:
        with open(file_name, 'r') as file:
            # stores the emails in a list (remove the /n from the end of each string)
            return [email.rstrip() for email in file]
    except:
        pass


def main():
    doctest.testmod()
    # analyze_emails("emails_list.txt")

if __name__ == "__main__":
    main()