# Captcha-system-using-keylogger
# AI Keylogger Flask Application

This Flask application uses a keylogger module to record the keystrokes of the user when they enter the captcha code. It checks the correctness of the captcha code entered by the user against the one stored in the keylogger's log file. The Flask application serves as an AI model that can be used to analyze and learn from user input patterns.

Here is an overview of the application's functionality:

1. Generate a random 5-character captcha code.
2. Start the keylogger and log the keystrokes of the user as they enter the captcha code.
3. Compare the user's input with the correct captcha code.
4. Display a success or failure message based on the user's input.
5. Stop the keylogger after the user's input has been processed.

Please note that this application is intended for educational purposes only and should not be used to invade the privacy of others.

You can clone the repository and run the application using the following command:

```bash
git clone https://github.com/username/flask-keylogger.git
cd flask-keylogger
python app.py