def seconds_to_mm_ss(time):
    minutes = time // 60
    seconds = time % 60
    return str(minutes) + ':' + "%02d" % seconds
