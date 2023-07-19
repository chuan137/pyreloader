#!/usr/bin/env python3
import os
import signal
import sys
from time import sleep


class Reloader:

    def __init__(self, command) -> None:
        self.command = command
        self.child_pid = None
        self.start_child()

    def __call__(self, _signo, _stack_frame):
        print("Reloading...")
        if self.child_pid:
            os.kill(self.child_pid, signal.SIGTERM)
        self.start_child()

    def start_child(self):
        """start child process running the command"""
        self.child_pid = os.fork()
        if self.child_pid == 0:
            os.execv(sys.executable, [sys.executable] + self.command)

    def kill_process(self, _signo, _stack_frame):
        """kill child process"""
        print("Killing process...")
        if self.child_pid:
            os.kill(self.child_pid, signal.SIGTERM)
            self.child_pid = None


def main():
    if len(sys.argv) < 2:
        print("Usage: %s <command>" % sys.argv[0])
        sys.exit(1)
    command = sys.argv[1:]

    # check script is in current path
    if not os.path.exists(command[0]):
        command[0] = os.path.dirname(sys.executable) + "/" + command[0]

    reloader = Reloader(command)
    signal.signal(signal.SIGHUP, reloader)
    signal.signal(signal.SIGTERM, reloader.kill_process)

    while reloader.child_pid:
        try:
            sleep(1)
        except KeyboardInterrupt:
            reloader.kill_process(None, None)
            sys.exit(0)


if __name__ == "__main__":
    main()
