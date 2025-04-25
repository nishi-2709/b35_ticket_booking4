pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'ticket-booking'
        DOCKER_TAG = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Test') {
            steps {
                sh 'docker-compose run web python manage.py test'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
} 