def bubble_sort(datas):
    for x in datas:  
        for i in range(0,len(datas)-1):
            if datas[i]>datas[i+1]:
                temp=datas[i+1]
                datas[i+1]=datas[i]
                datas[i]=temp
    print(datas)


datas=[7,1,3,9,4,6]
print(datas)
bubble_sort(datas)      
