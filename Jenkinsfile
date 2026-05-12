pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                dir('jenkins-result-main') {
                    bat 'npm install'
                }
            }
        }

        stage('Build') {
            steps {
                dir('jenkins-result-main') {
                    bat 'npm run build'
                }
            }
        }

        stage('Start Application') {
            steps {
                dir('jenkins-result-main') {
                    bat 'npm start'
                }
            }
        }
    }
}
