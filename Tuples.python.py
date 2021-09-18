from collections import defaultdict
test_list=[(5,6),(5,7),(6,8),(7,13)]
print("The original list is :"+str(test_list))
mapp=defaultdict(list)
for key,val in test_list:
    mapp[key].append(val)
res=[(key,*val) for key,val in mapp.items()]
print("The extracted elements:"+str(res))
