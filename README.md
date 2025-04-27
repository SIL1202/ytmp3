# YTMP3 Telegram Bot

## 專案簡介
本專案是一個 Telegram Bot，功能是接收使用者傳送的 YouTube 連結，自動下載並轉換成 MP3 音檔，傳回給使用者。Bot 已部署至 Railway 平台，24 小時雲端運作。

---

## 開發過程紀錄

### 1. 本地開發
- 使用 `python-telegram-bot` 搭配 `yt-dlp` 和 `ffmpeg`，開發並驗證基本功能。
- 本地環境下，`yt-dlp` 能順利處理常見 YouTube 連結，轉檔功能正常。
- 確認處理流程包含：接收文字訊息 → 呼叫 yt-dlp → 轉成 MP3 → 回傳音檔。

### 2. 雲端部署初期問題
- 初版使用 Railway 平台，預設採用 Nixpacks 進行建置。
- 遇到問題：Nixpacks 環境無法使用 `apt-get` 安裝 `ffmpeg`。
- 錯誤訊息出現：

- 判斷是因為 Nixpacks 環境基礎映像檔限制，不支援自行安裝系統套件。

### 3. 解決方案
- 放棄使用 Nixpacks，改用自定義 Dockerfile。
- Dockerfile 基礎選擇 `python:3.10-slim`，並手動安裝 `ffmpeg`。
- Dockerfile 寫法：
