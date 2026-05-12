from flask import Flask, render_template, request, send_file, jsonify
import pandas as pd
import os
from process_results import process_marks
from generate_report import generate_pdf

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs('output', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    try:
        df = process_marks('marks.csv')
        data = df.to_dict(orient='records')
        
        stats = {
            'total': len(df),
            'average': round(df['Percentage'].mean(), 2),
            'pass_count': len(df[df['Status'] == 'Pass']),
            'fail_count': len(df[df['Status'] == 'Fail']),
            'topper': df.loc[df['Total'].idxmax()]['Name']
        }
        
        # Grade Distribution for Chart
        grades = df['Grade'].value_counts().to_dict()
        
        return render_template('dashboard.html', students=data, stats=stats, grades=grades)
    except Exception as e:
        return f"Error: {e}"

@app.route('/download/<usn>')
def download_pdf(usn):
    try:
        df = process_marks('marks.csv')
        student = df[df['USN'].astype(str) == str(usn)].iloc[0].to_dict()
        pdf_path = f"output/result_{usn}.pdf"
        generate_pdf(student, pdf_path)
        return send_file(pdf_path, as_attachment=True)
    except Exception as e:
        return f"Error: {e}"

@app.route('/api/results')
def get_results():
    try:
        df = process_marks('marks.csv')
        return jsonify(df.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
