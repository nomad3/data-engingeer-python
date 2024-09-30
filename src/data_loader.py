import pandas as pd
import logging

class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_data(self) -> pd.DataFrame:
        """Load the CSV file and handle errors efficiently."""
        try:
            logging.info(f"Loading data from {self.file_path}")
            df = pd.read_csv(self.file_path)
            df['date'] = pd.to_datetime(df['date']).dt.date  # Normalize dates
            return df
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            raise
