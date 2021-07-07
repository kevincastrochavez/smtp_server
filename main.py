import smtplib

MY_EMAIL = 'pythonjohndoe@gmail.com'
MY_PASSWORD = 'pythondoe'

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL, 
        to_addrs='kevincastrochavez4@gmail.com', 
        msg='Subject:Hello\n\nThis is the body of my email')
    connection.close()