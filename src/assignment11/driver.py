import util

if __name__ == "__main__":
    emails = [
        "pritirai326@gmail.com",
        "my.corgi@our-edu.org",
        "ankit326.com"
    ]

    # Loop over each email and check if it's valid
    for email in emails:
        if util.check(email):
            print(f"'{email}' is a Valid Email")
        else:
            print(f"'{email}' is an Invalid Email")
