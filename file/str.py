from unicodedata import east_asian_width
def width(s) :
    '获取字符串宽度'
    t=0
    for i in s :
        if east_asian_width(i) in ('F','W','A') :
            t=t+2
        else :
            t=t+1
    return t
dw=['B','K','M','G','T','P','E','Z','Y']
def size(i) :
    '将字节数转为可读性较好的数'
    if i=='N/A' :
        return 'N/A'
    t=float(i)
    b=0
    while t > 10*2**10 and b<8 :
        b=b+1
        t=t/2**10
    global dw
    return "%.2f%s" %(t,dw[b])
def ftts(i) :
    '转换'
    if i=='d' :
        return '目录'
    elif i=='f' :
        return '文件'