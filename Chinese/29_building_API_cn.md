# 30天Python编程挑战：第29天 - 构建API

- [第29天](#第29天)
- [构建API](#构建api)
  - [API的结构](#api的结构)
  - [使用GET获取数据](#使用get获取数据)
  - [通过ID获取文档](#通过id获取文档)
  - [使用POST创建数据](#使用post创建数据)
  - [使用PUT更新](#使用put更新)
  - [使用Delete删除文档](#使用delete删除文档)
- [💻 练习：第29天](#-练习第29天)

## 第29天

## 构建API

在本节中，我们将介绍一个RESTful API，它使用HTTP请求方法来GET、PUT、POST和DELETE数据。

RESTful API是一种应用程序编程接口(API)，使用HTTP请求来GET、PUT、POST和DELETE数据。在前几节中，我们学习了Python、Flask和MongoDB。我们将利用我们获得的知识，使用Python Flask和MongoDB开发一个RESTful API。每个具有CRUD(创建、读取、更新、删除)操作的应用程序都有一个API，用于从数据库创建数据、获取数据、更新数据或删除数据。

浏览器只能处理GET请求。因此，我们必须有一个工具，可以帮助我们处理所有请求方法(GET、POST、PUT、DELETE)。

API示例：

- 国家API：https://restcountries.eu/rest/v2/all
- 猫品种API：https://api.thecatapi.com/v1/breeds

[Postman](https://www.getpostman.com/)是API开发领域非常流行的工具。所以，如果你想完成本节内容，你需要[下载Postman](https://www.getpostman.com/)。Postman的替代品是[Insomnia](https://insomnia.rest/download)。

![Postman](../images/postman.png)

### API的结构

API端点是一个可以帮助检索、创建、更新或删除资源的URL。结构如下所示：
示例：
https://api.twitter.com/1.1/lists/members.json
返回指定列表的成员。只有当经过身份验证的用户拥有指定列表时，才会显示私人列表成员。
公司名称后跟版本，然后是API的目的。
方法：
HTTP方法和URL

API使用以下HTTP方法进行对象操作：

```sh
GET        用于对象检索
POST       用于对象创建和对象操作
PUT        用于对象更新
DELETE     用于对象删除
```

让我们构建一个收集关于30DaysOfPython学生信息的API。我们将收集姓名、国家、城市、出生日期、技能和个人简介。

为了实现这个API，我们将使用：

- Postman
- Python
- Flask
- MongoDB

### 使用GET获取数据

在这一步中，让我们使用虚拟数据并将其作为json返回。

```py
import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/v1.0/students", methods=["GET"])
def get_students():
    students = [
        {
            "name": "Asabeneh",
            "country": "Finland",
            "city": "Helsinki",
            "skills": ["HTML", "CSS", "JavaScript", "Python"],
        },
        {
            "name": "David",
            "country": "UK",
            "city": "London",
            "skills": ["Python", "MongoDB"],
        },
        {
            "name": "John",
            "country": "Sweden",
            "city": "Stockholm",
            "skills": ["Java", "C#"],
        },
    ]
    return jsonify(students)


if __name__ == "__main__":
    # 部署时使用
    # 使其在生产和开发环境中都能工作
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
```

当你在浏览器上请求http://localhost:5000/api/v1.0/students URL时，你将获得以下内容：

![在浏览器上的GET](../images/get_on_browser.png)

当你在Postman上请求http://localhost:5000/api/v1.0/students URL时，你将获得以下内容：

![在Postman上的GET](../images/get_on_postman.png)

我们不再显示虚拟数据，而是将Flask应用程序与MongoDB连接，并从MongoDB数据库获取数据。

```py
import os
from flask import Flask, Response
from bson.json_util import dumps
import pymongo

app = Flask(__name__)

MONGODB_URI = os.environ.get(
    "MONGODB_URI",
    "mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority",
)
client = pymongo.MongoClient(MONGODB_URI)
db = client["thirty_days_of_python"]  # 访问数据库


@app.route("/api/v1.0/students", methods=["GET"])
def get_students():
    students = list(db.students.find())
    return Response(dumps(students), mimetype="application/json")


if __name__ == "__main__":
    # 部署时使用
    # 使其在生产和开发环境中都能工作
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
```

通过连接Flask，我们可以从thirty_days_of_python数据库中获取学生集合数据。

```sh
[
    {
        "_id": {
            "$oid": "5df68a21f106fe2d315bbc8b"
        },
        "name": "Asabeneh",
        "country": "Finland",
        "city": "Helsinki",
        "age": 38
    },
    {
        "_id": {
            "$oid": "5df68a23f106fe2d315bbc8c"
        },
        "name": "David",
        "country": "UK",
        "city": "London",
        "age": 34
    },
    {
        "_id": {
            "$oid": "5df68a23f106fe2d315bbc8e"
        },
        "name": "Sami",
        "country": "Finland",
        "city": "Helsinki",
        "age": 25
    }
]
```

### 通过ID获取文档

我们可以使用ID访问单个文档，让我们使用ID访问Asabeneh。
http://localhost:5000/api/v1.0/students/5df68a21f106fe2d315bbc8b

```py
import os
from flask import Flask, Response
from bson.objectid import ObjectId
from bson.json_util import dumps
import pymongo

app = Flask(__name__)

MONGODB_URI = os.environ.get(
    "MONGODB_URI",
    "mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority",
)
client = pymongo.MongoClient(MONGODB_URI)
db = client["thirty_days_of_python"]  # 访问数据库


@app.route("/api/v1.0/students", methods=["GET"])
def get_students():
    students = list(db.students.find())
    return Response(dumps(students), mimetype="application/json")


@app.route("/api/v1.0/students/<string:student_id>", methods=["GET"])
def get_student(student_id):
    student = db.students.find_one({"_id": ObjectId(student_id)})
    if student is None:
        return Response(status=404)
    return Response(dumps(student), mimetype="application/json")


if __name__ == "__main__":
    # 部署时使用
    # 使其在生产和开发环境中都能工作
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
```

```sh
{
    "_id": {
        "$oid": "5df68a21f106fe2d315bbc8b"
    },
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "age": 38
}
```

### 使用POST创建数据

我们使用POST请求方法创建数据

```py
import os
from datetime import datetime
from flask import Flask, Response, request
from bson.objectid import ObjectId
from bson.json_util import dumps
import pymongo

app = Flask(__name__)

MONGODB_URI = os.environ.get(
    "MONGODB_URI",
    "mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority",
)
client = pymongo.MongoClient(MONGODB_URI)
db = client["thirty_days_of_python"]  # 访问数据库


@app.route("/api/v1.0/students", methods=["GET"])
def get_students():
    students = list(db.students.find())
    return Response(dumps(students), mimetype="application/json")


@app.route("/api/v1.0/students/<string:student_id>", methods=["GET"])
def get_student(student_id):
    student = db.students.find_one({"_id": ObjectId(student_id)})
    if student is None:
        return Response(status=404)
    return Response(dumps(student), mimetype="application/json")


@app.route("/api/v1.0/students", methods=["POST"])
def create_student():
    student_data = {
        "name": request.form["name"],
        "country": request.form["country"],
        "city": request.form["city"],
        "birthyear": request.form["birthyear"],
        "skills": request.form["skills"].split(", "),
        "bio": request.form["bio"],
        "created_at": datetime.now(),
    }
    result = db.students.insert_one(student_data)
    new_student = db.students.find_one({"_id": result.inserted_id})
    return Response(dumps(new_student), mimetype="application/json", status=201)


if __name__ == "__main__":
    # 部署时使用
    # 使其在生产和开发环境中都能工作
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
```

### 使用PUT更新

```py
import os
from datetime import datetime
from flask import Flask, Response, request
from bson.objectid import ObjectId
from bson.json_util import dumps
import pymongo

app = Flask(__name__)

MONGODB_URI = os.environ.get(
    "MONGODB_URI",
    "mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority",
)
client = pymongo.MongoClient(MONGODB_URI)
db = client["thirty_days_of_python"]  # 访问数据库


@app.route("/api/v1.0/students", methods=["GET"])
def get_students():
    students = list(db.students.find())
    return Response(dumps(students), mimetype="application/json")


@app.route("/api/v1.0/students/<string:student_id>", methods=["GET"])
def get_student(student_id):
    student = db.students.find_one({"_id": ObjectId(student_id)})
    if student is None:
        return Response(status=404)
    return Response(dumps(student), mimetype="application/json")


@app.route("/api/v1.0/students", methods=["POST"])
def create_student():
    student_data = {
        "name": request.form["name"],
        "country": request.form["country"],
        "city": request.form["city"],
        "birthyear": request.form["birthyear"],
        "skills": request.form["skills"].split(", "),
        "bio": request.form["bio"],
        "created_at": datetime.now(),
    }
    result = db.students.insert_one(student_data)
    new_student = db.students.find_one({"_id": result.inserted_id})
    return Response(dumps(new_student), mimetype="application/json", status=201)


@app.route("/api/v1.0/students/<string:student_id>", methods=["PUT"])
def update_student(student_id):
    query = {"_id": ObjectId(student_id)}
    update_data = {
        "$set": {
            "name": request.form["name"],
            "country": request.form["country"],
            "city": request.form["city"],
            "birthyear": request.form["birthyear"],
            "skills": request.form["skills"].split(", "),
            "bio": request.form["bio"],
            "updated_at": datetime.now(),
        }
    }
    db.students.update_one(query, update_data)
    updated_student = db.students.find_one(query)
    if updated_student is None:
        return Response(status=404)
    return Response(dumps(updated_student), mimetype="application/json")


if __name__ == "__main__":
    # 部署时使用
    # 使其在生产和开发环境中都能工作
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
```

### 使用Delete删除文档

```py
import os
from datetime import datetime
from flask import Flask, Response, request
from bson.objectid import ObjectId
from bson.json_util import dumps
import pymongo

app = Flask(__name__)

MONGODB_URI = os.environ.get(
    "MONGODB_URI",
    "mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority",
)
client = pymongo.MongoClient(MONGODB_URI)
db = client["thirty_days_of_python"]  # 访问数据库


@app.route("/api/v1.0/students", methods=["GET"])
def get_students():
    students = list(db.students.find())
    return Response(dumps(students), mimetype="application/json")


@app.route("/api/v1.0/students/<string:student_id>", methods=["GET"])
def get_student(student_id):
    student = db.students.find_one({"_id": ObjectId(student_id)})
    if student is None:
        return Response(status=404)
    return Response(dumps(student), mimetype="application/json")


@app.route("/api/v1.0/students", methods=["POST"])
def create_student():
    student_data = {
        "name": request.form["name"],
        "country": request.form["country"],
        "city": request.form["city"],
        "birthyear": request.form["birthyear"],
        "skills": request.form["skills"].split(", "),
        "bio": request.form["bio"],
        "created_at": datetime.now(),
    }
    result = db.students.insert_one(student_data)
    new_student = db.students.find_one({"_id": result.inserted_id})
    return Response(dumps(new_student), mimetype="application/json", status=201)


@app.route("/api/v1.0/students/<string:student_id>", methods=["PUT"])
def update_student(student_id):
    query = {"_id": ObjectId(student_id)}
    update_data = {
        "$set": {
            "name": request.form["name"],
            "country": request.form["country"],
            "city": request.form["city"],
            "birthyear": request.form["birthyear"],
            "skills": request.form["skills"].split(", "),
            "bio": request.form["bio"],
            "updated_at": datetime.now(),
        }
    }
    db.students.update_one(query, update_data)
    updated_student = db.students.find_one(query)
    if updated_student is None:
        return Response(status=404)
    return Response(dumps(updated_student), mimetype="application/json")


@app.route("/api/v1.0/students/<string:student_id>", methods=["DELETE"])
def delete_student(student_id):
    query = {"_id": ObjectId(student_id)}
    result = db.students.delete_one(query)
    if result.deleted_count == 0:
        return Response(status=404)
    return Response(
        dumps({"message": "Student deleted successfully"}),
        mimetype="application/json",
    )


if __name__ == "__main__":
    # 部署时使用
    # 使其在生产和开发环境中都能工作
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
```

## 💻 练习：第29天

1. 实现上述示例并开发[这个](https://thirtydayofpython-api.herokuapp.com/)

🎉 恭喜！🎉

[<< 第28天](./28_Day_API/28_API_cn.md) | [第30天 >>](./30_Day_Conclusions/30_conclusions_cn.md)