pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.12'
        BOT_TOKEN = credentials('API_TOKEN')
        PIP_CACHE_DIR = '.pip_cache'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    extensions: [[
                        $class: 'CloneOption',
                        shallow: true,  // Неполный клон для ускорения
                        depth: 1
                    ]],
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[url: 'https://github.com/ilyaLed/tg_bot']]
                ])
            }
        }

        stage('Setup') {
            steps {
                sh """
                python${env.PYTHON_VERSION} --version
                python${env.PYTHON_VERSION} -m pip install --upgrade pip
                python${env.PYTHON_VERSION} -m pip install --user --cache-dir ${env.PIP_CACHE_DIR} aiogram==3.0.0b7 python-dotenv loguru
                """
            }
        }

        stage('Verify') {
            steps {
                script {
                    // Проверка, что бот действительно запускается
                    def botStart = sh(
                        script: "timeout 5 python${env.PYTHON_VERSION} -m bot || echo 'Bot exited'",
                        returnStatus: true
                    )
                    if (botStart != 143) {  // 143 = timeout
                        error("Bot failed to run properly")
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
            script {
                def duration = currentBuild.durationString.replace(' and counting', '')
                echo "Build stats:"
                echo "- Total: ${duration}"
                echo "- Checkout: ${currentBuild.rawBuild.getAction(org.jenkinsci.plugins.workflow.job.views.FlowDurationAction.class).getStepDurations().find { it.displayName == 'Checkout' }?.durationString ?: 'N/A'}"
            }
        }
    }
}