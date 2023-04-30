import smtplib

global user, recipient, subject, text
success = None
counter = 3


def establish_connection(user, passwd):
    is_success = None
    try:
        is_success = session.login(user, passwd)
        print('Authentication successful!')
    except Exception as error:
        print("login failed due to error:", error)
    finally:
        return is_success


def gets_user_and_passwd(counter):
    user = input("Enter your email address : ")
    passwd = input("Enter your password : ")
    print("trying to authenticate... ")
    success = establish_connection(user, passwd)
    if not success:
        counter -= 1
        print(f"You have {counter} attempts left")
    return counter, success, user


def gets_rec_subject_text():
    recipient = input("Enter recipient's email address : ")
    subject = input("Enter email subject : ")
    text = input("Enter your message : ")
    return recipient, subject, text


session = smtplib.SMTP("smtp.gmail.com", 587)
session.starttls()

while not success and counter != 0:
    counter, success, user = gets_user_and_passwd(counter)
    if success:
        recipient, subject, text = gets_rec_subject_text()
        message = f'Subject: {subject}\n\n{text}'
        session.sendmail(user, recipient, message)
        session.quit()
        print('Message sent :)')
    else:
        continue


