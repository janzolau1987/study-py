# Python爬虫框架Scrapy入门样例
##1.创建一个Scrapy项目
在开始爬取之前，必须创建一个新的Scrapy项目。进入打算存储代码的目录中，运行下列命令：
```shell
scrapy startproject tutorial
```
该命令将会创建下列目录:
```shell
tutorial/
    scrapy.cfg
    tutorial/
        __init__.py
        items.py
        pipelines.py
        settings.py
        spiders/
            __init.py
            ...
```

这些文件分别是:
```shell
scrapy.cfg : 项目的配置文件
tutorial/ : 该项目的python模块
tutorial/items.py : 项目中的item文件
tutorial/piplines.py : 项目中的pipelines文件
tutorial/settings.py : 项目的设置文件
tutorial/spiders/ : 放置spider代码的目录
```

##2.定义提取的Item
Item是保存爬取到的数据窗口；其使用方法和python字典类似，并且提供额外保护机制来避免拼写错误导致的未定义字段错误。
类似在ORM中做的一样，可以通过创建一个scrapy.Item类，并且定义类型为scrapy.Field的类属性来定义一个Item。
见tutorials/items.py

##3.编写爬取网站的spider并提取Item
Spider是用户编写用于从单个网站(或者一些网站)爬取数据的类。其包含一个用于下载的初始URL，如何跟进网页中的连接以及如何分析页面中的内容，提取生成Item的方法。
为了创建一个Spider，必须继承scrapy.Spider类，且定义以下三个属性：
> name : 用于区别Spider。该名字必须是唯一的，不可以为不同的Spider设定相同的名字。
> start_urls : 包含了Spider在启动时进行爬取的url列表。因此，第一个被获取到的页面将是其中之一。后续的URL则从初始的URL获取到的数据中提取。
> parse() : 是Spider的一个方法。被调用时，每个初始化URL完成下载后生成的Reponse对象将会作为唯一的参数传递给该函数。该方法负责解析返回的数据(response.data)，提取数据(生成item)以及生成需要进一步处理的URL的Request对象。
    见tutorials/spiders/dmoz_spider.py

###爬取
进入项目的根目录，执行下列命令启动Spider:
```shell
scrapy crawl dmoz
```
Scrapy为Spider的start_urls属性中的每个URL创建了scrapy.Request对象，并将parse方法作为回调函数(callback)赋值给Request。
Request对象经过调度，执行生成scrapy.http.Response对象并送回给spider parse()方法。

###提取Item
Selectors选择器简介
从网页中提取数据有很多方法。Scrapy使用一种基于XPath和CSS表达式机制：Scrapy Selectors。
这里给出XPath表达式的例子及对应含义:

    > /html/head/title : 选择HTML文档中<head>标签内的<title>元素
    > /html/head/title/text() : 选择上面提到的<title>元素的文字
    > //td : 选择所有的<td>元素
    > //div[@class="mine"] : 选择所有具有class="mine"属性有div元素

为了配合XPath,Scrapy除了提供了Selector之外，还提供了方法来避免每次从response中提取数据时生成selector的麻烦。
Selector有四个基本的方法:

    > xpath() : 传入xpath表达式，返回该表达式所对应的所有节点的selector list列表。
    > css() : 传入css表达式，返回该表达式所对应的所有节点的selector list列表
    > extract() : 序列化该节点的unicode字符串并返回list列表
    > re() : 根据传入的正则表达式对数据进行提取，返回unicode字符串list列表

###提取数据
可以通过这段代码选择该页面中网站列表里所有&lt;li&gt;元素:
```python
response.xpath('//ul/li')
```
网站的描述:
```python
response.xpath('//ul/li/text()').extract()
```
网站的标题:
```python
response.xpath('//ul/li/a/text()').extract()
```
网站的连接:
```python
response.xpath('//ul/li/a/@href').extract()
```

之前提到过，每个.xpath()调用返回selector组成的list，因此可以拼接更多的.xpath()来进一步获取某个节点。
```python
for sel in response.xpath('//ul/li'):
    title = sel.xpath('a/text()').extract()
    link = sel.xpath('a/@href').extract()
    desc = sel.xpath('text()').extract
    print title, link, desc
```
###使用Item
Item对象是自定义的python字典。可以使用标准的字典语法来获取到其每个字段的值。
```shell
>>> item = DmozItem()
>>> item['title'] = 'Example title'
>>> item['title']
```
一般来说，Spider将会把爬取到的数据以Item对象返回。

###保存爬取到的数据
最简单存储爬取的数据的方式是使用Feed exports：
```shell
scrapy crawl dmoz -o items.json
```
该命令将采用JSON格式对爬取的数据进行序列化，生成items.json文件。

在类似本篇教程里这样小规模的项目中，这种存储方式已经足够。 如果需要对爬取到的item做更多更为复杂的操作，您可以编
写 Item Pipeline 。 类似于我们在创建项目时对Item做的，用于您编写自己的 tutorial/pipelines.py 也被创建。不过
如果您仅仅想要保存item，您不需要实现任何的pipeline。

##4.编写Item Pipeline来存储提取到的Item(即数据)