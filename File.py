from time import sleep
file = open("C:/Users/lixiangyang/PycharmProjects/study/venv/1.txt",'r',encoding='utf-8')
text = file.read()
sleep(1)
print(text)
file.close()
