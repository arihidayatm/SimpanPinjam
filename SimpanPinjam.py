np = []
na = []
sp = []
sw = []
lma = []
td = 'y'
x = 0

while td.lower() == 'y':
    print('Entry Data Pinjaman Koperasi')
    print('============================')
    np.append(input('No Pinjaman           :'))
    na.append(input('Nama Anggota          :'))
    sp.append(input('Simpanan Pokok        :'))
    sw.append(input('Simpanan Wajib        :'))
    lma.append(input('Lama Menjadi Anggota  :'))
    x += 1
    td = input('Ada data lagi ?[Y/T]; ')

print('Laporan Data Rekening Pinjaman Koperasi ')
print('SIMPAN PINJAM XYZ ')
print('=======================================================================================================================')
print('| N0 |   NP  | Nama Anggota     | Simpanan Pokok | Simpanan Wajib | Lama Menjadi Anggota | Jumlah Pinjaman | Jumlah Angsuran |')
print('=======================================================================================================================')

t15 = 0
t10 = 0
t_10 = 0

for i in range(x):
    if int(lma[i]) >= 15:
        jp = round(200 / 100 * (int(sp[i]) + int(sw[i])))
        t15 += 1
    elif int(lma[i]) >= 10:
        jp = round(175 / 100 * (int(sp[i]) + int(sw[i])))
        t10 += 1
    else:
        jp = round(150 / 100 * (int(sp[i]) + int(sw[i])))
        t_10 += 1

    tb = 15 / 100
    la = 12
    ja = round((tb / la * jp) + (jp * 1 / 12))

    print(f'| {i + 1:2d} | {np[i]:4} | {na[i]:15} |  {sp[i]:12} |    {sw[i]:12} | {lma[i]:15} | {jp:15} | {ja:15} |')

print('=======================================================================================================================')
print(f'Total anggota dengan lama jadi anggota >= 15: {t15} Orang')
print(f'Total anggota dengan lama jadi anggota >= 10: {t10} Orang')
print(f'Total anggota dengan lama jadi anggota < 10: {t_10} Orang')


