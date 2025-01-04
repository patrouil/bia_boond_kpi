import logging
import smtplib
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Mailler:
    SMTP_PORT = 587

    def __init__(self, server_smpt: str, sender_email: str, sender_password: str):
        self.logger = logging.getLogger(__name__)
        self.server_smtp = server_smpt
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.attached_file = None
        return

    # end
    def body(self, body_msg) -> None:
        self.message_body = body_msg
        return

    def recipient(self, dest_email: str) -> None:
        self.recipient_address = dest_email
        return

    def subject(self, subject_txt: str) -> None:
        self.subject_text = subject_txt
        return

    def attach(self, filename: str) -> None:
        self.attached_file = filename

    def send(self):
        # Création du message
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = self.recipient_address
        msg['Subject'] = self.subject_text
        # Ajout du corps du message
        msg.attach(MIMEText(self.message_body, 'plain'))
        if (self.attached_file):
            with open(self.attached_file, 'rb') as fichier:
                piece_jointe = MIMEApplication(fichier.read())
                piece_jointe.add_header('Content-Disposition', 'attachment',
                                        filename=self.attached_file)  # Nom de la pièce jointe
                msg.attach(piece_jointe)
        # Connexion au serveur SMTP
        try:
            server = smtplib.SMTP(self.server_smtp, self.SMTP_PORT)
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            text = msg.as_string()
            r = server.sendmail(self.sender_email, self.recipient_address, text)
            self.logger.debug("sending mail %s", str(r))
        except Exception as e:
            self.logger.error(f"Une erreur s'est produite : {str(e)}")
        finally:
            server.quit()
        return
    # end
