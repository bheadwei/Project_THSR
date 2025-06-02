import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
import re
from datetime import datetime, timedelta

class PassengerInfoForm:
    def __init__(self):
        self.root = tb.Window(themename="journal")  
        self.root.title("高鐵訂票乘客資訊")
        self.root.geometry("400x620")
        
        self.stations = {
            "南港": "1", "台北": "2", "板橋": "3", "桃園": "4", "新竹": "5", "苗栗": "6",
            "台中": "7", "彰化": "8", "雲林": "9", "嘉義": "10", "台南": "11", "左營": "12"
        }

        # 表單區塊
        frame = tb.Frame(self.root, padding=20)
        frame.pack(expand=True, fill="both")

        self.create_label_input(frame, "出發日期*： (YYYY/MM/DD)", "date_entry")
        self.create_label_input(frame, "出發時間*： (HH:MM)", "time_entry")
        self.create_label_combobox(frame, "出發站*：", "start_var", default="台北")
        self.create_label_combobox(frame, "抵達站*：", "arrive_var", default="左營")
        self.create_label_input(frame, "張數*：", "amount_entry")
        self.create_label_input(frame, "身分證字號*：", "id_entry")
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

        if not all([date, time, id_number]):
            messagebox.showwarning("欄位未填", "請填寫所有欄位！")
            return
        
        # === 日期格式驗證 ===
        try:
            date_obj = datetime.strptime(date, "%Y/%m/%d")
            if date_obj.date() < datetime.today().date():
                messagebox.showerror("日期錯誤", "出發日期不能早於今天！")
                return
            elif date_obj.date() > (datetime.today().date() + timedelta(days=28)):
                messagebox.showerror("日期錯誤", "請輸入29天內的日期！")
                return
        except ValueError:
            messagebox.showerror("格式錯誤", "請輸入正確的日期格式 (YYYY/MM/DD)！")
            return

        # === 時間格式驗證 ===
        try:
            datetime.strptime(time, "%H:%M")
        except ValueError:
            messagebox.showerror("格式錯誤", "請輸入正確的時間格式 (HH:MM)！")
            return

        # === 張數驗證 ===
        if not amount.isdigit() or int(amount) <= 0:
            messagebox.showerror("張數錯誤", "請輸入正確的張數（正整數）！")
            return
        
         # === 身分證格式驗證 ===
        if not re.match(r'^[A-Z][0-9]{9}$', id_number):
            messagebox.showerror("身分證錯誤", "請輸入正確的身分證格式（1英文字母+9數字）！")
            return
        

        # === Email 格式驗證 ===
        if email and not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
            messagebox.showerror("Email格式錯誤", "請輸入正確的電子郵件格式！")
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
