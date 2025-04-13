pipeline {
    agent any
    
    stages {
        stage('Setup Python 3.12') {
            steps {
                sh '''#!/bin/bash
                # Проверяем наличие Homebrew
                if ! command -v brew &> /dev/null; then
                    echo "Устанавливаю Homebrew..."
                    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
                    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> $HOME/.zshrc
                    source $HOME/.zshrc
                fi

                # Устанавливаем Python 3.12
                brew install python@3.12
                brew link --overwrite python@3.12 --force

                # Проверяем установку
                /opt/homebrew/opt/python@3.12/bin/python3.12 --version
                '''
            }
        }
    stage('Run Bot') {
            steps {
                sh '''
                # Активация виртуального окружения (если используется)
                python3 -m venv myenv
                source myenv/bin/activate
                
                # Запуск бота с логированием
                nohup python3 -m bot > bot.log 2>&1 &
                echo "Бот запущен! Логи в bot.log"
                '''
            }
        }
    }
}