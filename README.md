# SecureGrid-ICS-Active-Defense
An AI-powered Intrusion Prevention System (IPS) for Industrial Control Systems that detects False Data Injection Attacks and performs automated self-healing remediation in real-time.
# 🛡️ SecureGrid: AI-Driven ICS Active Defense System

![License](https://img.shields.io/badge/license-MIT-blue.svg) ![Python](https://img.shields.io/badge/python-3.13-yellow.svg) ![Status](https://img.shields.io/badge/status-Prototype-green.svg)

## 📋 Overview
**SecureGrid** is a cybersecurity Senior Project designed to protect **Operational Technology (OT)** and **Industrial Control Systems (ICS)** from cyberattacks.

This system addresses the lack of built-in security in the **Modbus TCP** protocol. It deploys an AI-driven **Intrusion Prevention System (IPS)** that monitors sensor data in real-time. Unlike passive detection systems, SecureGrid features **Automated Remediation**: when a **False Data Injection Attack (FDIA)** is detected (e.g., Stuxnet-style manipulation), the system actively overrides the malicious command and restores the infrastructure to a safe state within milliseconds.

##Key Features
* **Virtual Industrial Plant:** A fully functional simulation of a SCADA environment (PLC & HMI) using Modbus TCP.
* **Hybrid Detection Engine:** Combines **Unsupervised Machine Learning (Isolation Forest)** for anomaly detection with heuristic safety limits.
* **Active Defense (SOAR):** Automatically engages "Self-Healing" protocols to overwrite malicious data and reset turbines to safe operational limits.
* **Real-Time SOC Dashboard:** A Flask-based interface mimicking a National Grid Monitor for visual threat tracking.

##Architecture
The system operates as a "Guardian" sidecar to the critical infrastructure.

