import tkinter as tk
from tkinter import messagebox

class PassengerInfoForm:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("高鐵訂票乘客資訊")
        self.root.geometry("300x400")
        # 高鐵站選單
        self.stations = {
            "南港": "1", "台北": "2", "板橋": "3", "桃園": "4", "新竹": "5", "苗栗": "6",
            "台中": "7", "彰化": "8", "雲林": "9", "嘉義": "10", "台南": "11", "左營": "12"
        }

        # 輸入欄位
        tk.Label(self.root, text="出發日期 (YYYY/MM/DD)").pack()
        self.date_entry = tk.Entry(self.root)
        self.date_entry.pack()

        tk.Label(self.root, text="出發時間 (HH:MM)").pack()
        self.time_entry = tk.Entry(self.root)
        self.time_entry.pack()

        tk.Label(self.root, text="出發站").pack()
        self.start_var = tk.StringVar(value="台北")
        tk.OptionMenu(self.root, self.start_var, *self.stations.keys()).pack()

        tk.Label(self.root, text="抵達站").pack()
        self.arrive_var = tk.StringVar(value="左營")
        tk.OptionMenu(self.root, self.arrive_var, *self.stations.keys()).pack()

        tk.Label(self.root, text="張數").pack()
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack()

        tk.Label(self.root, text="身分證字號").pack()
        self.id_entry = tk.Entry(self.root)
        self.id_entry.pack()

        tk.Label(self.root, text="電子郵件").pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()

        # 送出按鈕
        submit_btn = tk.Button(self.root, text="送出", command=self.submit)
        submit_btn.pack(pady=10)

        self.result = None  # 儲存輸入結果

        self.root.mainloop()

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

        # 儲存結果，關閉視窗
        self.result = {
            "date": date,
            "time": time,
            "start_station":start_station,
            "arrive_station":arrive_station,
            "amount": amount,
            "id_number": id_number,
            "email": email
        }
        self.root.destroy()
