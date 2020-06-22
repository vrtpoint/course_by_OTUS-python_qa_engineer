properties([disableConcurrentBuilds()])

pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
        timestamps()
    }
    stages {
        stage("memory information") {
            steps {
                sh "free -h"
            }
        }
        stage('tests') {
            steps {
                sh "pytest -v -s"
            }
        }
    }
}
