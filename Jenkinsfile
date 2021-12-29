properties([[$class: 'JobLocalConfiguration', changeReasonComment: ''], pipelineTriggers([pollSCM('30 * * * *  ')])])
node {
    stage("clone") {
        git branch: 'main', url: 'https://github.com/shay79il/MySoftware.git'
    }
    stage("show files") {
        sh "ls -l"
    }
}