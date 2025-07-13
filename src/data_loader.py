import pandas as pd

class AnimeDataLoader:
    def __init__(self, original_csv: str, processed_csv: str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_original_data(self) -> str:
        """Load the original anime data from a CSV file."""
        df = pd.read_csv(
            self.original_csv,
            encoding='utf-8',
            on_bad_lines='error'
        ).dropna()

        required_column = {'Name', 'Genres', 'sypnopsis'}

        missing_column = required_column - set(df.columns)

        if missing_column:
            raise ValueError(f"Missing required columns in the CSV: {missing_column}")

        df['combined_info'] = (
            "Title: " + df['Name'] 
            + ' Genres: ' + df['Genres'] 
            + ' ..Overview: ' + df['sypnopsis']
        )
        df[['combined_info']].to_csv(self.processed_csv, index=False, encoding='utf-8') 
        return self.processed_csv