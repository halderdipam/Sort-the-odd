def sort_array(source_array):
    o=[]
    for i in source_array:
        if i%2!=0:
            o.append(i)
    os = sorted(o)
    r=[]
    for i in  source_array:
        if i%2 !=0:
            r.append(os.pop(0))
        else:
            r.append(i)  
    return r
