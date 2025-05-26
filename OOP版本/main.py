from thsr_bot.booking import THSRBot
from time import sleep
if __name__ == "__main__":
    for attempt in range(1, 4):
        print(f"第 {attempt} 次嘗試訂票...")
        try:
            bot = THSRBot()
            bot.run()
            sleep(5)
            break
        except Exception as e:
            print(f"錯誤發生：{e}")
            bot.quit()
            if attempt == 3:
                print("重試達上限，結束程式。")
                