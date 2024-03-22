# Everything-To-Desktop-Pet
把gif变成桌宠！
## 使用方法
你需要安装python才能运行该程序，使用以下命令安装
```bash
# Debian/Ubuntu
sudo apt install python3
# Redhat/CentOS
sudo yum install python3
```
接下来克隆该仓库到本地
```bash
git clone https://github.com/CSneko/Everything-To-Desktop-pet.git
cd Everything-To-Desktop-pet/
```
使用以下命令启动它
```bash
python3 src/main.py
```
## 创建宠物
你需要在`pets`文件夹中创建一个`.json`文件，并将`test.json`的内容复制到其中，以下是内容解释
```json
{
  "name" : "宠物名称",
  "type" : "gif",
  "path" : "gif文件路径，相对于执行目录",
  "icon" : "图标路径",
  "speed" : "gif播放速度，请填一个整数",
  "size" : {
    "x" : "窗口的长，请填一个整数", "y": "窗口的宽，请填一个整数"
  }
}
```
## 未来计划
目前仅支持gif，未来会支持liv2d以及AI聊天功能