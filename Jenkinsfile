pipeline {
    agent any
    environment {
        registry = "shreyasarjun/python_app_with_cicd_pipeline"
        registryCredential = 'DOCKERHUB_CREDENTIALS'
        dockerImage = ''
    }

    stages {
        stage('Step1: Pulling source code from GitHub repository') {
            steps {
                git branch: 'master', credentialsId: 'Shreyas_Github', url: 'https://github.com/shreyasarjun/Python_Devops_Pipeline.git'
            }
        }

        stage('Step2: Building docker image') {
            steps {
                script {
                    dockerImage = docker.build registry
                }
            }
        }
        
        stage('Upload image to dockerhub') {
            steps{    
                script {
                    docker.withRegistry( '', registryCredential ) {
                    dockerImage.push()
                                }
                }
            }
        }
        
        
        stage('Docker Run') {
            steps{
                script {
                    dockerImage.run("-p 5000:5000 --rm --name python_app_with_cicd_pipeline")
         }
      }
    }
    }
}
