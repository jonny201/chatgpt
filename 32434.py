import tkinter as tk
import json
import socket


class TCPClientDialog:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("TCP Client Dialog")

        # create widgets
        tk.Label(self.root, text="Model:").grid(row=0, column=0, sticky=tk.W)
        self.model_entry = tk.Entry(self.root)
        self.model_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Temperature:").grid(row=1, column=0, sticky=tk.W)
        self.temperature_entry = tk.Entry(self.root)
        self.temperature_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Max Tokens:").grid(row=2, column=0, sticky=tk.W)
        self.max_tokens_entry = tk.Entry(self.root)
        self.max_tokens_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Top P:").grid(row=3, column=0, sticky=tk.W)
        self.top_p_entry = tk.Entry(self.root)
        self.top_p_entry.grid(row=3, column=1)

        tk.Label(self.root, text="Frequency Penalty:").grid(row=4, column=0, sticky=tk.W)
        self.frequency_penalty_entry = tk.Entry(self.root)
        self.frequency_penalty_entry.grid(row=4, column=1)

        tk.Label(self.root, text="Presence Penalty:").grid(row=5, column=0, sticky=tk.W)
        self.presence_penalty_entry = tk.Entry(self.root)
        self.presence_penalty_entry.grid(row=5, column=1)

        tk.Label(self.root, text="Stop:").grid(row=6, column=0, sticky=tk.W)
        self.stop_entry = tk.Entry(self.root)
        self.stop_entry.grid(row=6, column=1)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        self.submit_button.grid(row=7, column=0, columnspan=2)

    def submit(self):
        # create JSON data
        data = {
            "model": self.model_entry.get(),
            "temperature": float(self.temperature_entry.get()),
            "max_tokens": int(self.max_tokens_entry.get()),
            "top_p": float(self.top_p_entry.get()),
            "frequency_penalty": float(self.frequency_penalty_entry.get()),
            "presence_penalty": float(self.presence_penalty_entry.get()),
            "stop": [self.stop_entry.get()]
        }

        # send JSON data to TCP server
        HOST = 'localhost'
        PORT = 5000
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(json.dumps(data).encode())
            response = s.recv(1024)

        # show response in a dialog
        response_dialog = tk.Toplevel(self.root)
        response_dialog.title("Response")
        tk.Label(response_dialog, text=response.decode()).pack()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    dialog = TCPClientDialog()
    dialog.run()
