import random
import string


class Keylogger:
    def __init__(self, file_name):
        self.file_name = file_name
        self.current_word = ''

    def start(self):
        self.current_word = self.generate_random_chars(5)

    def stop(self):
        with open(self.file_name, 'a') as f:
            f.write(self.current_word + '\n')

    def generate_random_chars(self, num_chars):
        return ''.join(random.choice(string.ascii_uppercase) for _ in range(num_chars))