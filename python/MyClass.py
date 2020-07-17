# 创建类
class MyClass:
    # 定义属性
    name = "chenxuan"
    age = "24"
    # 私有属性
    __private_attrs = "__private_attrs"
     # 类的私有方法
    def __private_method():
       return "__private_method"
    # 定义函数
    def my_fun(x,y):
        return x+y
    # 类的方法
    def hello(self):
        # 类名
        print(self.__class__)
        # 函数返回值
        return 'hello world'
    # 访问私有属性
    print(__private_attrs)
    # 访问私有方法
    print(__private_method())

# 访问函数
print(MyClass.my_fun(2,3))
# 实例化类
x = MyClass()
# 访问类的属性
print(x.name)
print(x.age)
# 访问类的方法
print(x.hello())
