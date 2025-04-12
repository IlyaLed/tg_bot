pipeline {
    agent {
        docker {
            image 'python:3.12-slim'
            args '-v ${WORKSPACE}/.pip_cache:/root/.cache/pip'
        }
    }

    environment {
        BOT_TOKEN = credentials('API_TOKEN')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                sh """
                # Verify Python is available
                python --version
                
                # Install dependencies with cache
                pip install --upgrade pip
                pip install --cache-dir /root/.cache/pip \
                    aiogram==3.0.0b7 \
                    python-dotenv \
                    loguru
                """
            }
        }

        stage('Run Bot') {
            steps {
                sh """
                # Verify imports work
                python -c "from aiogram import Bot; print('Imports OK')"
                
                # Run with timeout (5 seconds)
                timeout 5 python -m bot || echo 'Bot exited with code $?'
                """
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        failure {
            echo 'Pipeline failed - check the logs above'
        }
    }
}