import smtplib
from email.message import EmailMessage

class AlertDispatcher:
    def __init__(self, email_config):
        self.smtp_server = email_config['smtp_server']
        self.smtp_port = email_config['smtp_port']
        self.login = email_config['login']
        self.password = email_config['password']
        self.recipient = email_config['recipient']

    def send_email(self, subject, body):
        """ Send an email alert. """
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = self.login
        msg['To'] = self.recipient

        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
            server.login(self.login, self.password)
            server.send_message(msg)

    def log_event(self, event):
        """ Log an event to a local file. """
        with open('event_log.txt', 'a') as file:
            file.write(f"{event}\n")

email_config = {
    'smtp_server': 'smtp.example.com',
    'smtp_port': 465,
    'login': 'user@example.com',
    'password': 'password',
    'recipient': 'admin@example.com'
}
dispatcher = AlertDispatcher(email_config)
dispatcher.log_event("Unauthorized file access detected.")
dispatcher.send_email("Security Alert", "Unauthorized file access was detected.")
