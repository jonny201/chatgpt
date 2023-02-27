import tkinter as tk
import json
import socket


class TCPClientDialog(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("TCP Client Dialog")
        self.geometry("400x300")
        self.model_var = tk.StringVar()
        self.temp_var = tk.StringVar()
        self.max_tokens_var = tk.StringVar()
        self.top_p_var = tk.StringVar()
        self.freq_penalty_var = tk.StringVar()
        self.pres_penalty_var = tk.StringVar()
        self.stop_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Model Entry
        model_label = tk.Label(self, text="Model:")
        model_label.grid(row=0, column=0)
        model_entry = tk.Entry(self, textvariable=self.model_var)
        model_entry.grid(row=0, column=1)

        # Temperature Entry
        temp_label = tk.Label(self, text="Temperature:")
        temp_label.grid(row=1, column=0)
        temp_entry = tk.Entry(self, textvariable=self.temp_var)
        temp_entry.grid(row=1, column=1)

        # Max Tokens Entry
        max_tokens_label = tk.Label(self, text="Max Tokens:")
        max_tokens_label.grid(row=2, column=0)
        max_tokens_entry = tk.Entry(self, textvariable=self.max_tokens_var)
        max_tokens_entry.grid(row=2, column=1)

        # Top P Entry
        top_p_label = tk.Label(self, text="Top P:")
        top_p_label.grid(row=3, column=0)
        top_p_entry = tk.Entry(self, textvariable=self.top_p_var)
        top_p_entry.grid(row=3, column=1)

        # Frequency Penalty Entry
        freq_penalty_label = tk.Label(self, text="Frequency Penalty:")
        freq_penalty_label.grid(row=4, column=0)
        freq_penalty_entry = tk.Entry(self, textvariable=self.freq_penalty_var)
        freq_penalty_entry.grid(row=4, column=1)

        # Presence Penalty Entry
        pres_penalty_label = tk.Label(self, text="Presence Penalty:")
        pres_penalty_label.grid(row=5, column=0)
        pres_penalty_entry = tk.Entry(self, textvariable=self.pres_penalty_var)
        pres_penalty_entry.grid(row=5, column=1)

        # Stop Entry
        stop_label = tk.Label(self, text="Stop:")
        stop_label.grid(row=6, column=0)
        stop_entry = tk.Entry(self, textvariable=self.stop_var)
        stop_entry.grid(row=6, column=1)

        # OK Button
        ok_button = tk.Button(self, text="OK", command=self.send_data)
        ok_button.grid(row=7, column=0, columnspan=2, pady=10)

    def send_data(self):
        data = {
            "model": self.model_var.get(),
            "temperature": float(self.temp_var.get()),
            "max_tokens": int(self.max_tokens_var.get()),
            "top_p": float(self.top_p_var.get()),
            "frequency_penalty": float(self.freq_penalty_var.get()),
            "presence_penalty": float(self.pres_penalty_var.get()),
            "stop": [self.stop_var.get()]
        }
        json_data = json.dumps(data)

        # Create TCP socket and send data
        HOST = 'localhost'
        PORT = 12345
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(json
