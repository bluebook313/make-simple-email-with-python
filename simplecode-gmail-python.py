import smtplib
user='4a2mum8p@gmail.com'
password='nwfaikxdrfeabhuj'
destenation = '4a2mum8p1@gmail.com'

def SenEmai(user, password, destenation, ):
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        print('Connection was successful!!!')

    except:
        print('An Can not to connect to the EmailServer ')

    try:
        server.starttls()
        print('Star tls protocol !')

    except:
        print('Can not to star tls protocol !')

    try:
        server.login(user=user,password=password)
        print('login was successful')
    except:
        print('Loggin fail')
        print('check your username and password')

    try:
        server.sendmail(user,destenation,'mail send from python')
    except:
        print('Can not send emai')


    print('mail sent')
    print('check the spam folder')

SenEmai(user,password,destenation)

