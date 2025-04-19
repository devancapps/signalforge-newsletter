import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

def send(html_content):
    """Send the newsletter via email."""
    # Email configuration
    smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
    smtp_port = int(os.getenv('SMTP_PORT', 587))
    username = os.getenv('EMAIL_USERNAME')
    password = os.getenv('EMAIL_PASSWORD')
    recipients = os.getenv('EMAIL_RECIPIENTS', '').split(',')
    subject = os.getenv('EMAIL_SUBJECT', '🔥 Weekly Top Affiliate Deals')

    if not all([username, password, recipients]):
        print("Missing email configuration. Please check your .env file.")
        return

    # Create message
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = username
    msg['To'] = ', '.join(recipients)

    # Attach HTML content
    msg.attach(MIMEText(html_content, 'html'))

    try:
        # Connect to SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)
        
        # Send email
        server.sendmail(username, recipients, msg.as_string())
        print("Newsletter sent successfully!")
        
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        server.quit() 