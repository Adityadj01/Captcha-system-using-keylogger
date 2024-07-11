# Captcha-system-using-keylogger
# AI Keylogger Flask Application

This Flask application utilizes a keylogger module to capture the user's keystrokes while entering the captcha code. It validates the accuracy of the entered captcha code against the one saved in the keylogger's log file. The Flask application serves as a template for studying and understanding user input patterns.

Here is an overview of the application's functionality:

1. Generate a random 5-character captcha code.
2. Start the keylogger and log the user's keystrokes  as they enter the captcha code.
3. Compare the user's input with the correct captcha code.
4. Display a success or failure message based on the user's input.
5. Stop the keylogger after the user's input has been processed.

Note that this application is intended for educational purposes only and should not be used to invade the privacy of others.

You can clone the repository and run the application using the following command:

```bash
git clone https://github.com/username/flask-keylogger.git
cd flask-keylogger
python app.py
