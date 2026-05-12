pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'npm install'
                    } else {
                        bat 'npm install'
                    }
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'npm run build'
                    } else {
                        bat 'npm run build'
                    }
                }
            }
        }

        stage('Start Application') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'npm start'
                    } else {
                        bat 'npm start'
                    }
                }
            }
        }
    }
}
