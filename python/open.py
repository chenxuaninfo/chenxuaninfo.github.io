# 写文件打开
f = open("./data/data.txt","w")
# 插入一行
f.write("hello,world!\n")
# 插入一行
f.write("hello,python!\n")
# 插入多行
f.writelines(["hello\n","vscode!\n"])
f.close()

# 读取文件
f = open("./data/data.txt","r")
txt = f.read()
print(txt)


# 写文件打开
f = open("./data/data.txt","a")
# 插入一行
f.write("你好,中国!\n")
# 关闭
f.close()

# 读取文件
f = open("./data/data.txt","r")
txt = f.read()
print(txt)
