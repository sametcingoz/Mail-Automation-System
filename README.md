# Internship Email Automation

This project is a professional Python automation tool designed to streamline internship applications to companies. It extracts company details from specific categories and sends personalized emails securely and reliably, preventing duplicate sends and avoiding spam-like behavior.

## Features

- **Automated Web Scraping**: Extracts company names, websites, and email addresses.
- **Category-Based Templates**: Uses a specific email subject and body template for each category.
- **Safe Sending Protocol**: Includes a delay between each email to prevent triggering spam filters.
- **Duplicate Prevention**: Keeps a log of sent emails (`logs/sent_emails.log`) so you never email the same company twice.
- **Manual Review Step**: Requires manual approval of scraped data before any email is sent.
- **Dry-Run Mode**: Allows testing the entire email sending pipeline without actually sending emails.
- **CV Attachment**: Automatically attaches your CV (PDF) to every outgoing email.

## Setup & Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd internship-email-automation
   ```

2. **Install dependencies**:
   It is recommended to use a virtual environment.
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   
   pip install -r requirements.txt
   ```

3. **Configuration**:
   Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
   Open `.env` and fill in your details:
   - `EMAIL_ADDRESS`: Your email (e.g., `sametcingoz1@gmail.com`)
   - `EMAIL_PASSWORD`: Your email app password (for Gmail, you need to generate an App Password).
   - `SMTP_SERVER`: Default is `smtp.gmail.com`
   - `SMTP_PORT`: Default is `587`
   - `CV_PATH`: Path to your CV file (e.g., `attachments/CV.pdf`)
   - `SEND_DELAY_SECONDS`: The delay between sending emails (e.g., `60`). Do not set this too low to avoid spam limits.

4. **Add Your CV**:
   Place your CV (e.g., `CV.pdf`) into the `attachments/` folder. Ensure the filename matches `CV_PATH` in your `.env` file.

## Usage Guide

The automation process works in three main steps: **Scrape**, **Review**, and **Send**.

### 1. Scrape Company Data

Run the scraper to collect company information from the 4 specified categories.
```bash
python src/main.py scrape
```
This will:
- Parse the directory pages with a polite delay (1-2 seconds) between requests.
- Save all scraped companies into `data/raw/`.
- Save only companies that have an email address into `data/processed/`.

### 2. Manual Review & Approval

**Crucial Step:** Emails are **never** sent automatically after scraping.
You must manually review the files in `data/processed/` and decide which companies you want to apply to.

- Open `data/processed/<category>.csv`.
- Delete the rows of companies you do NOT want to email.
- Copy or move the finalized CSV file to the `data/approved/` folder.

### 3. Send Emails

Before actually sending emails, it's highly recommended to run a **dry-run**. This simulates the sending process and logs what would happen, without sending anything.

```bash
python src/main.py send --dry-run
```

Once you are satisfied with the dry-run output, execute the real sending command:

```bash
python src/main.py send
```

This will:
- Read the approved CSV files.
- Match them with the correct email template for that category.
- Attach your CV.
- Send the email.
- Wait for `SEND_DELAY_SECONDS`.
- Record the successful send in `logs/sent_emails.log`.

### Checking Logs

- Successful emails are logged in `logs/sent_emails.log`.
- Any errors during the process are logged in `logs/errors.log`.

## Responsible Use Warning

**Important**: This project is for personal internship applications only. It should not be used as a spam bot or mass-marketing tool. The manual approval step, rate limiting, and duplicate prevention are intentionally built in to ensure professional and responsible communication. 
