import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = "pooja.ravi@imanage.com"         # Replace with yours
MY_PASSWORD = "Radheradhe@95"      # Replace with yours
RECIPIENT_ADDRESS = "pooja.ravi@imanage.com"  # Replace with yours
HOST_ADDRESS = 'smtp-mail.outlook.com'   # Replace with yours
HOST_PORT = 587
# Connection with the server
server = smtplib.SMTP(host=HOST_ADDRESS, port=HOST_PORT)
server.starttls()
server.login(MY_ADDRESS, MY_PASSWORD)

# Creation of the MIMEMultipart Object
message = MIMEMultipart()

# Setup of MIMEMultipart Object Header
message['From'] = MY_ADDRESS
message['To'] = RECIPIENT_ADDRESS
message['Subject'] = "Automated Email3"

# Creation of a MIMEText Part
textPart = MIMEText("This is my first plain text automated email\n\n Thanks\n Pooja", 'plain')

# Part attachment
message.attach(textPart)

# Send Email and close connection
server.send_message(message)
server.quit()