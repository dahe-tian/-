def ZuHeIndex(li):
    reli = []
    for i in range(0, len(li)):
        if 0 == i:
            reli.append(li[i])
        else:
            addli = []
            addli.append(li[i])
            for ii in reli:
                addli.append(ii+'","'+li[i])
                # print(ii+','+li[i])
            reli += addli
    return reli
li=['A','B','C','D']
a = ZuHeIndex(li)
for i in range(0,15):
    print('["'+a[i]+'"]')

