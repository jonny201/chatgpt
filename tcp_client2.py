import tkinter as tk
import socket

class TCPClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def send_message(self, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(message.encode('utf-8'))
            response = s.recv(1024)
            return response.decode('utf-8')

class TCPClientDialog:
    def __init__(self, master):
        self.master = master
        master.title("TCP Client Dialog")

        self.host_label = tk.Label(master, text="Host:")
        self.host_label.grid(row=0, column=0)

        self.host_entry = tk.Entry(master)
        self.host_entry.grid(row=0, column=1)

        self.port_label = tk.Label(master, text="Port:")
        self.port_label.grid(row=1, column=0)

        self.port_entry = tk.Entry(master)
        self.port_entry.grid(row=1, column=1)

        self.message_label = tk.Label(master, text="Message:")
        self.message_label.grid(row=2, column=0)

        self.message_entry = tk.Entry(master)
        self.message_entry.grid(row=2, column=1)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.grid(row=3, column=0)

        self.response_label = tk.Label(master, text="Response:")
        self.response_label.grid(row=4, column=0)

        self.response_text = tk.Text(master, height=5, width=30)
        self.response_text.grid(row=4, column=1)

    def send_message(self):
        host = self.host_entry.get()
        port = int(self.port_entry.get())
        message = self.message_entry.get()

        client = TCPClient(host, port)
        response = client.send_message(message)

        self.response_text.delete(1.0, tk.END)
        self.response_text.insert(tk.END, response)

if __name__ == '__main__':
    root = tk.Tk()
    app = TCPClientDialog(root)
    root.mainloop()
