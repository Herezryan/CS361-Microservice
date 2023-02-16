import string, email_micro

while True:
    file = open('sendmail.txt', 'r')
    word = file.readline()
    try:
        if word == 'yes':
            email_micro.start_serv()
            print('Email sent')
            break
    except:
        print('Waiting to send email')
    file.close()
