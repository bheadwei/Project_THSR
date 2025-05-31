from THSR_bot.booking import THSRBot
from THSR_bot.gui import PassengerInfoForm
from time import sleep
import os
import logging
import traceback

# 設定日誌紀錄
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    form = PassengerInfoForm()
    if form.result:  # 使用者有成功輸入資料
        user_data = form.result
        for attempt in range(1, 4):
            logging.info(f"第 {attempt} 次嘗試訂票...")
            try:
                bot = THSRBot(user_data)
                bot.run()   
                sleep(5)
                break
            except Exception as e:
                logging.error(f"錯誤發生，重新執行")
                errorfolder = "errorFolder"
                if not os.path.exists(errorfolder):
                    os.makedirs(errorfolder)
                # 設定錯誤檔案名稱
                filename = os.path.join(errorfolder, f"error_Stacktrace.txt")
                with open(filename, "w") as f:
                    # 寫入錯誤堆疊信息
                    f.write("錯誤發生，重新執行!\n")
                    f.write(f"錯誤訊息: {str(e)}\n")
                    f.write("錯誤堆疊信息:\n")
                    f.write(traceback.format_exc())  # 獲取完整的錯誤堆疊信息
                    
                bot.quit()
                if attempt == 3:
                    logging.critical("重試達上限，結束程式。")
                