import tkinter as tk
from tkinter import ttk
import tcp_client3
prompt = "Hi"
data = {
"param":{
    "prompt": prompt,
    "max_tokens": 1300,
    "n": 1,
    "stop": ".",
    "temperature": 0.1,
},
"key":"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",
"continue": "yes"
}

config = {
    "max_tokens": 1300,
    "n": 1,
    "stop": ".",
    "temperature": 0.1
}

window = tk.Tk()
window.geometry("400x800")
window.title("Chat Window")
# Create a notebook (tabs)
notebook = ttk.Notebook(window)
# Create the first tab
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='对话')
# Create the second tab
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='配置')
# Pack the notebook and show the window
notebook.pack(expand=1, fill="both")

class ChatWindow:
    def __init__(self, master):
        self.master = master

        # 聊天记录框
        self.chat_history = tk.Text(master, height=20, width=40)
        self.chat_history.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.chat_history.config(state=tk.DISABLED)

        # 输入框和发送按钮
        self.input_frame = tk.Frame(master)
        self.input_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.input_entry = tk.Text(self.input_frame,height=6,width=40)
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.send_button = tk.Button(self.input_frame, text="发送",height=6, command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

    def send_message(self, event=None):
        message = self.input_entry.get("1.0", "end-1c")
        if message:
            get_param()
            self.chat_history.config(state=tk.NORMAL)
            self.chat_history.insert(tk.END, f"You: {message}\n")
            self.chat_history.see(tk.END)
            self.input_entry.delete("1.0", "end")
            client = tcp_client3.TCPClient()
            data["param"][ "prompt" ] = message
            ret = client.send_json(data)
            self.chat_history.insert(tk.END, f"GTP: {ret}\n")
            self.chat_history.config(state=tk.DISABLED)
            self.chat_history.see(tk.END)


import tkinter as tk
from tkinter import ttk

config_list = {
    "默认":
        {
            "model": "code-davinci-002",
            "temperature": 0,
            "max_tokens": 64,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0,
            "stop": ["\"\"\""]
        },
    "解释代码":
        {
           "model" : "code-davinci-002",
          "temperature": 0,
           "max_tokens" : 64,
           "top_p" : 1,
           "frequency_penalty" : 0,
           "presence_penalty" : 0,
           "stop" : ["\"\"\""]
        },
    "给二年级学生总结":
        {
            "model" : "text-davinci-003",
            "temperature": 0.7,
            "max_tokens" : 256,
            "top_p" : 1,
            "frequency_penalty" : 0,
            "presence_penalty" : 0
        }
}

class ConfigDialog:
    def __init__(self, parent):
        self.dialog = parent
        self.key_var = tk.StringVar(value="")
        self.max_tokens_var = tk.DoubleVar(value=1300)
        self.temperature_var = tk.DoubleVar(value=0.1)
        self.n_var = tk.StringVar(value="1")
        self.stop_var = tk.StringVar(value=".")
        self.model_var = tk.StringVar(value="")

        self.key_entry = ttk.Entry(self.dialog, textvariable=self.key_var)
        self.max_tokens_slider = ttk.Scale(self.dialog, from_=10, to=2000, variable=self.max_tokens_var, orient="horizontal", length=200)
        self.temperature_slider = ttk.Scale(self.dialog, from_=0, to=1.0, variable=self.temperature_var, orient="horizontal", length=200)
        self.n_entry = ttk.Entry(self.dialog, textvariable=self.n_var)
        self.stop_entry = ttk.Entry(self.dialog, textvariable=self.stop_var)
        self.model_entry = ttk.Entry(self.dialog, textvariable=self.model_var)

        # Create a Combobox to display the options in config_list
        self.config_options = ttk.Combobox(self.dialog, values=list(config_list.keys()))

        # Bind the selected option to a callback function
        self.config_options.bind("<<ComboboxSelected>>", self.load_selected_config)

        ttk.Label(self.dialog, text="key:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.key_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.dialog, text="选择语言模型:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.config_options.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

        ttk.Label(self.dialog, text="max_tokens:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.max_tokens_slider.grid(row=2, column=1, padx=5, pady=5)
        ttk.Label(self.dialog, text="temperature:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.temperature_slider.grid(row=3, column=1, padx=5, pady=5)
        ttk.Label(self.dialog, text="n:").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self.n_entry.grid(row=4, column=1, padx=5, pady=5)
        ttk.Label(self.dialog, text="stop:").grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
        self.stop_entry.grid(row=5, column=1, padx=5, pady=5)
        ttk.Label(self.dialog, text="model:").grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
        self.model_entry.grid(row=6, column=1, padx=5, pady=5)

        self.load(config_list["默认"])
        self.config_options.current(0)

    def get(self):
        ret_data=  {
              "param":{
                "model": self.model_var.get(),
                "max_tokens": int(self.max_tokens_var.get()),
                "n": int(self.n_var.get()),
                "stop": self.stop_var.get(),
                "temperature": self.temperature_var.get()
            },
        }

        key_str = self.key_var.get()
        if "sk-"in key_str:
            ret_data["key"] = key_str
        print(ret_data)

        return ret_data

    def load(self, config):
        self.max_tokens_var.set(config.get("max_tokens", 1300))
        self.temperature_var.set(config.get("temperature", 0.1))
        self.n_var.set(config.get("n", "1"))
        self.stop_var.set(config.get("stop", "."))
        self.model_var.set(config.get("model", "code-davinci-002"))

    def load_selected_config(self, event):
        # Load the selected config from config_list
        selected_config_name = self.config_options.get()
        selected_config = config_list[selected_config_name]
        self.load(selected_config)

# Example usage:
chat_window = ChatWindow(tab1)
config_dialog= ConfigDialog(tab2)

def get_param():
    global data
    data = config_dialog.get()

window.mainloop()
