# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9

# with open('file1.txt', 'w') as data:
#     data.write('2*x**2 + 4*x + 5')
# with open('file2.txt', 'w') as data:
#     data.write('4*x**2 + 1*x + 4')
from importlib.resources import path
import re
import itertools


f1 = 'file1.txt'
f2 = 'file2.txt'
f3 = 'file3.txt'

def read_st(file):
    with open(str(file), 'r') as data:
        st = data.read()
    return st

def list_kort(st):
    st = st.replace('= 0', '') 
    st = re.sub("[*]", " ", st).split('+') 
    st = [char.split(' ') for char in st] 
    st = [[x for x in list if x] for list in st]
    for i in st:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    st = [tuple(int(x) for x in j if x != 'x') for j in st]
    return st


# сложение цифр без степеней
def sum_not_sqr(pol1, pol2):   
    x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
    for i in pol1 + pol2:        
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key = lambda r: r[1], reverse = True)
    return res

# итог

def sum_mn(pol):
    var = ['*x**'] * len(pol)
    coefs = [x[0] for x in pol]
    degrees = [x[1] for x in pol]
    new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
    for x in new_pol:
        if x[0] == '0': del (x[0])
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x**': del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1': 
            del x[-1]
            x[-1] = '*x'
        if len(new_pol)<=len(x)+1:
            x.append(' + ')
    new_pol = list(itertools.chain(*new_pol))
    return "".join(map(str, new_pol))

def write_to_file(file, pol):
    with open(file, 'w') as data:
        data.write(pol)

st1 = read_st(f1)
st2 = read_st(f2)
res_st1 = list_kort(st1)
res_st2 = list_kort(st2)

result = sum_mn(sum_not_sqr(res_st1, res_st2))
write_to_file(f3, result)

print(st1)
print(st2)
print(result)
