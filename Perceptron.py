import numpy as np

w1 = [0, 1, 0]
x1 = [2, 1, -1]
d1 = -1
x2 = [0, -1, -1]
d2 = 1
c = 0.1
w2 = [0, 0, 0]
# stop=0->se verifica daca signum1(net)=d1 si signum2(net)=d2
# stop=1 cand se realizeaza o corectie
stop = 0


def verificare_d1(w, x1,i=[0]):
    i[0]+=1
    print("\nPasul ",i)
    print("Verificare d1")
    net = np.dot(w, x1)
    print("net=", net)
    sign = np.sign(net)
    if sign != d1:
        print("Sign(net)!=d1=> are loc o corectie a ponderilor")
        for i in range(0, 3):
            w[i] = w[i] + c * (d1 - sign) * x1[i]
        print("Noile ponderi sunt:", w)
        stop = 1
    else:
        print("Nu se realizeaza nicio corectie, sign(net)=d1")
        stop = 0
    return stop


def verificare_d2(w, x2):
    print("Verificare d2")
    net = np.dot(w, x2)
    print("net=", net)
    sign = np.sign(net)
    if sign != d2:
        print("Sign(net)!=d1=> are loc o corectie a ponderilor")
        for i in range(0, 3):
            w[i] = w[i] + c * (d2 - sign) * x2[i]
        print("Noile ponderi sunt:", w)
        stop = 1
    else:
        print("Nu se realizeaza nicio corectie, sign(net)=d2")
        stop = 0
    return stop


while stop != 1:
    # se opreste cand nu se mai realizeaza nicio corectie, nici pt d1, nici pt d2
    if verificare_d1(w1, x1) == 0 and verificare_d2(w1, x2) == 0:
        stop = 1
print('\nPonderile finale sunt:')
print(w1)
