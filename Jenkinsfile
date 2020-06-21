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
        stage("create docker image") {
            steps {
                echo "start building image"
                sh "docker build - < Dockerfile"
            }
        }
        stage('lint') {
            steps {
                sh 'flake8 .'
            }
        }
        stage('tests') {
            steps {
                sh "pytest -v -s"
            }
        }
    }
  }
