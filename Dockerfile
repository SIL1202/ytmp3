FROM python:3.10-slim

# 安裝 ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# 設定工作目錄
WORKDIR /app

# 複製檔案到容器內
COPY . .

# 安裝 Python 套件
RUN pip install --no-cache-dir -r requirements.txt

# 執行 bot
CMD ["python", "bot.py"]
