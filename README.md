# 🚄 THSRCBot 自動高鐵訂票系統

一套使用 Python 與 Selenium 開發的 **台灣高鐵自動訂票機器人**，配合圖形化介面，使用者只需輸入資料，即可自動完成整個訂票流程，從選擇班次、辨識驗證碼、填寫旅客資料，到最終的訂單資訊下載。

---

## ✨ 功能特色

- 🖥️ 圖形化操作介面（Tkinter + ttkbootstrap）
- 🔍 自動填寫起訖站、日期、時間與張數
- 🤖 自動處理驗證碼辨識（使用 `ddddocr`）
- 📩 自動輸入身分證與電子信箱資料
- 💾 成功訂票後自動儲存 JSON 訂單紀錄
- 🧠 發生錯誤時自動重試（最多三次）

---

## 📦 安裝與執行方式

### 系統需求

- Python 3.8 ~ 3.12
- Google Chrome
- ChromeDriver（版本需與 Chrome 對應）

### 安裝套件

```bash
pip install -r requirements.txt
```

### 啟動程式

```bash
python main.py
```

---

## 🧾 GUI 輸入欄位說明

| 欄位名稱     | 說明與格式              | 必填 |
|------------|----------------------|------|
| 出發日期     | 格式：YYYY/MM/DD     | ✅   |
| 出發時間     | 格式：HH:MM          | ✅   |
| 出發站       | 從下拉選單中選擇         | ✅   |
| 抵達站       | 從下拉選單中選擇         | ✅   |
| 張數         | 整數（成人票數）         | ✅   |
| 身分證字號    | 台灣身份證格式，大寫     | ✅   |
| 電子郵件     | 例如：abc@gmail.com  | ❌   |

---

## 🗂️ 專案結構

```
THSRCBot/
├── main.py                      # 主程式入口，負責錯誤重試與 log 記錄
├── requirements.txt             # 套件需求檔
├── README.md                    # 本說明文件
├── THSRC_bot/
│   ├── booking.py              # 核心自動化訂票流程邏輯
│   ├── browser.py              # 設定與啟動 Selenium WebDriver
│   ├── gui.py                  # GUI 表單介面（Tkinter + ttkbootstrap）
│   ├── ocr.py                  # 使用 ddddocr 進行驗證碼辨識
│   └── parser.py               # 提取並解析最終訂單資訊
├── orderfolder/                # 儲存成功的訂單 JSON 檔案
└── errorfolder/                # 儲存錯誤資訊與堆疊紀錄
```

---

## 📊 訂票流程圖（Mermaid）

```mermaid
flowchart TD
    A[啟動主程式 main.py] --> B[開啟 GUI 輸入資料]
    B --> C{使用者送出表單？}
    C -- 否 --> B
    C -- 是 --> D[將表單轉為 user_data]
    D --> E[初始化 THSRCBot]
    E --> F[開啟官網頁面]
    F --> G[進入訂票頁 iframe]
    G --> H[填寫資料與時間]
    H --> I[截圖驗證碼並辨識]
    I --> J[送出查詢]
    J --> K[選擇班次並確認]
    K --> L[填寫身分證與 email]
    L --> M[送出乘客資料]
    M --> N[解析訂票資訊並存檔]
    N --> O[顯示成功與 JSON 儲存]
```

---

## 🔮 未來功能規劃

- 🧒 支援各類票卷：兒童票、敬老票、愛心票等
- 🗓️ 使用 DateEntry / TimePicker 避免手動輸入錯誤
- 🌐 多語系支援（繁中 / 英文）
- 💬 將訂票結果以 Email 寄送提醒
- 🧪 增加單元測試與自動化測試機制

---

## 📜 授權

本專案僅供學術與個人使用，請勿用於商業用途或惡意搶票。

---

## 🙋‍♂️ 貢獻與回饋

歡迎任何建議與改進，請透過 Issue 或 PR 提出！
