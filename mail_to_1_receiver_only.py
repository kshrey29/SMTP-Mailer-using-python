import smtplib

#initiates SMTP session
server=smtplib.SMTP('smtp.gmail.com',587)

#start TLS for security
server.starttls()

# Now log in to the server
server.login('sender@example.com','password')

#message you want to send
msg='Hello!'

#sending the email
server.sendmail('sender@example.com','receiver@example.com',msg)

#terminating the session
server.quit()