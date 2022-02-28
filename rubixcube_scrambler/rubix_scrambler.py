#Rubix cube scrambler
list = ['R', 'R Prime', 'L', 'L Prime', 'F', 'F Prime', 'U', 'U Prime', 'D', 'D Prime', 'B', 'B Prime','M', 'M Prime' ]
import random as r
def sa():
    ans =  r.choice(list)
    return ans
print(sa())