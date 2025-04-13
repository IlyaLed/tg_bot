pipeline {
    agent any

    stages {
        stage('Install Python 3.12') {
            steps {
                sh '''
                # Установка Homebrew (если его нет)
                if ! command -v brew >/dev/null 2>&1; then
                    echo "Устанавливаю Homebrew..."
                    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
                    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
                    source ~/.zshrc
                fi

                # Установка Python 3.12
                brew install python@3.12
                brew link --overwrite python@3.12

                # Проверка установки
                /opt/homebrew/opt/python@3.12/bin/python3.12 --version
                '''
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                # Используем абсолютный путь к Python 3.12
                /opt/homebrew/opt/python@3.12/bin/python3.12 -m pip install --upgrade pip
                /opt/homebrew/opt/python@3.12/bin/python3.12 -m pip install aiogram python-dotenv
                '''
            }
        }
    }
}