def vcompare(ver, upstream_ver):
    '''Using ossvt.natsort we compare ver and upstream_ver'''
    ver_split = ver.split('.')
    upsteram_ver_split = upstream_ver.split('.')
    count = 0
    for i in upsteram_ver_split:
        if ver_split[count] == upsteram_ver_split[count]:
            count += 1
            continue
        else:
            if int(ver_split[count]) < int(upsteram_ver_split[count]):
                return upstream_ver
            else:
                break
