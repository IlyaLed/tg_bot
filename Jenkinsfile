pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.12'
        BOT_TOKEN = credentials('API_TOKEN')  // Токен будет автоматически маскироваться
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                sh "python${env.PYTHON_VERSION} --version"
                sh "python${env.PYTHON_VERSION} -m pip install --upgrade pip"
                
                // Безопасная проверка токена
                script {
                    def botInfo = sh(
                        script: "curl -s 'https://api.telegram.org/bot${env.BOT_TOKEN}/getMe'",
                        returnStdout: true
                    )
                    echo "Bot username: ${botInfo.tokenize('"username":"')[1].tokenize('"')[0]}"
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                sh "python${env.PYTHON_VERSION} -m pip install aiogram python-dotenv loguru"
            }
        }

        stage('Run Bot') {
            when {
                branch 'main'  // Исправлено с master на main (актуально для новых репозиториев)
            }
            steps {
                sh "python${env.PYTHON_VERSION} -m bot"
            }
        }
    }

    post {
        always {
            cleanWs()
            script {
                def duration = currentBuild.durationString.replace(' and counting', '')
                echo "Build завершен за ${duration}"
            }
        }
        success {
            echo 'Pipeline успешно завершен!'
        }
        failure {
            echo 'Pipeline завершился с ошибкой!'
        }
    }
}