import subprocess
import threading
import queue


SENTINEL = "__KD_DONE__"


class KdExecutor:
    def __init__(self, path="kd.exe", dump_file=None):
        cmd = [path]
        if dump_file:
            cmd += ["-z", dump_file]

        self.proc = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
        self.queue = queue.Queue()
        threading.Thread(target=self._read_output, daemon=True).start()

    def _read_output(self):
        for line in self.proc.stdout:
            self.queue.put(line)

    def send_command(self, command, wait_prompt=True, timeout=300):
        self.proc.stdin.write(command + "\n" + f".echo {SENTINEL}\n")
        self.proc.stdin.flush()

        output_lines = []
        while True:
            try:
                line = self.queue.get(timeout=timeout)

            except queue.Empty:
                break
            if wait_prompt and SENTINEL in line:
                break
            output_lines.append(line)

        return "".join(output_lines)

    def close(self):
        self.proc.terminate()


if __name__ == "__main__":
    kd = KdExecutor(
        path=r"C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\kd.exe",
        dump_file=r"D:\BaiduNetdiskDownload\开发样本_0x133 0 Realtek WLAN NDIS OID\MEMORY.DMP",
    )
    result = kd.send_command("!analyze -v")
    print(result)
    kd.close()
