import os.path
import getpass
import mimetypes
import smtplib
from reportlab.platypus import Paragraph, Spacer, Table, Image, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from email.message import EmailMessage
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

message = EmailMessage()

sender = "dracospitfire@gmail.com"
recipient = 'austin3flores@gmail.com'

message['From'] = sender
message['To'] = recipient

message['Subject'] = "Greetings from {} to {}!".format(sender, recipient)

body = """Hey there! I'm learning to send emails using Python!"""

message.set_content(body)

attachment_path = "example.png"
attachment_filename = os.path.basename(attachment_path)

mime_type, _ = mimetypes.guess_type(attachment_path)

mime_type, mime_subtype = mime_type.split('/', 1)

with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
        maintype=mime_type,
        subtype=mime_subtype,
        filename=os.path.basename(attachment_path))

mail_server = smtplib.SMTP_SSL("smtp.gmail.com")
mail_pass = 'jtlvugftutewwail' #getpass.getpass('Password? ')
mail_server.login(sender, mail_pass)

mail_server.send_message(message)
mail_server.quit()

fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

report = SimpleDocTemplate("A Complete Inventory of My Fruit.pdf")
styles = getSampleStyleSheet()
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])

table_data = []
for k, v in fruit.items():
    table_data.append([k, v])

table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

report_pie = Pie(width=3*"inch", height=3*"inch")

report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)
report_chart = Drawing()
report_chart.add(report_pie)

report.build([report_title, report_table, report_chart])

