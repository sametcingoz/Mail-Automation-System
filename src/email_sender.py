import os
import smtplib
import time
import pandas as pd
from email.message import EmailMessage
from src.config import Config
from src.constants import CATEGORIES, APPROVED_DATA_DIR
from src.email_templates import get_template_for_category
from src.utils import setup_logging, get_sent_emails

logger = setup_logging("email_sender")

def send_emails(dry_run=False):
    """Reads approved CSV files and sends emails, preventing duplicates."""
    logger.info(f"Starting email sender... (Dry run: {dry_run})")
    
    # Ensure config is valid before proceeding
    if not dry_run:
        Config.validate()
        if not os.path.exists(Config.CV_PATH):
            raise FileNotFoundError(f"CV file not found at: {Config.CV_PATH}")
            
    sent_emails_set = get_sent_emails()
    logger.info(f"Loaded {len(sent_emails_set)} previously sent emails to prevent duplicates.")
    
    for cat_name, cat_data in CATEGORIES.items():
        csv_name = cat_data["csv_name"]
        approved_path = os.path.join(APPROVED_DATA_DIR, csv_name)
        
        if not os.path.exists(approved_path):
            logger.warning(f"Approved CSV not found for category {cat_name}: {approved_path}. Skipping.")
            continue
            
        try:
            df = pd.read_csv(approved_path)
        except Exception as e:
            logger.error(f"Failed to read CSV {approved_path}: {e}")
            continue
            
        if df.empty:
            logger.info(f"CSV {approved_path} is empty. Skipping.")
            continue
            
        logger.info(f"Processing {len(df)} companies for category: {cat_name}")
        
        try:
            subject, body = get_template_for_category(cat_name)
        except Exception as e:
            logger.error(f"Failed to get template for {cat_name}: {e}")
            continue

        for index, row in df.iterrows():
            company_name = row.get("Company Name", "Unknown Company")
            emails = str(row.get("Email", ""))
            
            if not emails or str(emails).strip().lower() == 'nan':
                logger.warning(f"No valid email found for {company_name}. Skipping.")
                continue
                
            # If there are multiple emails separated by commas, we'll send to the first one
            # Or you can split and send to all. We will just use the first valid one.
            email_list = [e.strip() for e in emails.split(",")]
            target_email = email_list[0]
            
            if target_email in sent_emails_set:
                logger.info(f"Skipping {company_name} ({target_email}) - Already sent.")
                continue
                
            logger.info(f"Preparing to send to {company_name} ({target_email})...")
            
            if dry_run:
                logger.info(f"[DRY RUN] Would send email to: {target_email} with subject: '{subject}'")
                continue
                
            # Actual sending logic
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = Config.EMAIL_ADDRESS
            msg['To'] = target_email
            msg.set_content(body)
            
            # Attach CV
            try:
                with open(Config.CV_PATH, 'rb') as f:
                    pdf_data = f.read()
                    msg.add_attachment(pdf_data, maintype='application', subtype='pdf', filename=os.path.basename(Config.CV_PATH))
            except Exception as e:
                logger.error(f"Failed to attach CV for {company_name}: {e}")
                continue
                
            try:
                with smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT) as server:
                    server.starttls()
                    server.login(Config.EMAIL_ADDRESS, Config.EMAIL_PASSWORD)
                    server.send_message(msg)
                    
                logger.info(f"Successfully sent to: {target_email} ({company_name})")
                sent_emails_set.add(target_email)
                
                # Politeness delay
                logger.info(f"Waiting for {Config.SEND_DELAY_SECONDS} seconds before the next email...")
                time.sleep(Config.SEND_DELAY_SECONDS)
                
            except Exception as e:
                logger.error(f"Failed to send email to {target_email} ({company_name}): {e}")

    logger.info("Email sending process completed.")
