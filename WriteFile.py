
# save file
def save(url_output_file, re):
    try:
        file = open(url_output_file, 'a+',encoding='utf-8')
#First, we need to  estimate the type of re, which can be int, list,tuple, dic, str
        if isinstance(re,list):
            for k in re:
                if len(k) >0:
                    file.write(k.replace("\n","") )
                    file.write('\n')
        else:
            file.write(re.replace("\n","") )
            file.write('\n')
        file.close()
    except Exception as e:
        print (e)

#read file,way is r,rb; encoding is uft-8 or
def readFile(path,way,code):
    try:
        f = open(path, way,encoding=code)
        a = f.readlines()
    except Exception as e:
        print(e)
    return a