pipeline {
    agent any

    parameters {
        booleanParam(name: 'RELEASE', defaultValue: false, description: 'Is this a release version?')
    }
    environment {
        VERSION = "0.0.1"
        RELEASE_VERSION = "D.1"
        VENV_DIR=".venv"
    }
    stages {
        stage('First Stage') {
            steps {
                auditTools()
            }
        }

        stage('Setup Python Environment') {
            steps {
                dir('./python_code') {
                make_venv()
                }
            }
        }


        stage('Unit Tests') {
            steps {
                dir('./python_code') {
                sh 'ls'
                sh '''
                echo "Executing Unit Tests..."
                export PYTHONPATH=$PWD
                .venv/bin/python -m pytest tests/ --junitxml=test-results/results.xml
                '''
                }
            }
        }


        stage('Run Code') {
            steps {
                dir('./python_code') {
                run_code()
                }
            }
        }
    }

    post {
        success {
            sh '''
                if [ "${RELEASE}" = true ]; then
                    echo "Will release"
                else
                    echo "Nothing will be released"
                fi
                '''
            echo 'Everything went great.'
        }
        failure {
            echo 'Woopsie-Daisy!'
        }
        always {
            cleanWs()
        }
    }

}


void auditTools() {
    sh '''
    git version
    python3 --version
    ls
    '''
}

void make_venv() {
    sh '''
        echo "Creating virtual environment..."
        python3 -m venv $VENV_DIR
        $VENV_DIR/bin/pip install --upgrade pip
        $VENV_DIR/bin/pip install -r requirements.txt
        '''
}

void run_code() {
    sh '''
        #!/bin/bash
        set -e  # Exit on erro
        VENV_PATH=".venv/bin/python
        # Ensure virtual environment exists
        if [ ! -x "$VENV_PATH" ]; then
            echo "Virtual environment not found at $VENV_PATH"
            exit 1
        f
        for dir in src/*/; do
            MAIN_FILE="${dir}main.py"
            if [ -f "$MAIN_FILE" ]; then
                echo "Running $MAIN_FILE"
                $VENV_PATH "$MAIN_FILE"
            else
                echo "Skipping $dir: main.py not found"
            fi
        done
        '''
}

