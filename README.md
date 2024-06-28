# ReadMe
智慧果业大屏项目前端，22计算机0102达标内容 后端

> 更新ing

### 2024-06-28
1. 使用蓝图进行模块划分
2. 更新用户管理模块接口： bigScreen/views/user.py
3. 更新数据库为sqlite3本地文件，方便学习
   > 程序运行后会在本地新建instance目录并创建test.db数据库文件
4. 程序每次启动会自动创建数据表和插入数据
   > 若不希望数据重置在 bigScreen/__ init__.py 文件中
   > 
   > 注释创建和删除表代码以及在app.py中注释插入数据代码

## 快速开始

```shell
cd bigScreen-Flask
# 安装flask
pip install flask
# 启动方式1
flask run
# 启动方式2
python app.py
```
## 意见和反馈
:e-mail: zhangqiuqian01@gmail.com
```text
请通过邮箱给我更多的意见和反馈
```

