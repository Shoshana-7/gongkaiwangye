from flask import Flask, request, make_response  # 导入 make_response 替代 render_template
import os  # 用于处理文件路径

app = Flask(__name__)
messages = []  # 存储消息


@app.route('/', methods=['GET', 'POST'])
def index():
    # 处理表单提交
    if request.method == 'POST':
        name = request.form.get('name', '匿名用户')
        message = request.form.get('message', '')
        if message:
            messages.append(f"{name}: {message}")

    # 读取 HTML 文件内容（这里填写你的 HTML 文件实际路径）
    html_path = r"D:\python\pythonProject3\.venv\mingzi\人因工程作业.html"
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # 替换 HTML 中的消息占位符（原来的 {% for msg in messages %} 逻辑）
    msg_html = ""
    for msg in messages:
        msg_html += f'<div class="msg">{msg}</div>'  # 和原来的 HTML 样式保持一致
    html_content = html_content.replace('{{ messages_here }}', msg_html)

    # 返回 HTML 内容
    return make_response(html_content)


if __name__ == '__main__':
    app.run(debug=True)