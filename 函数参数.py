
def add_end(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L

def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum


#def person(name,age,*,city,job):
  #  if 'city' in kw:
  #      pass
  #  if 'job' in kw:
  #      pass
#    print('name:',name,'age:',age,'other',city,job)

#extra={'city':'beijing' , 'job': 'engineer'}
#person('Michael',30,city='chaoyang',job=123456)
def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

f1(1,2)
f1(1,2,c=3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)
f1(1,2,d=99,ext=None)
f2(1,2,d=99,ext=None)
print('\n')
args=(1,2,3,4)
kw={'d':99 , 'x':'#'}
f1(*args,**kw)
args=(1,2,3)
kw={'d':88, 'x': '#'}
f2(*args, **kw)

