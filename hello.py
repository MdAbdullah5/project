import smtplib


def test_smtp_connection():
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "bodavamshikrishna30@gmail.com"
        sender_password = "svmx bmqs omrb gktb"

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            print("SMTP connection successful!")
    except Exception as e:
        print(f"Error with SMTP connection: {e}")


test_smtp_connection()
