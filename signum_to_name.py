# Convert signal number to string name

import signal

def signal_numtoname (num):
    name = []
    for key in signal.__dict__.keys():
        if key.startswith("SIG") and getattr(signal, key) == num:
            name.append (key)
    if len(name) == 1:
        return name[0]
    else:
        return str(num)
