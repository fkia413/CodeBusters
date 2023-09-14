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
				sh "sudo apt install -y python3 python3-pip"
				sh "export SECRET_KEY=${SECRET_KEY}"
				sh "export DB_PASSWORD=${DB_PASSWORD}"
				sh "export DB_HOST=${DB_HOST}"
				sh "docker login -u ${DOCKER_LOGIN_USR} -p ${DOCKER_LOGIN_PSW}"
			}
		}
		stage("Dependencies") {
			steps {
				sh "pip install -r requirements.txt"
			}
		}
		stage("Deploy") {
			steps {
				sh "python3 app.py"
			}
		}
	}
}
