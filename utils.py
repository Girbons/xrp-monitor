import os


def get_smtp_server():
    try:
        return os.environ['SMTP_SERVER']
    except KeyError:
        raise KeyError('SMTP_SERVER not set')


def get_smtp_email():
    try:
        return os.environ['SMTP_EMAIL']
    except KeyError:
        raise KeyError('SMTP_EMAIL not set')


def get_smtp_email_receiver():
    try:
        return os.environ['SMTP_EMAIL_RECEIVER']
    except KeyError:
        raise KeyError('SMTP_EMAIL not set')


def get_semtp_password():
    try:
        return os.environ['SMTP_PASSWORD']
    except KeyError:
        raise KeyError('SMTP_PASSWORD not set')


def get_smtp_port():
    try:
        return os.environ['SMTP_PORT']
    except KeyError:
        raise KeyError('SMTP_PORT not set')


SMTP_SERVER = get_smtp_server()
SMTP_EMAIL = get_smtp_email()
SMTP_EMAIL_RECEIVER = get_smtp_email_receiver()
SMTP_PASSWORD = get_semtp_password()
SMTP_PORT = get_smtp_port()
