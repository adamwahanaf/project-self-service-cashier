from transaction import*
from menu import*

trnsc1 = Transaction()
menu = Menu()

while True:
    choice = menu.main_menu()
    if choice == 1:
        while True:
            trnsc1.add_item()
            
            add_item_again = trnsc1.transaction_again("Tambah item lagi?")
            
            if not add_item_again:
                break

    elif choice == 2:
        while True:
            if len(trnsc1.list_items) < 1:
                print("Belum ada pesanan yang anda buat")
                break
            else:
                update_choice = menu.update_item()
                if update_choice == 1:
                    trnsc1.update_item_name()
                elif update_choice == 2:
                    trnsc1.update_item_qty()
                elif update_choice == 3:
                    trnsc1.update_price_per_item()
            
            update_item_again = trnsc1.transaction_again("Ingin perbarui data item lain?")
            
            if not add_item_again:
                break

    elif choice == 3:
        while True:
            if len(trnsc1.list_items) < 1:
                print("Belum ada pesanan yang anda buat")
                break
            else:
                delete_choice = menu.delete_item()
                if delete_choice == 1:
                    trnsc1.delete_item()
                    if len(trnsc1.list_items) < 1:
                        break
                    else:
                        update_item_again = trnsc1.transaction_again("Ingin hapus item lain?")
                        
                        if not add_item_again:
                            break

                elif delete_choice == 2:
                    trnsc1.reset_transaction()
                    break
    elif choice == 4:
        while True:
            if len(trnsc1.list_items) < 1:
                print("Belum ada pesanan yang anda buat")
                break
            else:
                valid_input = trnsc1.check_order()
                if valid_input:
                    print("\nPemesanan sudah benar")
                    trnsc1.display_total_order()
                    get_total_price = trnsc1.transaction_again("Ingin melihat total belanja anda?")
                    if get_total_price:
                        trnsc1.total_price()
                        user_pay = trnsc1.transaction_again("Lanjut lakukan pembayaran")
                        if user_pay:
                            print("Terima Kasih Telah Berbelanja!!")
                            break
                        else:
                            break
                    else:
                        break
                else:
                    print("\nTerdapat kesalahan input data")
                    trnsc1.display_total_order()
                    break

    elif choice == 5:
        break
        


"""pilih_menu = input("1/2/3/4")


if pilih_menu == "1":
    while True:
        item_name = input("nama item: ")
        item_qty = int(input("jumlah item: "))
        price_per_item = int(input("harga per item"))
        list_items = trnsc1.add_item(item_name=item_name, item_qty=item_qty, price_per_item=price_per_item)

        ulang = input("y/n: ")
        if ulang == 'n':
            break"""