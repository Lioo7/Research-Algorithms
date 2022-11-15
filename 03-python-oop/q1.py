import re

def analyze_emails(file_name: str):
    emails = convert_file_to_list(file_name)
    pattern = '^[a-z\d]+(([._-]{1}[a-z\d]+)+|([a-z\d]*))@[a-z\d-]+\.[a-z]+[a-z]+'
    for email in emails:
        if (re.search(pattern, email)):
            print("Valid!", email)

def convert_file_to_list(file_name: str):
    try:
        with open(file_name, 'r') as file:
            # stores the emails in a list (remove the /n from the end of each string)
            return [email.rstrip() for email in file]
    except:
        pass


def main():
    file_name = "emails_list.txt"
    analyze_emails(file_name)

if __name__ == "__main__":
    main()