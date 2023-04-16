def seconds_to_mm_ss(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return str(minutes) + ':' + "%02d" % seconds
