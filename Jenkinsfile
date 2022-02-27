node {
    stage("1. Clone a repository of your choice") {
        git branch: 'main', url: 'https://github.com/shay79il/UseOfJenkinsfile.git'
    }
    stage("2. Run a git command and show its output.") {
        sh "git log"
    }
    stage("3. Print a message to the console from the JenkinsFile itself.") {
        sh "echo Hello World"
    }
    stage("4. Run a file/script of your choice which will in turn print a message to the console.") {
        sh "chmod +x printHello.sh"
        sh "./printHello.sh"
    }
}
