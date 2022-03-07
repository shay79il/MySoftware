properties([parameters([[$class: 'ChoiceParameter', choiceType: 'PT_SINGLE_SELECT', filterLength: 1, filterable: false, name: 'ENV_NAME', randomName: 'choice-parameter-22735858864625', script: [$class: 'GroovyScript', fallbackScript: [classpath: [], sandbox: false, script: 'return [\'QA\']'], script: [classpath: [], sandbox: false, script: 'return [\'QA\',\'PRODUCTION\',\'PREPRODUCTION\']']]], [$class: 'CascadeChoiceParameter', choiceType: 'PT_SINGLE_SELECT', filterLength: 1, filterable: false, name: 'REGION', randomName: 'choice-parameter-22735863703539', referencedParameters: 'ENV_NAME', script: [$class: 'GroovyScript', fallbackScript: [classpath: [], sandbox: false, script: 'return [\'us-east-1\']'], script: [classpath: [], sandbox: false, script: '''def choices
switch(ENV_NAME){
    case \'PRODUCTION\':
        choices = [\'us-west-1\', \'eu-central-2\', \'ap-south-1\']
        break
    case \'PREPRODUCTION\':
        choices = [\'us-east-2\', \'eu-west-3\']
        break
    case \'QA\':
        choices = [\'us-east-1\']
        break
    default:
        choices = [\'us-east-1\']
        break
}
return choices''']]]]), [$class: 'JobLocalConfiguration', changeReasonComment: '']])




pipeline {
    agent any

    stages {
        stage ('(1) Git clone') {
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