"""
Constants used across the project.
"""
import os

# Base paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")
APPROVED_DATA_DIR = os.path.join(DATA_DIR, "approved")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

# Categories and their source URLs
CATEGORIES = {
    "Computer_and_Communication_Technologies": {
        "url": "https://www.hacettepeteknokent.com.tr/tr/firma_rehberi/bilgisayar_ve_iletisim_teknolojileri-16",
        "csv_name": "computer_communication.csv"
    },
    "Electronics": {
        "url": "https://www.hacettepeteknokent.com.tr/tr/firma_rehberi/elektronik-17",
        "csv_name": "electronics.csv"
    },
    "Defense_Industry_and_Aviation": {
        "url": "https://www.hacettepeteknokent.com.tr/tr/firma_rehberi/savunma_sanayi_havacilik-27",
        "csv_name": "defense_aviation.csv"
    },
    "Software": {
        "url": "https://www.hacettepeteknokent.com.tr/tr/firma_rehberi/yazilim-29",
        "csv_name": "software.csv"
    }
}
