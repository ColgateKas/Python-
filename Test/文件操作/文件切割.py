def save_file(fileNum, boyList, girlList):
    f2 = open('D:\\boy_'+ str(fileNum) +'.txt','a')
    f3 = open('D:\\gril_'+ str(fileNum) +'.txt','a')
        
    f2.writelines(boyList)
    f3.writelines(girlList)
        
    f2.close()
    f3.close()
    boyList.clear()
    girlList.clear()

def split_file(fileName):
    fileNum = 1
    boyList = []
    girlList = []
    f = open(fileName)
    for cont in f:
        print(cont)
        if '小甲鱼：' in cont:
            boyList.append(cont.replace('小甲鱼：',''))
        elif '小客服：' in cont:
            girlList.append(cont.replace('小客服：',''))

        elif '==' in cont:
            save_file(fileNum, boyList, girlList)
            fileNum += 1
    save_file(fileNum, boyList, girlList)
    f.close()

split_file('D:\\test.txt')
