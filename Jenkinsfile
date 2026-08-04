pipeline {

    agent any

    environment {
        IMAGE_NAME = "arifulislamece7/employee-management"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
            dir('app/employee-web') {
            sh '''
                docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .
                docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_NAME}:latest
                '''

                }
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: '30a5abf5-1740-4e07-bf01-cc761cefff0f',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                    sh '''
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin

                    docker push ${IMAGE_NAME}:${BUILD_NUMBER}

                    docker push ${IMAGE_NAME}:latest
                    '''
                }
            }
        }

        stage('Deploy Kubernetes') {
            steps {

                sh '''

                kubectl apply -f employee-managment-k8s/

                '''

            }
        }

    }
}
