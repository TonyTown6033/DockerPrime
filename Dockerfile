# 使用官方Python基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录的内容到工作目录
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露Flask应用运行的端口
EXPOSE 5000

# 启动Flask应用
CMD ["python", "app.py"]
