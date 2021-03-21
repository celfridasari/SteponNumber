listAwal = [[4,2],[6,6],[3,4]] #data awal
def steponNumber(x): #fungsi steponNumber
    a = [] # untuk menampung hasil penjumlahan dari x,y di listawal
    for i in range(len(x)): # looping untuk menjumlahkan x,y di dalam list awal
        if x[i][0] % 2 == 0 and x[i][1]%2==0 and x[i][0] >= x[i][1] and (x[i][0]-x[i][1]==2 or x[i][0]-x[i][1]==0): #validasi untuk menampilkan output  x,y dari input/list awal
            a.append(x[i][0]+x[i][1]) #memasukan output x,y ke dalam list a 
        elif x[i][0] % 2 != 0 and x[i][1]%2 != 0 and x[i][0] >= x[i][1] and (x[i][0]-x[i][1]==2 or x[i][0]-x[i][1]==0): #validasi untuk menampilkan output  x,y dari input/list awal
            a.append(x[i][0]+x[i][1]-1) #memasukan output x,y ke dalam list a
        else:
            a.append('No Number') #output jika tidak memenuhi kedua validasi di atas dan dimasukkan ke list a
    return a #output dari fungsi steponNumber
print(steponNumber(listAwal))

#penjelasan : dari grafik dapat diketahui pattern nya sbb:
# 1. x selalu lebih besar atau sama dengan y
# 2. jika x dan y sama-sama bilangan genap maka output nya adalah x+y
# 3. jika x dan y sama-sama bilangan ganjil maka output nya adalah x+y-1
# 4. selisih antara x dan y hanya bisa 0 atau 2