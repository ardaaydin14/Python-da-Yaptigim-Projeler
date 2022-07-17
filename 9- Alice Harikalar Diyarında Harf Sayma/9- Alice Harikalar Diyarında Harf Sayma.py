file_path = "C:/Users/arda_/Masaüstü/alice29.txt"
metin = open(file_path, 'r')
lines = 0
words = 0
characters = 0
a_sayisi = 0
b_sayisi = 0
c_sayisi = 0
C_sayisi = 0
d_sayisi = 0
e_sayisi = 0
f_sayisi = 0
g_sayisi = 0
h_sayisi = 0
i_sayisi = 0
j_sayisi = 0
k_sayisi = 0
l_sayisi = 0
m_sayisi = 0
n_sayisi = 0
o_sayisi = 0
p_sayisi = 0
q_sayisi = 0
r_sayisi = 0
s_sayisi = 0
t_sayisi = 0
u_sayisi = 0
v_sayisi = 0
w_sayisi = 0
x_sayisi = 0
y_sayisi = 0
z_sayisi = 0

for line in metin:
    for karakter in line:
        if karakter =="a":
            a_sayisi = a_sayisi + 1


    for karakter in line:
        if karakter =="b" :
            b_sayisi = b_sayisi + 1
    for karakter in line:
        if karakter =="c" :
            c_sayisi = c_sayisi + 1
    for karakter in line:
        if karakter =="C" :
            C_sayisi = C_sayisi + 1
    for karakter in line:
        if karakter =="d":
            d_sayisi = d_sayisi + 1
    for karakter in line:
        if karakter =="e":
            e_sayisi = e_sayisi + 1
    for karakter in line:
        if karakter =="f":
            f_sayisi = f_sayisi + 1
    for karakter in line:
        if karakter =="g":
            g_sayisi = g_sayisi + 1
    for karakter in line:
        if karakter =="h":
            h_sayisi = h_sayisi + 1
    for karakter in line:
        if karakter =="i":
            i_sayisi = i_sayisi + 1
    for karakter in line:
        if karakter =="j":
            j_sayisi = j_sayisi + 1
    for karakter in line:
        if karakter =="k":
            k_sayisi = k_sayisi + 1
    for karakter in line:
        if karakter =="l":
            l_sayisi = l_sayisi + 1
    for karakter in line:
        if karakter =="m":
            m_sayisi = m_sayisi + 1
    for karakter in line:
        if karakter =="n":
            n_sayisi = n_sayisi + 1
    for karakter in line:
        if karakter =="o":
            o_sayisi = o_sayisi + 1
    for karakter in line:
        if karakter =="p":
            p_sayisi = p_sayisi + 1
    for karakter in line:
        if karakter =="q":
            q_sayisi = q_sayisi + 1
    for karakter in line:
        if karakter =="r":
            r_sayisi = r_sayisi + 1
    for karakter in line:
        if karakter =="s":
            s_sayisi = s_sayisi + 1
    for karakter in line:
        if karakter =="t":
            t_sayisi = t_sayisi + 1
    for karakter in line:
        if karakter =="u":
            u_sayisi = u_sayisi + 1
    for karakter in line:
        if karakter =="v":
            v_sayisi = v_sayisi + 1
    for karakter in line:
        if karakter =="w":
            w_sayisi = w_sayisi + 1
    for karakter in line:
        if karakter =="x":
            x_sayisi = x_sayisi + 1
    for karakter in line:
        if karakter =="y":
            y_sayisi = y_sayisi + 1
    for karakter in line:
        if karakter =="z":
            z_sayisi = z_sayisi + 1





























    wordslist = line.split()
    lines = lines + 1
    words = words + len(wordslist)
    characters = characters + len(line)
print("number of lines =", (lines))
print("number of words =",(words))
print("number of characters =",(characters))
print("number of letter a =",(a_sayisi))
print("number of letter b =",(b_sayisi))
print("number of letter c =",(c_sayisi+C_sayisi))
print("number of letter d =",(d_sayisi))
print("number of letter e =",(e_sayisi))
print("number of letter f =",(f_sayisi))
print("number of letter g =",(g_sayisi))
print("number of letter h =",(h_sayisi))
print("number of letter i =",(i_sayisi))
print("number of letter j =",(j_sayisi))
print("number of letter k =",(k_sayisi))
print("number of letter l =",(l_sayisi))
print("number of letter m =",(m_sayisi))
print("number of letter n =",(n_sayisi))
print("number of letter o =",(o_sayisi))
print("number of letter p =",(p_sayisi))
print("number of letter q =",(q_sayisi))
print("number of letter r =",(r_sayisi))
print("number of letter s =",(s_sayisi))
print("number of letter t =",(t_sayisi))
print("number of letter v =",(v_sayisi))
print("number of letter w =",(w_sayisi))
print("number of letter x =",(x_sayisi))
print("number of letter y =",(y_sayisi))
print("number of letter z =",(z_sayisi))