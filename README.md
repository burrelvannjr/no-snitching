# README: I hate people who cross picket lines and I hate snitches more

## Description
This project is a Python-based automation script using Selenium WebDriver. Its designed to provide fake, believable data to csulbs class snitchy thing

## Prerequisites
To run this script, you need Python installed on your system, along with the Selenium package and the appropriate WebDriver for your browser.
Use a vpn, or some way to obfuscate your ip, otherwise have fun filling out a million captchas. I like nord :)

if you encounter a captcha there is enough time to fill it out. if you want more time, adjust the sleeo value at line 72 to be longer than 10 (seconds)

once you solve a captcha it should let you submit a few more times, if you keep getting them tho stop the script, change ip and restart


### Required Software & Drivers
1. **Python**: The script is written in Python, so you need Python installed.
2. **Selenium**: A browser automation framework.
3. **WebDriver**: An executable file that allows Selenium to interface with a browser. You need the correct WebDriver for your browser (e.g., ChromeDriver for Google Chrome).

## Installation

### Installing Python
- **Windows/macOS/Linux**: Download and install Python from the [official website](https://www.python.org/downloads/).

### Installing Selenium
- After installing Python, install Selenium by running the following command in your terminal or command prompt:
  ```shell
  pip install selenium
  ```

### Installing WebDriver
- The script uses `webdriver_manager`, which automatically downloads and installs the correct WebDriver for your browser.
- Install `webdriver_manager` by running:
  ```shell
  pip install webdriver_manager
  ```

## Script Usage

### Input Files
The script requires the following text files in the same directory as the script.
- `first-names.txt`: First names
- `last-names.txt`: Last names
- `courses.txt`: Course names
- `professors.txt`: Professor names
- `dates.txt`: random times for classes

### Running the Script
1. Open your terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the script by executing:
   ```shell
   python3 Spam.py
   ```
   or
   ```shell
   python Spam.py
   ```
   

### Script Behavior
1. The script initializes the Selenium WebDriver and opens the specified URL.
2. It reads a random line from each of the input files.
3. It fills out the form on the page using the randomly selected data.
4. After submitting the form, it waits for the user to complete any CAPTCHAs or additional verification.
5. Once the user signals completion (by pressing Enter), it closes the browser and restarts the process.

### Note
- The first time the script submits the form, it will pause and wait for you to manually solve a CAPTCHA or perform any required human verification. Press Enter in the terminal after you've completed this step. 

## Troubleshooting
- If the script isn't working as expected, ensure that:
  - All input files exist and are formatted correctly.
  - The IDs used in the script match the actual IDs of the form elements.
  - The WebDriver is compatible with your browser version.
  - reach out to me for help uhohspaghettioo@proton.me

## Contributions


Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request on the project's repository.
