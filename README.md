# Goopi 自動結帳機器人 

這是一個基於 Python 的自動化腳本，使用 Selenium 和 undetected-chromedriver 在 [goopi.co](https://www.goopi.co) 網站上自動購買商品。腳本能自動選擇商品、顏色、尺寸、數量，並完成結帳流程，包含填寫使用者資訊和信用卡資料。
#注意事項
 此專案已暫停最新 架構代碼並不是最佳化 僅供參考 
## 功能
- 根據商品名稱自動搜尋目標商品。
- 自動選擇商品顏色、尺寸和購買數量。
- 自動填寫使用者資訊（姓名、電子郵件、電話等）和信用卡資訊。
- 支援 7-11 門市取貨，預設指定門市資訊。
- 內建到期日檢查，防止腳本在指定日期後運行。
- 提供帶時間戳的日誌，方便除錯。

## 環境需求
- Python 3.8 或更高版本
- 已安裝 Chrome 瀏覽器
- 與 Chrome 版本相容的 ChromeDriver 可執行檔
- 一個包含商品、使用者、付款和門市資訊的 JSON 配置文件（`buy.json`）

## 安裝
1.安裝所需的 Python 套件：
   - `undetected-chromedriver`
   - `selenium`
2. 下載 [ChromeDriver](https://chromedriver.chromium.org/downloads) 並放置在 `D:/bbc.exe`（或在 `Goopi.py` 中更新路徑）。
3. 準備 `buy.json` 配置文件（參見下方 [配置](#配置)）。

## 使用方法
1. 更新 `buy.json` 文件，填入商品、使用者、付款和門市資訊。
2. 運行腳本：
   ```bash
   python Goopi.py
   ```
3. 腳本將執行以下操作：
   - 檢查到期日（預設：`2024-07-01 11:30:00`）。
   - 載入 goopi.co 網站。
   - 搜尋指定商品。
   - 將商品加入購物車，選擇顏色、尺寸和數量。
   - 使用提供的資訊完成結帳流程。

## 配置
在 `D:/` 目錄下創建 `buy.json` 文件，結構如下：

```json
{
  "product_info": {
    "product_name": "Wall of Sound - 7:37/“MOTE” Mesh-Mix Snow Pants",
    "Color": "Black",
    "size": "L",
    "count": 2
  },
  "personal_info": {
    "info_username": "張某某",
    "info_email": "aabb@gmail.com",
    "info_phone": "0966123432",
    "info_LineId": "@aery",
    "info_msg": "盡快出貨"
  },
  "card_info": {
    "card_number": "4532115598843071",
    "card_name": "張某某",
    "card_date": "10/27",
    "card_cvc": "171"
  },
  "store_info": {
    "id": "263713",
    "name": "新大慶門市",
    "address": "基隆市中山區中和路168巷7弄13號15號1樓"
  }
}
```
## 更新日誌
 v1
 支援根據商品名稱自動搜尋和選擇商品。
 支援選擇商品顏色、尺寸和購買數量。
 支援 7-11 門市取貨，包含預設門市資訊。
 內建到期日檢查，防止腳本在指定日期後運行。
 使用 JSON 配置文件（buy.json）儲存使用者、商品和付款資訊。
 提供帶時間戳的日誌，方便除錯。

 


## 貢獻
歡迎為本專案貢獻！

## 授權
本專案採用 MIT 授權，詳情請見 [LICENSE](LICENSE) 文件。

## 免責聲明
本腳本僅供教育用途。使用本腳本時，請確保遵守 [goopi.co](https://www.goopi.co) 的服務條款和相關法律法規。開發者對因使用本腳本而導致的任何問題不承擔責任。
