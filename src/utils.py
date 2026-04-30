import logging
import os
import sys
from src.constants import LOGS_DIR

def setup_logging(name):
    """Sets up a logger with file and console handlers."""
    logger = logging.getLogger(name)
    
    # Only configure if the logger doesn't already have handlers
    if not logger.handlers:
        logger.setLevel(logging.INFO)

        # Formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # File Handler for errors
        error_handler = logging.FileHandler(os.path.join(LOGS_DIR, "errors.log"), encoding='utf-8')
        error_handler.setLevel(logging.ERROR)
        error_handler.setFormatter(formatter)

        # File Handler for sent emails
        sent_handler = logging.FileHandler(os.path.join(LOGS_DIR, "sent_emails.log"), encoding='utf-8')
        sent_handler.setLevel(logging.INFO)
        sent_handler.setFormatter(formatter)

        # Console Handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)

        logger.addHandler(error_handler)
        logger.addHandler(sent_handler)
        logger.addHandler(console_handler)

    return logger

def get_sent_emails():
    """Reads the sent_emails.log and returns a set of already sent emails to avoid duplicates."""
    sent_emails_file = os.path.join(LOGS_DIR, "sent_emails.log")
    sent_emails = set()
    if os.path.exists(sent_emails_file):
        with open(sent_emails_file, "r", encoding="utf-8") as f:
            for line in f:
                # We expect the log format to be predictable, or we just search for "Sent email to: xxx@yyy.com"
                if "Successfully sent to:" in line:
                    parts = line.strip().split("Successfully sent to:")
                    if len(parts) > 1:
                        email = parts[1].strip().split()[0] # get just the email part
                        sent_emails.add(email)
    return sent_emails
