# Based on source from this thread https://stackoverflow.com/questions/18499497/how-to-process-sigterm-signal-gracefully

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Run this program.
# Find the Python program's pid (first column) ps -au | grep handleSIG
# kill -s TERM pid

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import time


class GracefulKiller:
    kill_now = False

    def __init__(self):
        pass
        # signal.signal(signal.SIGINT, self.exit_gracefully)
        # signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, *args):
        self.kill_now = True


if __name__ == '__main__':
    try:
        killer = GracefulKiller()
        while not killer.kill_now:
            time.sleep(1)
            print("doing something in a loop ...")

        print("End of the program. I was killed gracefully :)")  # With above signal, this line will be printed.
    finally:
        # If signal lines are commented out, SIGTERM won't trigger this line. Program quits immediately.
        print("finally called.")
