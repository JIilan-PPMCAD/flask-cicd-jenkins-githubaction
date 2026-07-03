pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        PYTHON_BIN = "${WORKSPACE}/${VENV_DIR}/bin/python"
        PIP_BIN = "${WORKSPACE}/${VENV_DIR}/bin/pip"
        PYTEST_BIN = "${WORKSPACE}/${VENV_DIR}/bin/pytest"
        
        MONGO_URI = "mongodb://localhost:27017/student_db"
        SECRET_KEY = "jenkins_automation_secret_key_proof"
        JENKINS_NODE_COOKIE = 'dontKillMe'
        
        // RECIPIENT SETUP: Define who should receive your build notifications
        NOTIFICATION_EMAIL = "your-email@example.com"
    }

    triggers {
        githubPush()
    }

    stages {
        stage('Build') {
            steps {
                echo 'Setting up Python Virtual Environment and Installing Dependencies...'
                sh '''
                    python3 -m venv ${VENV_DIR}
                    ${PIP_BIN} install --upgrade pip
                    if [ -f requirements.txt ]; then
                        ${PIP_BIN} install -r requirements.txt
                    else
                        ${PIP_BIN} install flask pytest python-dotenv flask-pymongo certifi
                    fi
                    ${PIP_BIN} install mongomock
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running Unit Tests...'
                sh '''
                    if [ -f test_app.py ]; then
                        ${PYTEST_BIN} test_app.py
                    else
                        echo "No test file found, skipping suite..."
                        exit 1
                    fi
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Application to Staging Port 8000...'
                sh '''
                    fuser -k 8000/tcp || true
                    echo "MONGO_URI='mongodb://localhost:27017/student_db'" > .env
                    echo "SECRET_KEY='jenkins_automation_secret_key_proof'" >> .env
                    export FLASK_ENV=staging
                    
                    nohup ${PYTHON_BIN} app.py > flask_app.log 2>&1 &
                    sleep 5
                    
                    echo "--- Current Application Runtime Log Output ---"
                    cat flask_app.log || true
                    echo "----------------------------------------------"
                    
                    curl -f http://localhost:8000 || exit 1
                '''
            }
        }
    }

    // UPDATED POST BLOCK FOR EMAIL ALERTS
    post {
        success {
            echo 'Pipeline completed successfully!'
            mail to: "${env.NOTIFICATION_EMAIL}",
                 subject: "SUCCESS: Jenkins Pipeline '${env.JOB_NAME}' (Build #${env.BUILD_ID})",
                 body: "Great news! The pipeline completed successfully.\n\nView the full build details here: ${env.BUILD_URL}"
        }
        failure {
            echo 'Pipeline failed. Check build logs.'
            mail to: "${env.NOTIFICATION_EMAIL}",
                 subject: "FAILURE: Jenkins Pipeline '${env.JOB_NAME}' (Build #${env.BUILD_ID})",
                 body: "Attention required! The build or deployment has failed.\n\nCheck the console logs to debug: ${env.BUILD_URL}"
        }
    }
}
