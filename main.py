from transaction import*
from menu import*

trnsc1 = Transaction()
menu = Menu()

while True:
    choice = menu.main_menu()
    if choice == 1:
        while True:
            add_item_again = trnsc1.add_item()

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
                    update_item_again = trnsc1.update_item_name()
                elif update_choice == 2:
                    update_item_again = trnsc1.update_item_qty()
                elif update_choice == 3:
                    trnsc1.update_price_per_item()

            if not update_item_again:
                break

    elif choice == 3:
        while True:
            if len(trnsc1.list_items) < 1:
                print("Belum ada pesanan yang anda buat")
                break
            else:
                delete_choice = menu.delete_item()
                if delete_choice == 1:
                    is_delete_item_again = trnsc1.delete_item()
                    if len(trnsc1.list_items) < 1:
                        break
                    else:
                        if not is_delete_item_again:
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
                    get_total_price = trnsc1._get_choice_1_2("Ingin melihat total belanja anda?")
                    if get_total_price:
                        trnsc1.total_price()
                        user_pay = trnsc1._get_choice_1_2("Lanjut lakukan pembayaran")
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
