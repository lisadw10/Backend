list_Menu = ['Makanan', 'Minuman' , 'Snack']
list_Makanan = ["Steak","Nasi Goreng","Mie Goreng","Ayam Geprek","Bakso","Mie Ayam","Lalapan"]
list_Minuman = ["Es Jus","Soda Gembira","Orange Juice","Lemon Tea","MilkShake","Es Campur","Air Mineral"]
list_Snack = ["Kentang Goreng","Tahu Walik","Tahu Petis","Sosis Bakar","Cireng","Pisang Goreng"]

nota = []
while True:
    print('~~~~~~~~Selamat Datang di Resto Mantap~~~~~~~~')
    print('Menu Restoran:')
    for Menu in range(0, len(list_Menu)):
        print(f'{Menu + 1}. {list_Menu[Menu]} ')
    Menu = input('Masukkan Menu Pilihan Anda: ')
    if Menu == '1':
        print ("~~~~Menu Makanan~~~~")
        for Menu_Makanan in range(0, len(list_Makanan)):
            print(f'{Menu_Makanan + 1}. {list_Makanan[Menu_Makanan]} ')
        ulang = True
        while ulang :
            Makanan = int(
                input(f'Silahkan Pilih Makanan 1-{len(list_Makanan)} '))
            if Makanan <= 0 or Makanan > len(list_Makanan):
                print("===================")
                print('Menu tidak ditemukan')
                for menu_Makanan in range(0, len(list_Makanan)):
                    print(f'{Menu_Makanan + 1}. {list_Makanan[Menu_Makanan]} ')
                continue
            else:
                nota.append(list_Makanan[Makanan - 1])
                print('Keranjang Belanja Anda:')
                print("===================")
                for list_nota in range(0, len(nota)):
                    print(f'{list_nota +1} . {nota[list_nota]}')
                ulang = False
            continue
    elif Menu == '2':
        print ("~~~~Menu Minuman~~~~")
        for Menu_Minuman in range(0, len(list_Minuman)):
            print(f'{Menu_Minuman + 1}. {list_Minuman[Menu_Minuman]} ')
        ulang = True
        while ulang :
            Minuman = int(input(f'Silahkan Pilih Minuman 1-{len(list_Minuman)} '))
            if Minuman <= 0 or Minuman > len(list_Minuman):
                print("===================")
                print('Menu tidak ditemukan')
                for Menu_Minuman in range(0, len(list_Minuman)):
                    print(f'{Menu_Minuman + 1}. {list_Minuman[Menu_Minuman]} ')
                continue
            else:
                nota.append(list_Minuman[Minuman - 1])
                print('Keranjang Belanja Anda')
                print("===================")
                for list_nota in range(0, len(nota)):
                    print(f'{list_nota +1} . {nota[list_nota]}')
                ulang = False
            continue
    elif Menu == '3':
        print ("~~~~Menu Snack~~~~")
        for Menu_Snack in range(0, len(list_Snack)):
            print(f'{Menu_Snack + 1}. {list_Snack[Menu_Snack]} ')
        ulang = True
        while ulang :
            Snack = int(input(f'Silahkan Pilih Snack 1-{len(list_Snack)} '))
            if Snack <= 0 or Snack > len(list_Snack):
                print("===================")
                print('Menu tidak ditemukan')
                for Menu_Snack in range(0, len(list_Snack)):
                    print(f'{Menu_Snack + 1}. {list_Snack[Menu_Snack]} ')
                continue
            else:
                nota.append(list_Snack[Snack - 1])
                print('Keranjang Belanja Anda')
                print("===================")
                for list_nota in range(0, len(nota)):
                    print(f'{list_nota +1} . {nota[list_nota]}')
                ulang = False
            continue
    else :
        print('Menu tidak ditemukan')
        continue
    lanjut = input('Pesan Lagi ?')
    if lanjut == 'y':
        continue
    else:
        print('Keranjang Belanja Anda')
        print("===================")
        for list_nota in range(0, len(nota)):
            print(f'{list_nota +1} . {nota[list_nota]}')
        print('TerimaKasih, Pesanan Akan Segera Diantar')
        break