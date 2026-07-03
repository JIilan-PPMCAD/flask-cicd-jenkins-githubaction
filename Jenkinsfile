pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        PYTHON_BIN = "${WORKSPACE}/${VENV_DIR}/bin/python"
        PIP_BIN = "${WORKSPACE}/${VENV_DIR}/bin/pip"
        PYTEST_BIN = "${WORKSPACE}/${VENV_DIR}/bin/pytest"
        
        MONGO_URI = "mongodb://localhost:27017/student_db"
        SECRET_KEY = "jenkins_automation_secret_key_proof"
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
                    
                    # Ensure mongomock is present for the isolated execution environment
                    ${PIP_BIN} install mongomock
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running Unit Tests...'
                sh '''
                    if [ -f test_app.py ]; then
                        # Clear wrapper dependencies to ensure real failure visibility
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
                    # Safely stops old app processes running on port 8000
                    fuser -k 8000/tcp || true
                    
                    # Generates configuration parameters inside runtime path
                    echo "MONGO_URI='mongodb://localhost:27017/student_db'" > .env
                    echo "SECRET_KEY='jenkins_automation_secret_key_proof'" >> .env
                    
                    # FIX: Inject environment context flag to pivot the live app into mock-database execution mode
                    export FLASK_ENV=staging
                    
                    # Launches flask app securely in background
                    nohup ${PYTHON_BIN} app.py > flask_app.log 2>&1 &
                    sleep 5
                    
                    # Prints runtime startup log directly to Jenkins Console if execution fails
                    echo "--- Current Application Runtime Log Output ---"
                    cat flask_app.log || true
                    echo "----------------------------------------------"
                    
                    # Verifies structural response profile via curl health check
                    curl -f http://localhost:8000 || exit 1
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check build logs.'
        }
    }
}
