# Automated Student Result Deployment System

A production-ready full-stack automation system for processing student results, generating reports, and deploying via CI/CD.

## 🚀 Features
- **Modern Dashboard**: Glassmorphism UI with real-time analytics.
- **Automated Processing**: Python-based CSV parsing and grade calculation.
- **PDF Generation**: Dynamic marksheet generation using ReportLab.
- **CI/CD Pipeline**: Full Jenkins integration for automated testing and deployment.
- **Responsive Design**: Fully mobile-friendly interface with dark/light mode.

## 🛠️ Tech Stack
- **Backend**: Python (Flask, Pandas)
- **Frontend**: HTML5, CSS3, JavaScript (Bootstrap 5, Chart.js)
- **CI/CD**: Jenkins
- **Testing**: PyTest
- **Reports**: ReportLab (PDF)

## 📁 Project Structure
```text
student-result-system/
│── app.py               # Flask Backend
│── process_results.py   # Business Logic
│── generate_report.py   # PDF Logic
│── marks.csv            # Data Source
│── requirements.txt     # Dependencies
│── Jenkinsfile          # CI/CD Pipeline
│── templates/           # UI Templates
│── static/              # CSS/JS Assets
│── output/              # Generated Reports
└── tests/               # Unit Tests
```

## ⚙️ Installation & Setup

### 1. Local Environment
1. Install Python 3.9+
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Access at `http://localhost:5000`

### 2. Jenkins Setup
1. Create a New Pipeline Job in Jenkins.
2. Link your GitHub repository.
3. Jenkins will automatically use the `Jenkinsfile` for:
   - Dependency installation.
   - CSV validation.
   - Running PyTest.
   - Generating student PDF reports.
   - Archiving artifacts.

## 📊 Business Logic (Grading Scale)
- **A**: >= 90%
- **B**: >= 80%
- **C**: >= 60%
- **D**: < 60% (Fail)

## 🧪 Running Tests
Execute the following command to run the automated test suite:
```bash
pytest tests/test_app.py
```

## ❓ Viva Questions
1. **How does Jenkins detect changes?** Using Webhooks or SCM Polling.
2. **What is the role of Pandas here?** For high-performance data manipulation and CSV parsing.
3. **How is the PDF generated?** Using the ReportLab library's canvas API.
4. **Why use Flask?** It's a lightweight WSGI web framework perfect for microservices.
