import argparse
import sys
import os
from src.scraper import run_scraper
from src.email_sender import send_emails
from src.constants import PROCESSED_DATA_DIR, APPROVED_DATA_DIR

def main():
    parser = argparse.ArgumentParser(description="Internship Email Automation Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Scrape command
    subparsers.add_parser("scrape", help="Scrape company data from Hacettepe Teknokent directory.")

    # Review command
    subparsers.add_parser("review", help="Show instructions for reviewing and approving scraped data.")

    # Send command
    send_parser = subparsers.add_parser("send", help="Send emails to approved companies.")
    send_parser.add_argument("--dry-run", action="store_true", help="Simulate sending emails without actually sending them.")

    args = parser.parse_args()

    if args.command == "scrape":
        run_scraper()
    elif args.command == "review":
        print("\n--- Manual Review Instructions ---")
        print(f"1. Open the CSV files in: {os.path.abspath(PROCESSED_DATA_DIR)}")
        print("2. Delete rows for companies you do NOT want to email.")
        print(f"3. Move or copy the finalized files to: {os.path.abspath(APPROVED_DATA_DIR)}")
        print("4. Ensure your .env is configured and CV is in the attachments folder.")
        print("5. Run `python src/main.py send --dry-run` to test.")
        print("----------------------------------\n")
    elif args.command == "send":
        send_emails(dry_run=args.dry_run)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
