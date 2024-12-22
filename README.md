# FormBot Demonstrator

## Overview
**FormBot Demonstrator** is an educational project that showcases the functionality of automated bots for interacting with online forms. This tool demonstrates how bots can:

- Extract form structures dynamically.
- Autofill input fields with predefined values.
- Select options from radio buttons, checkboxes, and dropdown lists.
- Programmatically submit forms.

The project serves as a practical demonstration of bot behavior and mechanics, providing insights into how automation can be used for testing, research, and educational purposes.

---

## Features

- **Dynamic Form Parsing:** Automatically identifies and processes input fields, radio buttons, checkboxes, and dropdown lists.
- **Autofill Capability:** Populates form fields with sample data.
- **Multi-Browser Support:** Compatible with Chrome, Firefox, and Edge using Selenium WebDriver.
- **Repeated Submissions:** Loops through the process multiple times for testing purposes.
- **Actionable Logging:** Logs key actions and errors during execution for transparency.

---

## Use Cases

- **Educational Purposes:** Learn how bots interact with web forms programmatically.
- **Automation Testing:** Test web form functionality using automated scripts.
- **Demonstration Tool:** Showcase the potential of bots in filling and submitting forms.

---

## Requirements

- Python 3.8+
- Selenium WebDriver
- WebDriver Manager libraries:
  - `webdriver-manager`
- Supported browsers:
  - Google Chrome
  - Mozilla Firefox
  - Microsoft Edge

Install the required Python packages using:
```bash
pip install selenium webdriver-manager
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/formbot-demonstrator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd formbot-demonstrator
   ```
3. Configure your preferred browser in the script by setting the `My_Browser` variable to `'chrome'`, `'firefox'`, or `'edge'`.

---

## Usage

1. Open the script file and specify the target Google Form URL in the `Google_Form_URL` variable.
2. Run the script:
   ```bash
   python formbot_demonstrator.py
   ```
3. Observe the bot as it:
   - Parses the form structure.
   - Autofills fields with sample data.
   - Selects options and submits the form.

---

## Ethical Disclaimer

This project is intended for educational and demonstration purposes only. Do not use this tool for unethical activities, including spamming, unauthorized data collection, or violating the terms of service of any website. Always seek proper authorization before using automation on web platforms.

---

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

