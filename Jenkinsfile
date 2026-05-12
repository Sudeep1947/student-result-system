pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                dir('student-result-system') {
                    bat 'npm install'
                }
            }
        }

        stage('Build') {
            steps {
                dir('student-result-system') {
                    bat 'npm run build'
                }
            }
        }

        stage('Start Application') {
            steps {
                dir('student-result-system') {
                    bat 'npm start'
                }
            }
        }
    }
}
