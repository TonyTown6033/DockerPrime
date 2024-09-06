## Docker部署的步骤
- docker build -t my-flask-app .
- docker run -d -p 5000:5000 -name my-flask-container my-flask-app


在根目录下运行


### 可能遇到的问题
Q: python 脚本直接执行可以跑, docker跑不了
A: 没有绑定监听到0.0.0.0
