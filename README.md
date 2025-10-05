🧪 The Internet Automation Test Suite
Project Name: The Internet Automation Suite
Author: MD Rifat Mahmud
Date: October 2025
Framework: Python + Selenium + Pytest
Reporting: Pytest HTML Report (report.html)

📘 Overview
This project automates five critical user interface scenarios from The Internet, a popular testing practice site.
The purpose is to demonstrate manual-to-automation test conversion, framework structure, and evidence-based reporting.

🚀 Test Scenarios Covered
#
Scenario
File
Description
1️⃣
Form Authentication
test_auth.py
Valid & invalid login attempts
2️⃣
Dropdown Selection
test_dropdown.py
Selecting options from a dropdown list
3️⃣
File Upload
test_file_upload.py
Uploading a file and verifying upload success
4️⃣
JavaScript Alerts
test_alerts.py
Handling alerts and confirm popups
5️⃣
Broken Images
test_broken_images.py
Detecting missing/broken image links

🏗️ Project Structure
the-internet-suites/
│
├── helpers/                 # Utility functions (e.g., config loader)
│   └── utils.py
│
├── pages/                   # Page Object Model classes
│   ├── base_page.py
│   ├── home_page.py
│   ├── auth_page.py
│   ├── dropdown_page.py
│   └── ...
│
├── tests/                   # Test scripts for each scenario
│   ├── test_auth.py
│   ├── test_dropdown.py
│   ├── test_file_upload.py
│   ├── test_alerts.py
│   └── test_broken_images.py
│
├── config.json              # Base URL and driver configuration
├── report.html              # Pytest HTML execution report
├── requirements.txt         # Project dependencies
└── README.md                # Documentation

⚙️ Setup & Execution
1️⃣ Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Run all tests with HTML report
pytest tests/ --html=report.html --self-contained-html
4️⃣ View the report
After execution, open report.html in your browser.

📹 Evidence of Execution
A full screen recording (.mkv) demonstrates the test execution process.
It shows environment setup, test run via Pytest, and HTML report generation.

🧠 Key Highlights
    • Page Object Model (POM) structure for reusability
    • Independent and modular test scripts
    • Clean and maintainable code
    • HTML reporting with time-stamped execution results
    • Comprehensive coverage of five diverse UI behaviors

🧾 Test Report Summary (Example)
Result
Count
✅ Passed
5
❌ Failed
0
⚠️ Skipped
0
⏱️ Duration
~2 mins

📈 Future Enhancements
    • Integrate with GitHub Actions for CI/CD testing
    • Add parallel execution using pytest-xdist
    • Capture screenshots on test failures
    • Support multiple browsers (Chrome, Firefox)

🧑‍💻 Author
MD Rifat Mahmud
📧 [rifatmahmud19040@gmail.com]
🔗 GitHub: mdrifatmahmud
# The Internet Suites – Automated Test Project
