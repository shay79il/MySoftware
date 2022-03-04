pipeline {
    agent any

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
            sh 'docker push shay79il/python-app'
        }
        failure {
            echo "${env.BUILD_URL}"
            echo "======= FAIL !!! =======\n======= FAIL !!! =======\n======= FAIL !!! =======\n"
        }
    }
}