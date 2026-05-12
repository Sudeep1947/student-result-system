import pytest
import sys
import os

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app
from process_results import calculate_grade, process_marks

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_grade_calculation():
    assert calculate_grade(95) == 'A'
    assert calculate_grade(85) == 'B'
    assert calculate_grade(65) == 'C'
    assert calculate_grade(50) == 'D'

def test_index_page(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Automated Result System' in rv.data

def test_dashboard_page(client):
    rv = client.get('/dashboard')
    assert rv.status_code == 200
    assert b'Student Results' in rv.data

def test_csv_processing():
    # Ensure marks.csv exists or use a temporary one
    df = process_marks('marks.csv')
    assert df is not None
    assert 'Total' in df.columns
    assert 'Grade' in df.columns
    assert 'Status' in df.columns

def test_api_endpoint(client):
    rv = client.get('/api/results')
    assert rv.status_code == 200
    data = rv.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
