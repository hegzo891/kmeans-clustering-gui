import pandas as pd

class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self, percent):
        df = pd.read_csv(self.file_path)

        # Drop CustomerID (not useful)
        if 'CustomerID' in df.columns:
            df = df.drop(columns=['CustomerID'])

        # Select ONLY required features
        df = df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]


        # Apply percentage
        n = int(len(df) * percent / 100)
        return df.iloc[:n]