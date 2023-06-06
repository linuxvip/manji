# Django Api接口框架
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


---
DRF 接口实现

### 继承GenericAPIView原因
之前rest框架最基础的view里面继承的是APIview，现在我们升级一下，继承``GenericAPIView``。

GenericAPIView是继承APIView的，使用完全兼容APIView，主要增加了操作序列化器和数据库查询的方法，
作用是为下面Mixin扩展类的执行提供方法支持。通常在使用时，可以配合一个或多个Mixin扩展类

重点：`GenericAPIView`在`APIView`基础上完成了哪些事
 1. `get_queryset()`：从类属性queryset中获得model的queryset数据   
    
 2. `get_object()`：从类属性queryset中获得model的queryset数据

 3. `get_serializer()`：从类属性serializer_class中获得serializer的序列化类

也就是封装了继承APIview里面的一些方法。

继承GenericAPIView之后提供的关于序列化器使用的属性与方法
关于序列化器属性
以下的这两个属性名字不能变，是`GenericAPIView`类里面的属性
 `queryset` 指明视图需要的数据（model查询数据）
 `serializer_class` 指明视图使用的序列化器　
 举个例子：
```
    """列表视图"""
    # 指定序列化器类
    serializer_class = BookInfoModelSerializer
    # 指定查询集'数据来源'
    queryset = BookInfo.objects.all()
```
提供的关于数据库查询的属性与方法
1. `get_queryset()` 从类属性queryset中获得model的queryset数据，查询多个数据

2. `get_object()` 从类属性queryset中获得model的queryset数据，再通过有名分组pk来确定唯一操作对象, 也就是获取详情数据

3. `get_serializer()` 从类属性serializer_class中获得serializer的序列化类，主要用来提供给Mixin扩展类使用。 获取序列化器对象

#### 继承GenericAPIView实现查询全部
```
    """以下是继承GenericAPIView的视图"""
class BookListGenericView(GenericAPIView):
    """列表视图"""
    # 指定序列化器类
    serializer_class = BookInfoModelSerializer
    # 指定查询集'数据来源'
    queryset = BookInfo.objects.all()

    def get(self, request):
        qs = self.get_queryset()  # 获取到数据集
        serializer = self.get_serializer(qs, many=True)  # 得到序列化器对象
        return Response(serializer.data)  # 从序列化器对象里面拿出数据返回
```
继承`GenericAPIView`查询一个，也就是详情

```
class BookDetailGenericView(GenericAPIView):
    """详情视图"""
    # 指定序列化器类
    serializer_class = BookInfoModelSerializer
    # 指定查询集'数据来源'
    queryset = BookInfo.objects.all()

    def get(self, request, pk):
        book = self.get_object()  #get_object()方法根据pk参数查找queryset中的数据对象
        serializer = self.get_serializer(book)
        return Response(serializer.data)
```

继承GenericAPIView 进行修改数据
```
class BookDetailGenericView(GenericAPIView):
    """详情视图"""
    # 指定序列化器类
    serializer_class = BookInfoModelSerializer
    # 指定查询集'数据来源'
    queryset = BookInfo.objects.all()

    def put(self, request, pk):
        book = self.get_object()  # 查询出指定pk的数据
        serializer = self.get_serializer(book, request.data) # 获取序列化器对象
        serializer.is_valid(raise_exception=True)  #  验证成功
        serializer.save()  #  更新
        return Response(serializer.data)  # 将更新的数据返回
```
#### 路由
```
    # # 列表视图的路由GenericAPIView
    url(r'^books/$', views.BookListGenericView.as_view()),
    # 详情视图的路由GenericAPIView
    url(r'^books/(?P<pk>\d+)/$', views.BookDetailGenericView.as_view()),
```
---

### 为什么要用 mixins视图工具集
之前只是继承了GenericAPIView。代码还是比较多，现在再次升级一下，不仅仅要继承GenericAPIView，还要多继承一些东西，让代码变少，具体还要继承什么？

作用：提供了几种后端视图（对数据资源的增删改查）处理流程的实现，如果需要编写的视图属于这五种，则视图可以通过继承相应的扩展类来复用代码，减少自己编写的代码量。

这五个扩展类需要搭配GenericAPIView父类，因为五个扩展类的实现需要调用GenericAPIView提供的序列化器与数据库查询的方法。

### 5个mixins视图工具集
1. mixins有五个工具类文件，一共提供了五个工具类，六个工具方法：单查、群查、单增、单删、单整体改、单局部改

2. 继承工具类可以简化请求函数的实现体，但是必须继承GenericAPIView，需要GenericAPIView类提供序列化器与数据库查询的方法

3. 工具类的工具方法返回值都是Response类型对象，如果要格式化数据格式再返回给前台，可以通过 response.data 拿到工具方法返回的Response类型对象的响应数据

### 五个工具类：
 CreateModelMixin（增加）,
 DestroyModelMixin（删除）,
 ListModelMixin（查询,查queryset）, 查询list集合
 RetrieveModelMixin（查询，查对象，针对于存在"pk"）, 查询详情
 UpdateModelMixin（修改）
 
 
#### 查询list集合
1. ListModelMixin（群查）

列表视图扩展类，提供 list 方法快速实现查询视图，返回200状态码。除了查询，该list方法会对数据进行过滤和分页

```
"""以下是GenericAPIView和mixin的混合使用视图"""
class BookListGenericView(ListModelMixin, GenericAPIView):
    """列表视图"""
    # 指定序列化器类
    serializer_class = BookInfoModelSerializer
    # 指定查询集'数据来源'
    queryset = BookInfo.objects.all()

    def get(self, request):
        return self.list(request)  #  ListModelMixin里面有list方法

```


#### 新增数据
2. CreateModelMixin（单增）

创建视图扩展类，提供create方法快速创建资源的视图，成功返回201的状态码
```
"""以下是GenericAPIView和mixin的混合使用视图"""
class BookListGenericView(CreateModelMixin, ListModelMixin, GenericAPIView):
    """列表视图"""
    # 指定序列化器类
    serializer_class = BookInfoModelSerializer
    # 指定查询集'数据来源'
    queryset = BookInfo.objects.all()

    def post(self, request):
        return self.create(request)

```

### 单查和修改
3. RetrieveModelMixin(单查)

详情视图扩展类，提供retrieve方法，可以快速实现返回一个存在的数据对象。

4. UpdateModelMixin(更新，修改) 

更新视图扩展类，提供update方法，可以快速实现更新一个存在的数据对象，同时也提供partial_update方法，可以实现局部更新。
```
class BookDetailGenericView(UpdateModelMixin, RetrieveModelMixin, GenericAPIView):
    """详情视图"""
    # 指定序列化器类
    serializer_class = BookInfoModelSerializer
    # 指定查询集'数据来源'
    queryset = BookInfo.objects.all()

    def get(self, request, pk):
        return self.retrieve(request, pk)  # 单查

    def put(self, request, pk):
        return self.update(request, pk)  # 修改
```

### 路由
```
# # 列表视图的路由GenericAPIView
url(r'^books/$', views.BookListGenericView.as_view()),
# 详情视图的路由GenericAPIView
url(r'^books/(?P<pk>\d+)/$', views.BookDetailGenericView.as_view()),

```