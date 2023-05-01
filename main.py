import smtplib

session = smtplib.SMTP("smtp.gmail.com", 587)
session.starttls()


def establish_connection(user, passwd):
    is_success = None
    try:
        is_success = session.login(user, passwd)
        print('Authentication successful!')
    except Exception as error:
        print("login failed due to error:", error)
    finally:
        return is_success


def get_user_and_passwd():
    user = input("Enter your email address : ")
    passwd = input("Enter your password : ")
    return user, passwd


def get_recipient_address_subject_and_text():
    recipient = input("Enter recipient's email address : ")
    subject = input("Enter email subject : ")
    text = input("Enter your message : ")
    return recipient, subject, text


def send_mail():
    success = None
    counter = 3
    while not success and counter != 0:
        user, passwd = get_user_and_passwd()
        print("trying to authenticate... ")
        success = establish_connection(user, passwd)
        if not success:
            counter -= 1
            print(f"You have {counter} attempts left")
        else:
            recipient, subject, text = get_recipient_address_subject_and_text()
            message = f'Subject: {subject}\n\n{text}'
            session.sendmail(user, recipient, message)
            session.quit()
            print('Message sent :)')


send_mail()
