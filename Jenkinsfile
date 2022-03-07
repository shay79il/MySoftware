pipeline {
    agent any

    environment {
        REGION = 'eu-west-1'
        ENV_NAME = 'PROD'
    }

    stages {
        stage ('(1) Git checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/shay79il/UseOfJenkinsfile/'
            }
        }
        stage ('(2) Build image') {
            steps {
                sh 'docker build -t shay79il/python-app .'
            }
        }
    }

    post {
        success {
            echo "${env.BUILD_URL}"
            echo "======= SUCCESS =======\n======= SUCCESS =======\n======= SUCCESS =======\n"

            // stage ('(1) Push image to dockerHub')
            sh 'docker push shay79il/python-app'

            // stage ('(2) apply new namespace')
            sh 'kubectl apply -f ./staging-ns.yml'

            // stage ('(3) Add Helm Chart repo')
            sh 'helm repo add myhelmrepo https://shay79il.github.io/helm-chart/'

            // stage ('(4) Deploy my Helm Chart')
            sh 'helm upgrade --install mychart myhelmrepo/home-assignment-1   --namespace staging \
                --set myApp.REGION=${REGION} \
                --set myApp.ENV_NAME=${ENV_NAME}'
        }
        failure {
            echo "${env.BUILD_URL}"
            echo "======= FAIL !!! =======\n======= FAIL !!! =======\n======= FAIL !!! =======\n"
            echo "======= Build docker image \nshay79il/python-app FAILED!!! =======\n"
        }
    }
}