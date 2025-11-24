1. Overview
Project Name: VIT Wi-Fi Service Triage Script

Purpose: To automate the initial data collection and provide instant first-level troubleshooting steps for common Wi-Fi connectivity problems faced by VIT Bhopal students.

Technology: Python 3 (CLI-based)

Target Audience: Students of VIT Bhopal.

2. Features
User Identification: Gathers and verifies the user's Name, 10-digit Registration Number, and Batch year.

Credential Verification: Prompts the user to input and verify their provided Username and Password.

Problem Categorization: Allows the user to select from common Wi-Fi issues:

Network problems

Connection failure

Slow speed

Fortinet installation issues

Phone-specific network problems (with device warnings)

Automated Advice: Provides a simple, actionable troubleshooting tip for the selected problem category.

IT Escalation: Directs the user to the CTS office for complex issues.

3. Usage
Prerequisites: Ensure you have Python 3 installed on your system.

Run the Script:

Bash

python VIT wifi.py
Follow Prompts: The script will guide you through entering your details and selecting your issue.

4. Code Structure (High-Level)
The script uses basic Python input/output (input(), print()) and while loops for simple input validation
 (e.g., verifying the Registration Number length and confirmation answers).
 It employs an if-elif-else structure to map the user's problem choice to the corresponding troubleshooting advice.

