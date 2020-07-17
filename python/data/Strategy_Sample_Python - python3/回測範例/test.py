# -*- coding: UTF-8 -*-

#取得報價資訊，詳情請查看技巧51
#execfile('function.py')   execfile在python3中已被废除，代替函数：exec(open(filename).read())
exec(open("function.py", encoding = 'utf-8').read())

for i in getMatch():		

  UpDn5Info=getLastUpDn5()
  print(getLastOrder())