- 方法``__init()___``
  - 形参self必不可少，且必须位于其他形参前面。
    - (相当于this指针)
  - 类中的每个方法都要有一个形参self

- 我们通常可以认为首字母大写的名称（如 Dog ）指的是类，而小写的名称（如 my_dog ）指的是根据类创建的实例

- ​

- 继承

  - 定义子类时，必须在括号内指定父类的
    名称。初始化时使用super()调用父类初始化方法
  - super() 是一个特殊函数，帮助 Python 将父类和子类关联起来。
    - 父类也称为 超类 （ superclass ），名称 super 因此而得名。

- 模块导入

  - ``from A import B`
    - 单个类|方法的导入
  - ``import a`
    - 导入整个类。 定义对象时要使用a.A (a是文件名， A是类名)
    -  module_name.class_name
  - ``from a import *``
    - 导入模块a中的所有类 ，极易发生命名冲突

- python标准库

  - OrderedDict类
    - ``from collections import OrderedDict``
    - 有序字典！
    - 字典让你能够将信息关联起来，但它们不记录你添加键 — 值对的顺序。要创建字典并记录其中的键 — 值对的添加顺序，可使用模块 collections 中的 OrderedDict类。 OrderedDict 实例的行为几乎与字典相同，区别只在于记录了键 — 值对的添加顺序
  - randint
    - ``from random import randint``
    - randint（a,b) 随机数生成




- 类名应采用 驼峰命名法 ，即将类名中的每个单词的首字母都大写，而不使用下划线。实例名和模块名都采用小写格式，并在单词之间加上下划线。

