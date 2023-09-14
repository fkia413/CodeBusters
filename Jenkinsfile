pipeline {
	agent any
	// specify environment variables - used for docker
	environment {
		SECRET_KEY = credentials("SECRET_KEY")
		DB_PASSWORD = credentials("DB_PASSWORD")
		DB_HOST = credentials("DB_HOST")
		DOCKER_LOGIN = credentials("DOCKER_LOGIN")
	}
	stages {
		stage("Build") {
			steps {
				sh "sudo apt update -y && sudo apt install -y python3 python3-pip"
			}
		}
		stage("Dependencies") {
			steps {
				sh "pip install -r requirements.txt"
			}
		}
		stage("Test") {
			steps {
				sh "python3 -m pytest --cov=application --cov-report html"
			}
			post {
				always {
					achiveArtifacts 'htmlcov/**'
				}
			}
		}
		stage("Build Docker image") {
			steps {
				sh "docker build -t 1391819/qa-cinema:latest ."
			}
		}
		stage("Push to Docker Hub") {
			steps {
				withCredentials([usernamePassword(credentialsId: 'DOCKER_LOGIN', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
					sh "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"
                    			//sh "docker push 1391819/qa-cinema:latest"
                		}
			}
		}
		// this uses the local database, not the cloud one
		// the cloud one is accessible only through the instances created using the Terraform configuration
		stage("Deploy") {
			steps {
				sh "python3 app.py"
			}
		}
	}
}
