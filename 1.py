import os
import subprocess


class _Helper:
    @staticmethod
    def _linux_cmd(cmd: str):
        process = subprocess.Popen(cmd, shell=True)
        status = os.waitpid(process.pid, 0)[1]
        print("执行状态", status)


if __name__ == '__main__':
    _Helper._linux_cmd("ls")
