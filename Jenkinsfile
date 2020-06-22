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
        post {
            always {
                script {
                    allure ([
                    includeProperties: false,
                    jdk: '',
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'python-selenium/allure-results']]])
                }
        }
    }
    }
  }
