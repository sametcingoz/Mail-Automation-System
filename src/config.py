import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
    CV_PATH = os.getenv("CV_PATH", "attachments/CV.pdf")
    SEND_DELAY_SECONDS = int(os.getenv("SEND_DELAY_SECONDS", 60))

    @classmethod
    def validate(cls):
        """Validates that all necessary configuration variables are set."""
        missing = []
        if not cls.EMAIL_ADDRESS or cls.EMAIL_ADDRESS == "your_email@gmail.com":
            missing.append("EMAIL_ADDRESS")
        if not cls.EMAIL_PASSWORD or cls.EMAIL_PASSWORD == "your_app_password":
            missing.append("EMAIL_PASSWORD")
            
        if missing:
            raise ValueError(f"Missing or default configuration for: {', '.join(missing)}. Please update your .env file.")
        
        # We don't validate CV_PATH strictly on import since scraping doesn't need it.
        # But we do need it for sending.
