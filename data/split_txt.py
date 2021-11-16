def split():
    f = open(r"txt\a.txt",'r',encoding='UTF8')
    f2=open(r"txt\crawling.txt","w",encoding='UTF8')
    data=f.read()
    word=data.split()
    num=0
    for i in range(len(word)):
        num+=len(word[i])+1
        if num>11:
            f2.write("\n")
            num=len(word[i])+1
            while(num>11):
                print(word[i])
                res=list(word[i])
                longword=''.join(res[:10])
                f2.write(longword)
                f2.write("\n")
                del res[:10]
                word[i]=''.join(res)
                num=len(word[i])+1

        f2.write(word[i])
        f2.write(" ")
    f.close()
    f2.close()

