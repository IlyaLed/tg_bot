pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.12'
        BOT_TOKEN = credentials('API_TOKEN')
    }

    stages {
        // Проверка токена (перенесено внутрь stages)
        stage('Verify Token') {
            steps {
                script {
                    echo "Проверка токена..."  
                    sh """curl -s "https://api.telegram.org/bot${env.BOT_TOKEN}/getMe\""""
                }
            }
        }

        // Получение кода из репозитория
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        // Настройка Python
        stage('Setup Python') {
            steps {
                sh "python${env.PYTHON_VERSION} --version"
                sh "python${env.PYTHON_VERSION} -m pip install --upgrade pip"
            }
        }

        // Проверка окружения
        stage('Environment Check') {
            steps {
                sh """
                    python${env.PYTHON_VERSION} -c "import os, logging, asyncio; from dotenv import load_dotenv; from aiogram import Bot, Dispatcher, types, F; print('All imports OK!')"
                """
            }
        }

        // Запуск бота
        stage('Run Bot') {
            when {
                branch 'master' 
            }
            steps {
                sh "python${env.PYTHON_VERSION} -m bot" 
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo 'Pipeline успешно завершен!'
        }
        failure {
            echo 'Pipeline завершился с ошибкой!'
        }
    }
}