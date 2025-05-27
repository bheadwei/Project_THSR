import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox

class PassengerInfoForm:
    def __init__(self):
        self.root = tb.Window(themename="journal")  # 可換成其他主題 like 'superhero', 'darkly', 'cosmo', 'morph'
        self.root.title("高鐵訂票乘客資訊")
        self.root.geometry("400x620")
        
        self.stations = {
            "南港": "1", "台北": "2", "板橋": "3", "桃園": "4", "新竹": "5", "苗栗": "6",
            "台中": "7", "彰化": "8", "雲林": "9", "嘉義": "10", "台南": "11", "左營": "12"
        }

        # 表單區塊
        frame = tb.Frame(self.root, padding=20)
        frame.pack(expand=True, fill="both")

        self.create_label_input(frame, "出發日期： (YYYY/MM/DD)", "date_entry")
        self.create_label_input(frame, "出發時間： (HH:MM)", "time_entry")
        self.create_label_combobox(frame, "出發站：", "start_var", default="台北")
        self.create_label_combobox(frame, "抵達站：", "arrive_var", default="左營")
        self.create_label_input(frame, "張數：", "amount_entry")
        self.create_label_input(frame, "身分證字號：", "id_entry")
        self.create_label_input(frame, "電子郵件：", "email_entry")

        # 送出按鈕
        submit_btn = tb.Button(self.root, text="送出", command=self.submit, bootstyle=PRIMARY)
        submit_btn.pack(pady=20)

        self.result = None
        self.root.mainloop()

    def create_label_input(self, parent, text, attr_name):
        label = tb.Label(parent, text=text, font=("微軟正黑體", 10))
        label.pack(anchor="w", pady=(10, 0))
        entry = tb.Entry(parent, width=30)
        entry.pack()
        setattr(self, attr_name, entry)

    def create_label_combobox(self, parent, text, attr_name, default=None):
        label = tb.Label(parent, text=text, font=("微軟正黑體", 10))
        label.pack(anchor="w", pady=(10, 0))
        var = tb.StringVar(value=default)
        combobox = tb.Combobox(parent, textvariable=var, values=list(self.stations.keys()), state="readonly", width=28)
        combobox.pack()
        setattr(self, attr_name, var)

    def submit(self):
        date = self.date_entry.get().strip()
        time = self.time_entry.get().strip()
        amount = self.amount_entry.get().strip()
        id_number = self.id_entry.get().strip().upper()
        email = self.email_entry.get().strip()
        start_station = self.stations.get(self.start_var.get())
        arrive_station = self.stations.get(self.arrive_var.get())

        if not all([date, time, id_number, email]):
            messagebox.showwarning("欄位未填", "請填寫所有欄位！")
            return

        self.result = {
            "date": date,
            "time": time,
            "start_station": start_station,
            "arrive_station": arrive_station,
            "amount": amount,
            "id_number": id_number,
            "email": email
        }
        self.root.destroy()
