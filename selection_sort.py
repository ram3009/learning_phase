def selection_sort(datas):
    for i in range(len(datas)):                #loop based on th no of items in list
        min_pos=i
        for j in range(i,len(datas)):
            if datas[j]<datas[min_pos]:
                min_pos=j
        temp=datas[i]
        datas[i]=datas[min_pos]
        datas[min_pos]=temp
        print(datas)


datas=[9,8,2,6,5,1,7]
print(datas)
selection_sort(datas)
