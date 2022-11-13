def analyze_emails(file_name: str):
    emails = convert_file_to_list(file_name)

def convert_file_to_list(file_name: str):
    try:
        with open(file_name, 'r') as file:
            # stores the emails in a list
            return [email.rstrip() for email in file]
    except:
        pass


def main():
    file_name = "emails_list.txt"
    analyze_emails(file_name)

if __name__ == "__main__":
    main()