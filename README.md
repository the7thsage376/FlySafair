# FlySafair

## How to run tests

These instructions assume you're on Windows using PowerShell and want to run the existing Selenium script (`flight_booking.py`). This guide keeps things simple (no pytest required).

1. Create and activate a Python virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install required packages (Selenium and the Chrome WebDriver manager if you prefer to manage drivers manually):

```powershell
pip install selenium
# Optionally install webdriver-manager to auto-download drivers:
pip install webdriver-manager
```

3. Ensure Chrome is installed and matches the ChromeDriver version. If using `webdriver-manager`, the driver will be handled automatically by your script.

4. Run the test script:

```powershell
python flight_booking.py
```

Notes:
- If you see errors about the driver, try installing `webdriver-manager` and updating the script to use it, or download the ChromeDriver that matches your Chrome version and place it on your PATH.
- Avoid committing real passenger data; use test data only.

# FlySafair Automation Suite

This project is a Selenium-powered automation suite that simulates real-world flight booking on FlySafair — built for clarity, scalability, and recruiter visibility.

---

## Getting Started

Follow these steps to set up and run the automation script:

### Prerequisites
- Python 3.x installed
- Chrome browser installed
- ChromeDriver matching your Chrome version

### Installation and Execution

1. Setup a virtual environment
-  `python -m venv venv`
- `venv/Scripts/activate`

2. Install Selenium into environment
- `pip install selenium`

3. Run the script
- `python flight_booking.py`

---

### Tools and programming languages used: <br>

- Selenium webdriver with Python