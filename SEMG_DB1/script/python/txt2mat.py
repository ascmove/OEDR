import scipy.io as sio
import os

filename = '..\\..\\src\\A_TXT\\1Amar.txt'
matname = '.\\.out\\A_TXT\\1Amar.mat'

colname_1  = 'Recto_Femoral'
colname_2  = 'Biceps_Femoral'
colname_3  = 'Vasto_Medial'
colname_4  = 'EMG_Semitendinoso'
colname_5  = 'Flexo_Extension'

if not os.path.isdir('.\\.out\\A_TXT\\'):
    os.mkdir('.\\.out\\A_TXT\\')

with open(filename) as fp:
    i = 0

    col_1 = []
    col_2 = []
    col_3 = []
    col_4 = []
    col_5 = []
    for line in fp:
        i += 1
        if i < 8:
            continue

        line = line.strip('\n')
        vctr = line.split("	")
        if (vctr[0] == '') or (vctr[1] == '') or (vctr[2] == '') or (vctr[3] == '') or (vctr[4] == ''):
            continue
        col_1.append(float(vctr[0]))
        col_2.append(float(vctr[1]))
        col_3.append(float(vctr[2]))
        col_4.append(float(vctr[3]))
        col_5.append(float(vctr[4]))

    sio.savemat(matname, {colname_1: [col_1],colname_2: [col_2],colname_3: [col_3],colname_4: [col_4],colname_5: [col_5]})