- 文件打开

  - ``with open('filename') as file_object:``

  - 使用关键字with ， 可以自动在不需要访问文件后将其关闭。

  - 读取： contents=file_object.read()

    - 逐行读取:
      - ``for line in file_object``
    -  readlines() 从文件中读取每一行，并将其存储在一个列表中

  - 文件路径：在 Windows 系统中，在文件路径中使用反斜杠（ \ ）而不是斜杠（ / ）

    - 绝对路径通常比相对路径更长，因此将其存储在一个变量中，再将该变量传递给 open() 会有所帮助
- 异常
  - try :
  - except ValueError:
  - else :
- 存储数据
  - ``json.dump(data,file)`` 和 ``json.load``(file)
  - 可以不用考虑str int类型的问题。直接使用dump和load存储和读取即可。
- ​

