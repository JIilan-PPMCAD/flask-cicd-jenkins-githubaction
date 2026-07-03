# Student Registration System & Dual CI/CD Platform

A robust, enterprise-grade **Flask** web application designed to manage student registration records. The project features a comprehensive dual-pipeline infrastructure using **Jenkins** and **GitHub Actions** for multi-stage continuous validation, isolated unit testing, background execution controls, and email-based operational diagnostics.

---

## 🛠️ Tech Stack & Features

*   **Core Application Framework:** Python 3, Flask, Jinja2 Templates, Bootstrap 5.
*   **Database Management System:** MongoDB via `Flask-PyMongo` and `bson`.
*   **Isolated Testing Layer:** In-memory automation database simulation via `mongomock`.
*   **Jenkins CI/CD Infrastructure:** Pipeline Workspace Engine, GitHub Webhooks, Zoho Mail SMTP integrations.
*   **GitHub Actions CI/CD Layer:** Native Linux runner workflows, encrypted repository secrets, SSH multi-port deployment tracking.

---

## 🚀 Unified Pipeline Architecture Workflow

1.  **Developer Push:** Code changes or formal version tags are pushed to the remote repository.
2.  **Jenkins Automation Path:** 
    *   GitHub webhooks trigger automated pipeline builds.
    *   Creates an isolated virtual environment and resolves dependencies.
    *   Executes mock testing sweeps.
    *   Deploys updates cleanly and fires Zoho Mail alerting statuses.
3.  **GitHub Actions Automation Path:** 
    *   Pushes to the `stage` branch deploy to an isolated staging workspace path over port 8001.
    *   Pushes of semantic version tags (`v*`) isolate and execute a production workspace layout over port 8002.

---

## 🔧 Jenkins CI/CD Infrastructure Setup & Monitoring

### 1. Platform Infrastructure & Core Dashboards
Our primary automation server is hosted on an AWS Ubuntu EC2 node, channeling incoming development triggers using a live Jenkins workspace project tracking dashboard view.

![Jenkins Core Pipeline Dashboard Overview](Screenshots/Jenkins-CICD/Pipelen-Overview.png)
![Active AWS EC2 Hosting Node Footprint](Screenshots/Jenkins-CICD/ec2-jenkins.png)

### 2. Pipeline Webhooks & Execution Log Analytics
Commits trigger instant platform runs, running unit tests and outputting verification records cleanly into the master log view.

![Automated Webhook Sync Rules on GitHub Portal](Screenshots/Jenkins-CICD/webhook-jenkins-cicdjob.png)
![Webhook Trigger Step Ingestion Handshake Metrics](Screenshots/Jenkins-CICD/Jenkins-pipelinejob-triggered-onpush.png)
![Successful Build Ingestion Verification Tracker Node Logs](Screenshots/Jenkins-CICD/Jenkins-pipelinejob-triggered-onpush-suceess.png)
![Jenkins Multi-Stage Status Monitor Dashboard Layout](Screenshots/Jenkins-CICD/Job-statges.png)
![Console Build History Complete Log Dump Output](Screenshots/Jenkins-CICD/Jenkins-pipelinejob-console-log.png)

---

## 📧 Jenkins Automated Mail Alerts Configuration

To bypass traditional cloud port filtering and establish instant failure visibility, automated pipeline communications navigate safely via an encrypted Zoho SMTP relay channel using an authorized App Password configuration. If a build breaks, the pipeline attaches compressed operational log diagnostics (`flask_app.log`) directly to the outgoing delivery queue.

### Global SMTP Integration & Zoho Setup
*   **SMTP Server Target Address:** `smtp.zoho.in`
*   **Secure Routing Port:** `465` (SSL Active)
*   **System Identity Header / From:** `jilanshaik20@zohomail.in`

![Extended Email Parameter Adjustments](Screenshots/Jenkins-CICD/mail-config-jenkins.png)
![Secure Credential Configuration and SSL Layer Verification Mapping](Screenshots/Jenkins-CICD/mail-setup-test-config.png)
![Zoho Secure Portal App Password Token Authorization Generation](Screenshots/Jenkins-CICD/zohomail-app-password.png)
![Zoho Delivery Queue Extended Mail Attachment Delivery Receipt](Screenshots/Jenkins-CICD/Suceess_failer_mail_alerts.png)

---

## 🤖 GitHub Actions Pipeline Monitoring

This secondary CI/CD infrastructure manages branch isolation and executes standalone validation parameters without causing port collisions on the hosting EC2 instance.

### 1. Workflow Security & Environment Branching
Infrastructure configuration addresses are protected via GitHub Encrypted Secrets, enabling automated environment routing based on branch metrics.

![Configured GitHub Actions Pipeline Secrets](Screenshots/GitHub-Actions/github-action-secrets.png)
![GitHub Repository Branch Networking Model](Screenshots/GitHub-Actions/github-branhes.png)

### 2. Continuous Integration & Unit Testing Logs
The pipeline builds an isolated execution matrix layer for each push, running dependency validation steps and your `pytest` suite in parallel.

![Automated pip Install Dependencies Step Logs](Screenshots/GitHub-Actions/install-dependencies.png)
![Isolated Pytest Verification Test Suite Output](Screenshots/GitHub-Actions/Run-Test-suite.png)

### 3. Continuous Deployment & Releases Dashboard
When changes land on the `stage` branch, the app deploys to the staging server over port 8001. Pushing formal version tags triggers a separate production environment deployment tracking thread running on port 8002.

![Staging and Production Pipeline Deployment History Status](Screenshots/GitHub-Actions/Deployement_dashboard.png)
![Repository Release Pinned Tags Track Logs](Screenshots/GitHub-Actions/Tags.png)
![Production Tag Packages Delivery Status Dashboard](Screenshots/GitHub-Actions/Releases.png)

---

## 💻 Manual Setup & Configurations

### Local Execution Guide
```bash
# Clone the verified repository
git clone https://github.com
cd flask-cicd-jenkins-githubaction

# Create an isolated python context layer
python3 -m venv venv
source venv/bin/activate

# Resolve dependencies
pip install -r requirements.txt
pip install mongomock

# Launch the app
python3 app.py
```

### Runtime Environment Parameters (`.env`)
```env
MONGO_URI='mongodb://localhost:27017/student_db'
SECRET_KEY='jenkins_automation_secret_key_proof'
FLASK_ENV='staging'
```
