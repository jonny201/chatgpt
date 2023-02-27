import tkinter as tk
import json
import socket

class TCPClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def send_message(self, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.host, self.port))
            sock.sendall(message.encode())
            response = sock.recv(1024).decode()
            return response

class DialogBox:
    def __init__(self, master):
        self.master = master
        self.master.title("TCP Client")

        # Create session window
        self.session_window = tk.Text(self.master)
        self.session_window.pack(side=tk.LEFT)

        # Create config window
        self.config_window = tk.Frame(self.master)
        self.config_window.pack(side=tk.RIGHT)

        self.model_label = tk.Label(self.config_window, text="Model:")
        self.model_label.pack()
        self.model_entry = tk.Entry(self.config_window)
        self.model_entry.pack()

        self.temperature_label = tk.Label(self.config_window, text="Temperature:")
        self.temperature_label.pack()
        self.temperature_entry = tk.Entry(self.config_window)
        self.temperature_entry.pack()

        self.max_tokens_label = tk.Label(self.config_window, text="Max Tokens:")
        self.max_tokens_label.pack()
        self.max_tokens_entry = tk.Entry(self.config_window)
        self.max_tokens_entry.pack()

        self.top_p_label = tk.Label(self.config_window, text="Top P:")
        self.top_p_label.pack()
        self.top_p_entry = tk.Entry(self.config_window)
        self.top_p_entry.pack()

        self.frequency_penalty_label = tk.Label(self.config_window, text="Frequency Penalty:")
        self.frequency_penalty_label.pack()
        self.frequency_penalty_entry = tk.Entry(self.config_window)
        self.frequency_penalty_entry.pack()

        self.presence_penalty_label = tk.Label(self.config_window, text="Presence Penalty:")
        self.presence_penalty_label.pack()
        self.presence_penalty_entry = tk.Entry(self.config_window)
        self.presence_penalty_entry.pack()

        self.stop_label = tk.Label(self.config_window, text="Stop:")
        self.stop_label.pack()
        self.stop_entry = tk.Entry(self.config_window)
        self.stop_entry.pack()

        self.submit_button = tk.Button(self.config_window, text="Submit", command=self.submit)
        self.submit_button.pack()

    def submit(self):
        params = {
            "model": self.model_entry.get(),
            "temperature": float(self.temperature_entry.get()),
            "max_tokens": int(self.max_tokens_entry.get()),
            "top_p": float(self.top_p_entry.get()),
            "frequency_penalty": float(self.frequency_penalty_entry.get()),
            "presence_penalty": float(self.presence_penalty_entry.get()),
            "stop": [self.stop_entry.get()]
        }
        message = json.dumps(params)
        client = TCPClient('localhost', 12345)
        response = client.send_message(message)
        self.session_window.insert(tk.END, "Sent: " + message + "\n")
        self.session_window.insert(tk.END, "Received: " + response + "\n")

if __name__ == '__main__':
    root = tk.Tk()
    dialog = DialogBox(root)
    root.mainloop()
