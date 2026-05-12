pipeline {
    agent any
    
    environment {
        // Detect OS for command execution
        IS_WINDOWS = isUnix() ? false : true
    }

    stages {
        stage('Setup') {
            steps {
                script {
                    if (IS_WINDOWS) {
                        bat 'python -m pip install --upgrade pip'
                        bat 'pip install -r requirements.txt'
                    } else {
                        sh 'pip3 install -r requirements.txt'
                    }
                }
            }
        }

        stage('Validation') {
            steps {
                script {
                    if (IS_WINDOWS) {
                        bat 'python process_results.py'
                    } else {
                        sh 'python3 process_results.py'
                    }
                }
            }
        }

        stage('Testing') {
            steps {
                script {
                    if (IS_WINDOWS) {
                        bat 'pytest tests/test_app.py'
                    } else {
                        sh 'pytest tests/test_app.py'
                    }
                }
            }
        }

        stage('Artifact Generation') {
            steps {
                script {
                    if (IS_WINDOWS) {
                        bat 'python generate_report.py'
                    } else {
                        sh 'python3 generate_report.py'
                    }
                }
                archiveArtifacts artifacts: 'output/*.pdf', fingerprint: true
            }
        }

        stage('Deployment') {
            steps {
                echo 'Deploying Automated Student Result System...'
                // In production, this would restart a service or update a container
            }
        }
    }

    post {
        always {
            junit testResults: '**/test-results/*.xml', allowEmptyResults: true
        }
        success {
            echo 'Build and Deployment Successful!'
            // mail to: 'admin@example.com', subject: 'Deployment Success', body: 'The system has been deployed successfully.'
        }
        failure {
            echo 'Build Failed. Please check logs.'
        }
    }
}
