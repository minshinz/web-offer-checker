# Web Offer Checker

This script automatically checks a specific website for a particular offer and alerts you when it's available.

## Prerequisites

Before running the script, you need to set up your environment. Follow these steps:

1. **Install Python**
   - macOS usually comes with Python pre-installed. To check, open Terminal and type:
     ```
     python3 --version
     ```
   - If Python is not installed, download and install it from [python.org](https://www.python.org/downloads/).

2. **Install pip (Python package installer)**
   - pip usually comes with Python. To check if it's installed, run:
     ```
     pip3 --version
     ```
   - If pip is not installed, follow the instructions [here](https://pip.pypa.io/en/stable/installation/).

3. **Install Selenium**
   - Open Terminal and run:
     ```
     pip3 install selenium
     ```

4. **Install ChromeDriver**
   - First, check your Chrome version by going to Chrome menu > About Google Chrome.
   - Download the matching ChromeDriver version from [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads).
   - Unzip the downloaded file.
   - Move the `chromedriver` executable to `/usr/local/bin`:
     ```
     sudo mv ~/Downloads/chromedriver /usr/local/bin/
     ```
   - Make it executable:
     ```
     sudo chmod +x /usr/local/bin/chromedriver
     ```

## Running the Script

1. Save the Python script to a file, e.g., `offer_checker.py`.

2. Open Terminal and navigate to the directory containing the script: `cd /path/to/script/directory`

3. Run the script:

4. The script will open Chrome windows and check for the offer. When found, it will play a sound and attempt to click a specific button.

5. To stop the script, press Ctrl+C in the Terminal window.

## Troubleshooting

- If you get a "chromedriver" cannot be opened because the developer cannot be verified error, go to System Preferences > Security & Privacy, and click "Allow Anyway".

- If you encounter any other issues, ensure all prerequisites are correctly installed and that you're using compatible versions of Python, Selenium, and ChromeDriver.

## Note

This script is for educational purposes only. Be sure to comply with the terms of service and policies of any website you interact with using automated tools.
