import pandas as pd
student={
    "name":["archana","bhagyashri","vaishnavi"],
    "marks":[89,78,53],
    "city":["sangli","pune","nanded"]
}

df=pd.DataFrame(student)
print(df)

# output- pandas gives data in tabular format like this
#          name  marks    city
# 0     archana     89  sangli
# 1  bhagyashri     78    pune
# 2   vaishnavi     53  nanded
