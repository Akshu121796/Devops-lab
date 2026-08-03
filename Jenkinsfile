pipeline {

    agent any

    stages {

        stage('Checkout Source Code') {
            steps {
                echo 'Downloading latest application code from GitHub...'
                git branch: 'main',
                url: 'https://github.com/sayleenarkhede/Jenkins-CI-Demo.git'
            }
        }

        stage('Verify Application Files') {
            steps {
                echo 'Checking project files...'
                bat 'if exist index.html (echo index.html Found) else (exit 1)'
                bat 'if exist style.css (echo style.css Found) else (exit 1)'
                bat 'if exist script.js (echo script.js Found) else (exit 1)'
            }
        }

        stage('Create Build Artifact') {
            steps {
                echo 'Packaging application...'
                bat 'powershell Compress-Archive -Path * -DestinationPath WebApplication.zip -Force'
            }
        }

        stage('Archive Build') {
            steps {
                archiveArtifacts artifacts: 'WebApplication.zip', fingerprint: true
            }
        }

    }

    post {

        success {
            echo 'Application Build Completed Successfully.'
        }

        failure {
            echo 'Application Build Failed.'
        }

    }

}
