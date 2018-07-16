##任一个英文的纯文本文件，统计其中的单词出现的个数。


def readtxt(text):
    text = open('%s' %text ,'r')
    txt = text.readline()
    txt = str(txt)
    txtbox = txt.split()
    text.close()
    b='单词量为:'+str(len(txtbox))

    return b


if __name__ == '__main__':
    filaddress = input('请输入txt文本的地址\n')
    print(readtxt(filaddress))