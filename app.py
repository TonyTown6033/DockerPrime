from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = './uploaded_files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    try:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        
        # 假设你有一个函数 `process_file` 来处理文件
        result = process_file(file_path)
        
        return jsonify({"filename": file.filename, "result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def process_file(file_path: str):
    # 这里放置你的处理逻辑
    # 例如解析文件内容，执行脚本等
    # 这里简单示例返回文件大小
    return os.path.getsize(file_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

