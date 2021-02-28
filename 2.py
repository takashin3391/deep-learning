import numpy as np

def AND1(x1,x2):
    w1,w2,theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

def AND2(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b=-0.7
    tmp = np.sum(x*w)+b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x)+b
    if(tmp<=0):
        return 0
    else:
        return 1

def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2
    tmp = np.sum(x*w)+b
    if(tmp<=0):
        return 0
    else:
        return 1

def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND2(s1,s2)
    return y


def main():
    a = XOR(0,0)
    print('(0,0):%d' %a)
    a = XOR(1,0)
    print('(1,0):%d' %a)
    a = XOR(0,1)
    print('(0,1):%d' %a)
    a = XOR(1,1)
    print('(1,1):%d' %a)

if __name__ == "__main__":
    main()