pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.12'
        // Секреты 
        BOT_TOKEN = credentials('API_TOKEN')
    }

    stage('Verify Token') {
        steps {
            script {
                echo "Токен бота: ${env.BOT_TOKEN}"  
                // Проверка работы с API Telegram
                sh """
                    curl -s "https://api.telegram.org/bot${env.BOT_TOKEN}/getMe" | jq
                """
            }
        }
    }
    
    stages {
        //  Получение кода из репозитория
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        // Настройка Python
        stage('Setup Python') {
            steps {
                sh "python --version"
                sh "python -m pip install --upgrade pip"
            }
        }

        stage('Environment Check') {
            steps {
                sh "python${PYTHON_VERSION} -c \"import os, logging, asyncio; from dotenv import load_dotenv; from aiogram import Bot, Dispatcher, types, F; print('All imports OK!')\""
            }
        }

        // Запуск бота
        stage('Run Bot') {
            when {
                branch 'master' 
            }
            steps {
                sh "python -m bot" 
            }
        }
    }

    post {
        always {
            // Очистка 
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