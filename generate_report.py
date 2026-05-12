from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generate_pdf(student_data, output_path):
    if not os.path.exists('output'):
        os.makedirs('output')
        
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width/2, height - 100, "Student Marksheet")
    
    c.setFont("Helvetica", 14)
    y_position = height - 150
    
    details = [
        f"USN: {student_data['USN']}",
        f"Name: {student_data['Name']}",
        f"Subject 1: {student_data['Subject1']}",
        f"Subject 2: {student_data['Subject2']}",
        f"Subject 3: {student_data['Subject3']}",
        f"Total Marks: {student_data['Total']}",
        f"Percentage: {student_data['Percentage']:.2f}%",
        f"Grade: {student_data['Grade']}",
        f"Status: {student_data['Status']}"
    ]
    
    for line in details:
        c.drawString(100, y_position, line)
        y_position -= 30
        
    c.save()

if __name__ == "__main__":
    sample_data = {
        'USN': '101', 'Name': 'John Doe', 'Subject1': 85, 'Subject2': 90, 
        'Subject3': 78, 'Total': 253, 'Percentage': 84.33, 'Grade': 'B', 'Status': 'Pass'
    }
    generate_pdf(sample_data, "output/sample_result.pdf")
