import pandas as pd

class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self, percent):
        df = pd.read_csv(self.file_path)

    # Drop ID
        if 'CustomerID' in df.columns:
            df = df.drop(columns=['CustomerID'])

    # Encode Gender
        if 'Gender' in df.columns:
            df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

    # Keep numeric
        df = df.select_dtypes(include=['number'])

    # Remove missing
        df = df.dropna()

        n = int(len(df) * percent / 100)
        return df.iloc[:n]