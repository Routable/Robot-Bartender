# Message handling and logger for system output.
# Easily changed to disable test outputs in future.
# Simple print nothing to disable system logging.

import datetime


def sys_log(message):
    print("%s: %s" % (datetime.datetime.now().strftime("%I:%M:%S %p"), message))

