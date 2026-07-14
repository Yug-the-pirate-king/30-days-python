# 30天Python编程挑战：第26天 - Python网络编程

- [第26天](#-第26天)
  - [Python网络编程](#python网络编程)
    - [Flask](#flask)
      - [文件夹结构](#文件夹结构)
    - [设置项目目录](#设置项目目录)
    - [创建路由](#创建路由)
    - [创建模板](#创建模板)
    - [Python脚本](#python脚本)
    - [导航](#导航)
    - [创建布局](#创建布局)
      - [提供静态文件](#提供静态文件)
    - [部署](#部署)
      - [创建Heroku账户](#创建heroku账户)
      - [登录Heroku](#登录heroku)
      - [创建requirements和Procfile](#创建requirements和procfile)
      - [将项目推送到Heroku](#将项目推送到heroku)
  - [练习：第26天](#练习第26天)

# 📘 第26天

## Python网络编程

Python是一种通用编程语言，可用于多种场合。在本节中，我们将看到如何使用Python进行网络开发。Python有许多Web框架，Django和Flask是最流行的两个。今天，我们将学习如何使用Flask进行Web开发。

### Flask

Flask是用Python编写的Web开发框架，使用Jinja2模板引擎，也可以与现代前端库（如React）结合使用。

如果你还没有安装 virtualenv，请先安装它。虚拟环境可以隔离项目依赖与本地机器依赖。

#### 文件夹结构

完成所有步骤后，你的项目文件结构应如下所示：

```sh
├── Procfile
├── app.py
├── env
│   ├── bin
├── requirements.txt
├── static
│   └── css
│       └── main.css
└── templates
    ├── about.html
    ├── home.html
    ├── layout.html
    ├── post.html
    └── result.html
```

### 设置项目目录

按照以下步骤开始使用Flask。

**步骤1**：安装 virtualenv。

```sh
pip install virtualenv
```

**步骤2**：创建项目目录、虚拟环境并激活它。

```sh
asabeneh@Asabeneh:~/Desktop$ mkdir python_for_web
asabeneh@Asabeneh:~/Desktop$ cd python_for_web/
asabeneh@Asabeneh:~/Desktop/python_for_web$ virtualenv venv
asabeneh@Asabeneh:~/Desktop/python_for_web$ source venv/bin/activate
(venv) asabeneh@Asabeneh:~/Desktop/python_for_web$ pip freeze
(venv) asabeneh@Asabeneh:~/Desktop/python_for_web$ pip install Flask
(venv) asabeneh@Asabeneh:~/Desktop/python_for_web$ pip freeze
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
(venv) asabeneh@Asabeneh:~/Desktop/python_for_web$
```

我们创建了项目目录 `python_for_web`，并在其中创建虚拟环境 `venv`（名称可自定义）。激活后，`pip freeze` 显示尚未安装任何包；安装 Flask 后，会列出项目依赖。

现在，在项目目录中创建 `app.py` 作为主文件，并编写以下代码。

### 创建路由

首先创建首页路由。

```py
# app.py：Flask 应用入口文件
from flask import Flask
import os  # 用于读取环境变量中的端口

app = Flask(__name__)

@app.route('/')  # 定义首页路由
def home():
    return '<h1>欢迎</h1>'

if __name__ == '__main__':
    # 通过环境变量获取端口；本地默认 5000，部署平台会自动注入 PORT
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

要运行 Flask 应用，在主目录中执行：

```sh
python app.py
```

然后访问本地主机的 5000 端口。

接下来，添加"关于"路由。

```py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')  # 定义首页路由
def home():
    return '<h1>欢迎</h1>'

@app.route('/about')  # 定义"关于"页面路由
def about():
    return '<h1>关于我们</h1>'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

现在，我们希望在访问 `/about` 时渲染 HTML 文件，而不是返回字符串。为此，需要先从 `flask` 导入 `render_template`，然后在项目目录中创建 `templates` 文件夹，并放入 `home.html` 和 `about.html`。

### 创建模板

在 `templates` 文件夹内创建 HTML 文件。

`home.html`

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>主页</title>
  </head>

  <body>
    <h1>欢迎回家</h1>
  </body>
</html>
```

`about.html`

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>关于</title>
  </head>

  <body>
    <h1>关于我们</h1>
  </body>
</html>
```

### Python脚本

`app.py`

```py
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')  # 渲染 templates/home.html
def home():
    return render_template('home.html')

@app.route('/about')  # 渲染 templates/about.html
def about():
    return render_template('about.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

### 导航

```html
<ul>
  <li><a href="/">主页</a></li>
  <li><a href="/about">关于</a></li>
</ul>
```

现在，我们可以用上面的链接在页面之间跳转。接下来再添加一个处理表单数据的页面，命名为 `post.html`。

我们可以使用 Jinja2 模板引擎向 HTML 文件注入数据。

```py
from flask import Flask, render_template, request
import os

# 多个页面共享的名称，避免多处硬编码
CHALLENGE_NAME = '30天Python编程挑战'

app = Flask(__name__)

@app.route('/')  # 定义首页路由
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    return render_template(
        'home.html',
        techs=techs,
        name=CHALLENGE_NAME,
        title='主页'
    )

@app.route('/about')
def about():
    return render_template('about.html', name=CHALLENGE_NAME, title='关于我们')

@app.route('/post')
def post():
    name = '编程语言文章'
    path = request.path  # 获取当前请求路径
    return render_template('post.html', name=name, path=path, title='文章')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

`home.html`

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{{ title }}</title>
  </head>

  <body>
    <ul>
      <li><a href="/">主页</a></li>
      <li><a href="/about">关于</a></li>
      <li><a href="/post">文章</a></li>
    </ul>
    <h1>欢迎回到{{ name }}</h1>
    <ul>
      {% for tech in techs %}
      <li>{{ tech }}</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

`about.html`

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{{ title }}</title>
  </head>

  <body>
    <ul>
      <li><a href="/">主页</a></li>
      <li><a href="/about">关于</a></li>
      <li><a href="/post">文章</a></li>
    </ul>
    <h1>关于{{ name }}</h1>
  </body>
</html>
```

`post.html`

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{{ title }}</title>
  </head>

  <body>
    <ul>
      <li><a href="/">主页</a></li>
      <li><a href="/about">关于</a></li>
      <li><a href="/post">文章</a></li>
    </ul>
    <h1>{{ name }}</h1>
    <p>当前路径：{{ path }}</p>
    <form action="/result" method="POST">
      <div>
        <input type="text" name="first_name" placeholder="第一名字" required />
      </div>
      <div>
        <input type="text" name="last_name" placeholder="姓氏" required />
      </div>
      <div>
        <input type="text" name="old_job" placeholder="旧工作" />
      </div>
      <div>
        <input type="text" name="current_job" placeholder="当前工作" />
      </div>
      <div>
        <input type="text" name="country" placeholder="国家" />
      </div>
      <div>
        <button type="submit">提交</button>
      </div>
    </form>
  </body>
</html>
```

现在，添加一个接收表单数据的路由。我们使用 POST 方法，因为需要处理表单提交。

```py
from flask import Flask, render_template, request
import os

CHALLENGE_NAME = '30天Python编程挑战'

app = Flask(__name__)

@app.route('/')  # 定义首页路由
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    return render_template(
        'home.html',
        techs=techs,
        name=CHALLENGE_NAME,
        title='主页'
    )

@app.route('/about')
def about():
    return render_template('about.html', name=CHALLENGE_NAME, title='关于我们')

@app.route('/post')
def post():
    name = '文章'
    return render_template('post.html', name=name, title='文章')

@app.route('/result', methods=['POST'])  # 仅接受 POST 请求
def result():
    # 一次性从表单组织数据：
    # - 必填字段缺失时 Flask 会自动返回 400 错误
    # - 可选字段缺失时默认空字符串，避免 KeyError
    result_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'old_job': request.form.get('old_job', ''),
        'current_job': request.form.get('current_job', ''),
        'country': request.form.get('country', '')
    }

    print(*result_data.values())  # 在服务端打印表单数据，方便调试

    return render_template(
        'result.html',
        result_data=result_data,
        title='结果'
    )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

`result.html`

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{{ title }}</title>
  </head>

  <body>
    <ul>
      <li><a href="/">主页</a></li>
      <li><a href="/about">关于</a></li>
      <li><a href="/post">文章</a></li>
    </ul>
    <h1>表单数据</h1>

    <ul>
      <li>第一名字：{{ result_data.first_name }}</li>
      <li>姓氏：{{ result_data.last_name }}</li>
      <li>旧工作：{{ result_data.old_job }}</li>
      <li>当前工作：{{ result_data.current_job }}</li>
      <li>国家：{{ result_data.country }}</li>
    </ul>
  </body>
</html>
```

在现实世界中，我们不会在每个页面重复 HTML 代码，而是创建一个公共布局并让其他页面继承它。下面创建 `layout.html`，其他文件继承该布局。

### 创建布局

`layout.html`

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      href="https://fonts.googleapis.com/css?family=Lato:300,400|Nunito:300,400|Raleway:300,400&display=swap"
      rel="stylesheet"
    />
    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='css/main.css') }}"
    />
    <title>{% if title %}30天Python - {{ title }}{% else %}30天Python{% endif %}</title>
  </head>

  <body>
    <header>
      <div class="menu-container">
        <div>
          <a class="brand-name nav-link" href="/">30天Python</a>
        </div>
        <ul class="nav-lists">
          <li class="nav-list">
            <a class="nav-link active" href="{{ url_for('home') }}">主页</a>
          </li>
          <li class="nav-list">
            <a class="nav-link active" href="{{ url_for('about') }}">关于</a>
          </li>
          <li class="nav-list">
            <a class="nav-link active" href="{{ url_for('post') }}">文章</a>
          </li>
        </ul>
      </div>
    </header>
    <main>
      {% block content %}{% endblock %}
    </main>
  </body>
</html>
```

在上面的布局中，我们创建了公共的导航和页面结构。`{% block content %}{% endblock %}` 标记允许子模板插入各自的内容。

`home.html`

```html
{% extends 'layout.html' %}

{% block content %}
<div class="container">
  <h1>欢迎回到{{ name }}</h1>
  <p>
    本项目使用以下技术构建：
    <span class="tech">Flask</span>、
    <span class="tech">Python</span>、
    <span class="tech">HTML</span> 与
    <span class="tech">CSS</span>
  </p>
  <ul>
    {% for tech in techs %}
    <li class="tech">{{ tech }}</li>
    {% endfor %}
  </ul>
</div>
{% endblock %}
```

`about.html`

```html
{% extends 'layout.html' %}

{% block content %}
<div class="container">
  <h1>关于{{ name }}</h1>
  <p>
    这个挑战是一个30天编程挑战，旨在帮助你通过每天解决一个Python问题来学习Python编程语言。
  </p>
</div>
{% endblock %}
```

`post.html`

```html
{% extends 'layout.html' %}

{% block content %}
<div class="container">
  <h1>{{ name }}</h1>
  <p>{{ path }}</p>
  <form action="{{ url_for('result') }}" method="POST">
    <div>
      <input type="text" name="first_name" placeholder="第一名字" required />
    </div>
    <div>
      <input type="text" name="last_name" placeholder="姓氏" required />
    </div>
    <div>
      <input type="text" name="old_job" placeholder="旧工作" />
    </div>
    <div>
      <input type="text" name="current_job" placeholder="当前工作" />
    </div>
    <div>
      <input type="text" name="country" placeholder="国家" />
    </div>
    <div>
      <button type="submit">提交</button>
    </div>
  </form>
</div>
{% endblock %}
```

`result.html`

```html
{% extends 'layout.html' %}

{% block content %}
<div class="container">
  <h1>表单数据</h1>
  <ul>
    <li>第一名字：{{ result_data.first_name }}</li>
    <li>姓氏：{{ result_data.last_name }}</li>
    <li>旧工作：{{ result_data.old_job }}</li>
    <li>当前工作：{{ result_data.current_job }}</li>
    <li>国家：{{ result_data.country }}</li>
  </ul>
</div>
{% endblock %}
```

#### 提供静态文件

将 `main.css` 放在 `static/css` 目录下：

```css
/* === 变量 === */
:root {
  --primary-color: #5bbc2e;
  --primary-hover: #4b9c25;
  --bg-color: #f0f8ea;
  --border-color: #ddd;
}

/* === 通用 === */
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  padding: 0;
  font-family: "Lato", sans-serif;
  background-color: var(--bg-color);
}

.container {
  max-width: 80%;
  margin: 0 auto;  /* 水平居中 */
  padding: 30px;
}

ul {
  list-style-type: none;
  padding: 0;
}

.tech {
  color: var(--primary-color);
}

/* === 头部导航 === */
header {
  background-color: var(--primary-color);
}

.menu-container {
  display: flex;
  justify-content: space-between;
  align-items: center;  /* 垂直居中对齐 */
  padding: 20px 30px;
}

.brand-name {
  color: white;
  font-weight: 800;
  font-size: 24px;
}

.nav-lists {
  display: flex;
  margin: 0;
}

.nav-list {
  margin-right: 15px;
}

.nav-link {
  text-decoration: none;
  color: white;
  font-weight: 300;
}

/* === 表单 === */
form {
  margin: 30px 0;
  border: 1px solid var(--border-color);
  padding: 30px;
  border-radius: 10px;
}

form > div {
  margin-bottom: 15px;
}

input {
  width: 100%;
  padding: 10px;
  border: 1px solid var(--border-color);
  border-radius: 5px;
  outline: 0;
  font-size: 16px;
  margin-top: 5px;
}

button {
  padding: 12px 24px;
  border: 0;
  background-color: var(--primary-color);
  color: white;
  border-radius: 10px;
  font-size: 16px;
  outline: 0;
  cursor: pointer;
}

button:hover {
  background-color: var(--primary-hover);
}
```

### 部署

#### 创建Heroku账户

Heroku 是一个流行的 PaaS 部署平台，可用于托管 Python Web 应用。部署前请确保已注册账户并安装 Heroku CLI。

#### 登录Heroku

```sh
asabeneh@Asabeneh:~/Desktop/python_for_web$ heroku login
heroku: Press any key to open up the browser to login or q to exit:
Opening browser to https://cli-auth.heroku.com/auth/cli/browser/ec0972d5-d8c6-4adf-b004-a42a22dd09a8
Logging in... done
Logged in as asabeneh@gmail.com
asabeneh@Asabeneh:~/Desktop/python_for_web$
```

#### 创建requirements和Procfile

在部署前，我们需要告诉 Heroku 需要安装哪些依赖以及如何运行应用。`requirements.txt` 列出所有依赖包及其版本。

```sh
asabeneh@Asabeneh:~/Desktop/python_for_web$ pip freeze
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
asabeneh@Asabeneh:~/Desktop/python_for_web$ pip freeze > requirements.txt
```

`Procfile` 告诉 Heroku 如何运行应用。在本例中，我们使用 Gunicorn 作为 WSGI HTTP 服务器。需要先将 Gunicorn 添加到依赖中。

```sh
asabeneh@Asabeneh:~/Desktop/python_for_web$ pip install gunicorn
asabeneh@Asabeneh:~/Desktop/python_for_web$ pip freeze > requirements.txt
```

创建 `Procfile`，并写入以下内容：

```sh
web: gunicorn app:app
```

#### 将项目推送到Heroku

```sh
asabeneh@Asabeneh:~/Desktop/python_for_web$ heroku create 30-days-of-python-app
Creating ⬢ 30-days-of-python-app... done
https://30-days-of-python-app.herokuapp.com/ | https://git.heroku.com/30-days-of-python-app.git
asabeneh@Asabeneh:~/Desktop/python_for_web$ git init
Initialized empty Git repository in /home/asabeneh/Desktop/python_for_web/.git/
asabeneh@Asabeneh:~/Desktop/python_for_web$ heroku git:remote -a 30-days-of-python-app
set git remote heroku to https://git.heroku.com/30-days-of-python-app.git
asabeneh@Asabeneh:~/Desktop/python_for_web$ echo -e "venv\n.vscode" > .gitignore
asabeneh@Asabeneh:~/Desktop/python_for_web$ git add .
asabeneh@Asabeneh:~/Desktop/python_for_web$ git commit -m "first python web app"
[master (root-commit) 9dfcc6a] first python web app
 9 files changed, 403 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 Procfile
 create mode 100644 app.py
 create mode 100644 requirements.txt
 create mode 100644 static/css/main.css
 create mode 100644 templates/about.html
 create mode 100644 templates/home.html
 create mode 100644 templates/layout.html
 create mode 100644 templates/post.html
 create mode 100644 templates/result.html
asabeneh@Asabeneh:~/Desktop/python_for_web$ git push heroku master
Enumerating objects: 14, done.
Counting objects: 100% (14/14), done.
Delta compression using up to 2 threads
Compressing objects: 100% (12/12), done.
Writing objects: 100% (14/14), 6.08 KiB | 1.52 MiB/s, done.
Total 14 (delta 2), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> Python app detected
remote: -----> Installing python-3.6.10
remote: -----> Installing pip
remote: -----> Installing dependencies with Pipenv 2018.5.18…
remote:        Installing dependencies from Pipfile.lock (872ae5)…
remote: -----> Installing SQLite3
remote: -----> $ python manage.py collectstatic --noinput
remote:        Traceback (most recent call last):
remote:          File "manage.py", line 10, in <module>
remote:            from app import app
remote:        ModuleNotFoundError: No module named 'app'
remote:
remote:  !     Error while running '$ python manage.py collectstatic --noinput'.
remote:        See traceback above for details.
remote:
remote:        You may need to update application code to resolve this error.
remote:        Or, you can disable collectstatic for this application:
remote:
remote:           $ heroku config:set DISABLE_COLLECTSTATIC=1
remote:
remote:        https://devcenter.heroku.com/articles/django-assets
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote:
remote: -----> Compressing...
remote:        Done: 55.7M
remote: -----> Launching...
remote:        Released v3
remote:        https://30-days-of-python-app.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
To https://git.heroku.com/30-days-of-python-app.git
 * [new branch]      master -> master
asabeneh@Asabeneh:~/Desktop/python_for_web$
```

如你所见，我们已经成功地创建并部署了第一个 Python Web 应用。你可以使用[此链接](https://30-days-of-python-app.herokuapp.com/)访问本应用。

事不宜迟，让我们做一些练习，巩固所学到的知识。

## 练习：第26天

1. 创建一个名为"成绩计算器"的 Flask 应用。用户可以输入科目名称和分数，应用根据分数区间显示不同消息：
   - 如果分数 ≥ 90，显示"优秀！你的[科目]成绩是[分数]"。
   - 如果 80 ≤ 分数 < 90，显示"很好！你的[科目]成绩是[分数]"。
   - 如果 70 ≤ 分数 < 80，显示"一般！你的[科目]成绩是[分数]"。
   - 如果 60 ≤ 分数 < 70，显示"及格！你的[科目]成绩是[分数]"。
   - 如果分数 < 60，显示"你需要更加努力！你的[科目]成绩是[分数]"。

2. 创建一个"体重指数计算器"应用，计算 BMI = 体重(kg) / 身高(m)²，并根据 BMI 值显示健康状态：
   - BMI < 18.5："体重过轻"
   - 18.5 ≤ BMI < 24.9："健康体重"
   - 25 ≤ BMI < 29.9："超重"
   - BMI ≥ 30："肥胖"

3. 创建一个博客应用，用户可以添加、编辑和删除博客文章。

4. 创建一个"任务管理器"应用，用户可以添加、查看和删除任务。

🎉 恭喜！🎉

[<< 第25天](./25_Day_Pandas/25_pandas_cn.md) | [第27天 >>](./27_Day_Python_with_mongodb/27_python_with_mongodb_cn.md)