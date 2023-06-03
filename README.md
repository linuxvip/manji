# 蛮吉 学习项目
## Django Api接口框架
### DRF前置基础知识
1. Python基础知识
Django 是使用 Python 编写的，因此熟悉 Python 语法和基本概念是必要的。你需要了解变量、函数、类、模块等基本概念，并熟悉 Python 的面向对象编程（OOP）思想。

2. Django框架
DRF 是建立在 Django 框架之上的，因此熟悉 Django 框架是必要的。你需要了解 Django 的基本结构、模型-视图-模板（MVT）的设计模式，以及 Django 的路由、视图、模型等概念。

3. RESTful API 的概念
了解什么是 REST（Representational State Transfer）及其核心原则是很重要的。你应该了解资源的概念、HTTP 方法的使用、状态码的含义以及如何设计符合 RESTful 原则的 API。

4. HTTP 协议
熟悉 HTTP 协议是理解和设计 RESTful API 的基础。你需要了解 HTTP 请求方法（GET、POST、PUT、DELETE 等）、请求头、请求体、状态码等相关概念。

5. 数据库知识
DRF 可以与各种数据库进行交互，包括关系型数据库（如 MySQL、PostgreSQL）和非关系型数据库（如 MongoDB）。你应该对数据库的基本概念、模型设计、查询语言等有一定了解。

6. Web 开发基础知识：了解 Web 开发的基本概念和技术，包括前端开发（HTML、CSS、JavaScript）和后端开发（服务器、请求处理、响应生成等）。


### RESTful API规范

1. RESTful API 接口设计规范的关键要素
- 使用合适的HTTP方法：RESTful API 使用不同的 HTTP 方法来表示不同的操作。
常用的方法包括:

    - GET：用于获取资源
    - POST：用于创建新资源
    - PUT：用于更新完整资源
    - PATCH：用于部分更新资源
    - DELETE：用于删除资源

- 使用合适的资源路径：
    - API 的资源路径应该清晰、简洁，并且能够准确地表示资源的层次结构。资源路径应该使用名词复数形式，并使用斜杠（/）进行分隔。

- 使用合适的HTTP状态码
  API 应该返回合适的 HTTP 状态码来表示操作的结果。
    常用的状态码包括：
    - 200 OK：表示成功的 GET 请求
    - 201 Created：表示成功的 POST 请求
    - 204 No Content：表示成功的 DELETE 请求
    - 400 Bad Request：表示请求无效
    - 401 Unauthorized：表示未经授权
    - 404 Not Found：表示资源不存在
    - 500 Internal Server Error：表示服务器内部错误

- 使用合适的数据格式,JSON 是目前最常用的格式，它具有简洁、易读、易解析的特点。
    - JSON
    - XML

- 使用合适的版本控制,
如果 API 的接口可能会发生变化，应该考虑使用版本控制来管理接口的演进。可以在资源路径中包含版本号，或者使用自定义的请求头来指定版本号。
    - /api/v1
    - /api/v2

- 使用合适的身份认证和授权机制
对于需要保护的资源，应该使用适当的身份认证和授权机制
    - 基本认证
    - 令牌认证
    - OAuth

- 使用适当的过滤、排序和分页
对于返回大量数据的接口，应该提供过滤、排序和分页的功能，以便客户端能够按需获取数据。

- 提供合适的错误处理和错误信息
当出现错误时，应该提供清晰、有用的错误信息，以帮助开发者诊断和解决问题。


### Django简单场景示例
1. 安装python
2. 安装Django
3. 安装djangorestframework
4. Django MTV 模型和 Model示例
5. Django Admin演示
6. Django FBV & CBV

#### FBV代码示例
#### CBV代码示例


### Django常用场景示例
1. model创建
2. Django Admin示例
3. 使用View基础类完成CURD api接口。（重要）

完成。