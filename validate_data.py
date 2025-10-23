import pandas as pd
import re 

def validate_csv(file_path):
    df = pd.read_csv(file_path)
    print(f'Loaded {len(df)} rows\n')

    # check for missing values 
    missing = df.isnull().sum()
    print('Missing values per column: ')
    print(missing[missing > 0], "\n")

    # check for duplicate entries
    duplicates = df[df.duplicated()]
    print(f'Found {len(duplicates)} duplicate rows\n')

    # check for digit entries only in column: age
    invalid_age = df[~df['age'].astype(str).str.isdigit()]
    print(f'Invalid ages: {len(invalid_age)} rows\n')

    # check email format
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    invalid_emails = df[~df['email'].astype(str).str.match(email_pattern, na=False)]
    print(f'Invalid emails: {len(invalid_emails)} rows\n')

    print('Validation completed.\n')


if __name__ == "__main__":
    validate_csv("data/data.csv")




