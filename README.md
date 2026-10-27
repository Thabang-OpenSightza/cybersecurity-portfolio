# cybersecurity-portfolio

WTC-G9BEDDDP

# DevSecOps Shift-Left Pipeline: Automated Security Scanning

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-2088FF?logo=github-actions&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

## Executive Summary
This project demonstrates a "Shift-Left" DevSecOps pipeline designed to catch security vulnerabilities before they reach production. Using GitHub Actions, the pipeline automatically executes Static Application Security Testing (SAST) and secrets detection on every code push. If critical flaws (such as hardcoded credentials or SQL injection vectors) are detected, the build fails, preventing insecure code from being merged.

## Proof of Concept & Evidence

**1. Pipeline Catching Vulnerabilities (Intentional Failure):**
*(Screenshot showing the Red X in GitHub Actions when Gitleaks/Bandit detected the hardcoded secret and SQL injection)*

**2. Pipeline Passing After Remediation:**
*(Screenshot showing the Green Checkmark after fixing the code to use environment variables and parameterized queries)*

**3. Secure Code Implementation:**
*(Screenshot of `src/app.py` showing `os.environ.get` and secure SQL query practices)*

## Architecture Diagram

```mermaid
graph LR
    classDef dev fill:#ffffff,stroke:#232F3E,stroke-width:2px,color:#000000;
    classDef github fill:#2088FF,stroke:#232F3E,stroke-width:2px,color:#ffffff;
    classDef scanner fill:#D13212,stroke:#232F3E,stroke-width:2px,color:#ffffff;
    classDef deploy fill:#2ECC71,stroke:#232F3E,stroke-width:2px,color:#ffffff;

    Dev(["Developer<br/>(Git Push)"]):::dev
    
    subgraph GitHub Actions Pipeline
        direction TB
        Gitleaks(["Gitleaks<br/>(Secrets Detection)"]):::scanner
        Semgrep(["Semgrep<br/>(SAST / Code Flaws)"]):::scanner
    end

    Deploy(["Deploy to Production"]):::deploy
    Block(["Build Failed<br/>(Block Merge)"]):::scanner

    Dev ==>|1. Push Code| GitHub
    GitHub -.->|2. Trigger CI/CD| Gitleaks
    GitHub -.->|2. Trigger CI/CD| Semgrep
    
    Gitleaks ==>|3. Pass| Deploy
    Semgrep ==>|3. Pass| Deploy
    Gitleaks -.->|4. Fail| Block
    Semgrep -.->|4. Fail| Block

