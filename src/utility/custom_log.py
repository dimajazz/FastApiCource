from datetime import datetime


def log(tag='', message=''):
    current_time = datetime.now()

    with open('logs/log.txt', 'w+') as log_file:
        log_file.write(
            f'{current_time.year}-{current_time.month}-{current_time.day} {current_time.hour}:{current_time.minute}:{current_time.second} => ')
        log_file.write(f'{tag}: {message}\n')
