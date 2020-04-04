
s="""1 23 3 42 3 56
44 1 5 71 9 35"""
def judge(s):
    num_str = s.split('\n')
    # print(num_str)
    res=list()
    for i in range(len(num_str)):
        res.append(num_str[i].split(' '))
    result=list()
    for item in res:
        for i in item:
            if int(item[0])>=10 and int(item[-1])>=10:
                for j in item[1:-1]:
                    if int(j)>10:
                        result.append('false')
                        break
                    else:
                        result.append('true')
            elif int(item[0])<10 and int(item[-1])<10:
                for j in item[1:-1]:
                    if int(j) < 10:
                        result.append('false')
                        break
                    else:
                        result.append('true')
            else:
                pass
    return ' '.join(result)

judge(s)


