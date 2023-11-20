# Simple Tic Tac Toe

def RNG(Isi):
    Combo = [[0,1,2],[3,4,5],[6,7,8],
             [0,3,6],[1,4,7],[2,5,8],
             [0,4,8],[2,4,6]]
    Nilai = []
    # Reduce chance player win
    # Check value each combination
    k = 0
    Terbaik = 0 
    for i in range(8):
        for j in range(3):
            if Isi[Combo[i][j]] == 'X':
                k += 1
            if Isi[Combo[i][j]] == 'O':
                k -= 1
        Nilai.append(k)
    # Take the best decision
    for i in range(len(Nilai)):
        Tmp = Nilai[i]
        if Tmp>Terbaik:
            Terbaik = Tmp
    # Fill it
    for i in range(3):
        if Isi[Combo[Terbaik][i]] == 'X':
            continue
        else:
            Komputer = Combo[Terbaik][i]
    return Komputer

def Papan(a,b,c,d,e,f,g,h,i):
    print('==========')
    print(f'| {a} | {b} | {c} |')
    print('==========')
    print(f'| {d} | {e} | {f} |')
    print('==========')
    print(f'| {g} | {h} | {i} |')
    print('==========')

def Main(Kotak=0, Isi=[], Bentuk='' ):
    Isi[Kotak] = Bentuk

def Cek_menang(Isi=[]):
    Combo = [[0,1,2],[3,4,5],[6,7,8],
             [0,3,6],[1,4,7],[2,5,8],
             [0,4,8],[2,4,6]]
    Win = 0
    for i in range(8):
        for j in range(3):
            if Isi[Combo[i][j]] == 'X':
                Win = Win + 1
            elif Isi[Combo[i][j]] == 'O':
                Win = Win - 1
    if Win == 3:
        print('Player Win')
    elif Win == -3:
        print('Bot Win')

Terisi = 0
Batas = 9
Komputer = 4
Isi = ['','','','','','','','','']
Papan(Isi[0], Isi[1], Isi[2], Isi[3], Isi[4], Isi[5], Isi[6], Isi[7], Isi[8])
while (Terisi<Batas):
    Orang = input('kotak mana yang ingin diisi : ')
    Orang = int(Orang)
    Main(Orang, Isi, 'X')
    Komputer = RNG(Isi)
    Main(Komputer, Isi, 'O')
    Papan(Isi[0], Isi[1], Isi[2], Isi[3], Isi[4], Isi[5], Isi[6], Isi[7], Isi[8])
    Cek_menang(Isi)
    Terisi += 1