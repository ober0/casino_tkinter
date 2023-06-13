text1=0
text2=0
text3=0
text4=0
text5=0
text6= 0
text7=0
text8=0
text9=0
text10=0


with open('history.txt', 'r')as file:
    text = file.read()
    text = text.split()
    for i in range(1,11):
        text10 = text9
        text9 = text8
        text8 = text7
        text7 = text6
        text6 = text5
        text5 = text4
        text4 = text3
        text3 = text2
        text2 = text1
        text1 = text[-i]
print(text10)
