import pandas
a=pandas.Series(["john","Blake","Martin"])
print(a)#by-default indexing is in integer it starts from as usual 0
print(a[0])#john
print(a[1])#Blake

#pandas support labeled indexing
#labeled index- a,b,c 

labeled_index=pandas.Series(["john","Blake","Martin"],index=['a','b','c'])
print(labeled_index)
#a      john
# b     Blake
# c    Martin
# dtype: object
print(labeled_index.a)#john
print(labeled_index['a'])#john
print(labeled_index['b'])#Blake