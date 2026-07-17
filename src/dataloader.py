import pandas as pd

common_encodings = ['utf-8', 'latin1', 'ISO-8859-1', 'cp1252']

def load_csv(df):

    for encoding in common_encodings:
        df.seek(0)  # Reset the file pointer to the beginning of the file
        try:
            return pd.read_csv(df, encoding=encoding)
        except Exception as e:
            continue
    raise ValueError("Unable to read the CSV file with common encodings.")