# get user input
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase

from email.utils import make_msgid
from email.message import EmailMessage
import mimetypes
from getpass import getpass

msg = EmailMessage()

EMAIL_HOST = 'smtp.gmail.com'


def send_email(text,filename):
    from_addr = input("from: ")
    to_addr = input("to: ")
    password = getpass()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Data Insights'

    image_cid = make_msgid(domain='xyz.com')

    msg.add_alternative("""\
    <html>
        <body>
            <p>Software Jobs.<br>
                {text}
            </p>
            <img src="cid:{image_cid}">
        </body>
    </html>
    """.format(image_cid=image_cid[1:-1],text=text), subtype='html')
    # to add an attachment is just add a MIMEBase object to read a picture locally.
    with open(f'./output/{filename}.png', 'rb') as img:

        maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')

        # attach it
        msg.get_payload()[0].add_related(img.read(),
                                         maintype=maintype,
                                         subtype=subtype,
                                         cid=image_cid)

    server = smtplib.SMTP(EMAIL_HOST)
    server.connect(EMAIL_HOST)

    server.starttls()
    server.set_debuglevel(1)

    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
