import time


class Logger:
    def __init__(self, log_file='logs.txt'):
        self.log_file = log_file

    def log(self, *messages):
        with open(self.log_file, 'a') as f:
            date = time.strftime('%Y-%m-%d %H:%M:%S')
            f.write(f'[{date}] {str(messages)}\n')

    def clear(self):
        with open(self.log_file, 'w') as f:
            f.write('')
