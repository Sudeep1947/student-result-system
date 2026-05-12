import pandas as pd
import os

def calculate_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 60:
        return 'C'
    else:
        return 'D'

def process_marks(csv_path):
    if not os.path.exists(csv_path):
        return None
    
    df = pd.read_csv(csv_path)
    
    # Validation
    if df.isnull().values.any():
        raise ValueError("CSV contains empty values")
    
    if df['USN'].duplicated().any():
        raise ValueError("Duplicate USN found")
        
    subjects = ['Subject1', 'Subject2', 'Subject3']
    for sub in subjects:
        if (df[sub] < 0).any() or (df[sub] > 100).any():
            raise ValueError(f"Invalid marks in {sub}")

    # Calculations
    df['Total'] = df[subjects].sum(axis=1)
    df['Percentage'] = (df['Total'] / (len(subjects) * 100)) * 100
    df['Grade'] = df['Percentage'].apply(calculate_grade)
    df['Status'] = df['Percentage'].apply(lambda x: 'Pass' if x >= 60 else 'Fail')
    
    return df

if __name__ == "__main__":
    try:
        results = process_marks('marks.csv')
        print(results)
    except Exception as e:
        print(f"Error: {e}")
