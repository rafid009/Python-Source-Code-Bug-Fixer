import time

def get_current_time_in_millis():
    return int(time.time() * 1000)

def to_string_list(code_list):
    return [str(c) for c in code_list]