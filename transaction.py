class Transaction:
    def __init__(self):
        self.list_items = {}
    
    def add_item(self):
        print(("\n"+"-" * 15 + " Menu Buat Pesanan " + "-" * 15 +"\n"))

        while True:
            item_name = input("Nama item: ")
            is_item_name_empty = self._is_item_name_empty(item_name)
            if not is_item_name_empty:
                continue
            normalize_item_name = self._normalize_name(item_name)
            if normalize_item_name in self.list_items:
                print(f"Peringatan: Item {item_name} sudah ada dalam daftar.")
                print("\n1. Lanjut tambah item lain" \
                "2. Kembali ke menu awal untuk update item")
                is_choice_num_1 =  self._get_choice_1_2("Pilih menu")
                if not is_choice_num_1:
                    break
        while True:
            try:
                item_qty = int(input("Jumlah item: "))
                is_item_qty_less_than_1 = self._is_less_than_1(item_qty)
                if not is_item_qty_less_than_1:
                    break
                else:
                    print("Error: Tidak boleh angka 0 atau minus")
            except ValueError:
                print('Error: Salah input, hanya input angka saja')
        while True:    
            try:
                price_per_item = int(input("Harga per item: "))
                is_price_per_item_less_than_1 = self._is_less_than_1(price_per_item)
                if not is_price_per_item_less_than_1:
                    break
                else:
                    print("Error: Tidak boleh angka 0 atau minus")
            except ValueError:
                print('Error: Salah input, hanya input angka saja')

        self.list_items[normalize_item_name] = {
            "Original Name": item_name,
            "Quantity": item_qty,
            "Price per Item": price_per_item
        }

        self.display_order("Item yang dibeli adalah:")

        return self._get_y_n_choice("Tambah item lagi?")
    
    def update_item_name(self):
        while True:
            old_item_name = input("Nama item lama: ")
            if not old_item_name.strip():
                print("Nama item tidak boleh kosong")
                continue
            normalize_old_item_name = self._normalize_name(old_item_name)
            if normalize_old_item_name in self.list_items:
                break
            else:
                print("Error: Tidak ditemukan nama item yang dimasukkan")
        while True:
            new_item_name = input("Nama item baru: ")
            normalize_new_item_name = self._normalize_name(new_item_name)
            if normalize_new_item_name in self.list_items and normalize_new_item_name != normalize_old_item_name:
                print(f"Peringatan: Item {new_item_name} sudah ada dalam daftar.")
                print("\n1. Lanjut update nama item" \
                "2. Kembali ke menu sebelumnya")
                is_choice_num_1 =  self._get_choice_1_2("Pilih menu")
                if not is_choice_num_1:
                    break
            else:
                break
        tmp = self.list_items.pop(normalize_old_item_name)
        self.list_items[normalize_new_item_name] = tmp
        self.list_items[normalize_new_item_name]["Original Name"] = new_item_name
        self.display_order(f"Item yang dibeli adalah\n" 
                            f"(setelah merubah nama item {old_item_name} "
                            f"menjadi {new_item_name})")
        
        return self._get_y_n_choice("Update item lagi?")
    
    def update_item_qty(self):
        while True:
            item_name = input("Nama item: ")
            if not item_name.strip():
                print("Nama item tidak boleh kosong")
                continue
            normalize_item_name = self._normalize_name(item_name)
            if normalize_item_name in self.list_items:
                break
            else:
                print(f'Error: {item_name} tidak ditemukan')
                print("\n1. Lanjut update nama item" \
                "2. Kembali ke menu sebelumnya")
                is_choice_num_1 =  self._get_choice_1_2("Pilih menu")
                if not is_choice_num_1:
                    break
        while True:
            try:
                new_item_qty = int(input("Jumlah item baru: "))
                is_item_qty_less_than_1 = self._is_less_than_1(new_item_qty)
                if not is_item_qty_less_than_1:
                    break
                else:
                    print("Error: Tidak boleh angka 0 atau minus")
            except ValueError:
                print('Error: Salah input, hanya input angka saja')
        if self.list_items[normalize_item_name]["Quantity"] != new_item_qty:
            self.list_items[normalize_item_name]["Quantity"] = new_item_qty
            self.display_order(f"Item yang dibeli adalah\n" 
                               f"(setelah merubah jumlah item {item_name} "
                               f"menjadi {new_item_qty})")
            
            return self._get_y_n_choice("Update item lagi?")
        
    def update_price_per_item(self):
        while True:
            item_name = input("Nama item: ")
            if not item_name.strip():
                print("Nama item tidak boleh kosong")
                continue
            normalize_item_name = self._normalize_name(item_name)
            if normalize_item_name in self.list_items:
                break
            else:
                print(f'Error: {item_name} tidak ditemukan')
                print("\n1. Lanjut update nama item" \
                "2. Kembali ke menu sebelumnya")
                is_choice_num_1 =  self._get_choice_1_2("Pilih menu")
                if not is_choice_num_1:
                    break
        while True:
            try:
                new_price_per_item = int(input("Jumlah item baru: "))
                is_item_qty_less_than_1 = self._is_less_than_1(new_price_per_item)
                if not is_item_qty_less_than_1:
                    break
                else:
                    print("Error: Tidak boleh angka 0 atau minus")
            except ValueError:
                print('Error: Salah input, hanya input angka saja')
        
        if self.list_items[normalize_item_name]["Price per Item"] != new_price_per_item:
            self.list_items[normalize_item_name]["Price per Item"] = new_price_per_item
            self.display_order(f"Item yang dibeli adalah\n"
                               f"(setelah merubah harga per item {item_name} "
                               f"menjadi Rp.{new_price_per_item}")
            
            return self._get_y_n_choice("Update item lagi?")
    
    def delete_item(self):
        while True:
            item_name = input("Nama item: ")
            if not item_name.strip():
                print("Nama item tidak boleh kosong")
                continue
            normalize_item_name = self._normalize_name(item_name)
            if normalize_item_name in self.list_items:
                break
            else:
                print(f'Error: {item_name} tidak ditemukan')
                print("\n1. Lanjut hapus item" \
                "2. Kembali ke menu sebelumnya")
                is_choice_num_1 =  self._get_choice_1_2("Pilih menu")
                if not is_choice_num_1:
                    break

        del self.list_items[normalize_item_name]

        if len(self.list_items) < 1:
            print(f"\nSemua item berhasil dihapus")
            return False
        else:
            self.display_order(f"Item yang dibeli adalah\n"
                               f"(setelah menghapus item {self.item_name})")
            
            return self._get_y_n_choice("Hapus item lagi?")
    
    def reset_transaction(self):
        self.list_items.clear()
        print("Semua item berhasil di-delete!\n")
    
    def check_order(self):
        for item_name in self.list_items:

            if (not self.list_items[item_name].get('Original Name', '').strip() or
                self.list_items[item_name].get('Quantity', 0) <= 0 or
                self.list_items[item_name].get('Price per Item', 0) <= 0):
                return False
            
        return True
    
    def display_order(self, prompt):
        print(f"\n{prompt}")
        print("+"+"-"*4 + "+"+"-"*14 + "+"+"-"*13 + "+"+"-"*12 + "+")
        print("| No " + "| Nama Item ".ljust(15) + "| Jumlah Item " + "| Harga/Item |")
        print("+"+"-"*4 + "+"+"-"*14 + "+"+"-"*13 + "+"+"-"*12 + "+")
        
        for num, item_name in enumerate(self.list_items):
            print(f"| {num+1} ".ljust(5) + f"| {self.list_items[item_name]["Original Name"]} ".ljust(15) 
                  + f"| {self.list_items[item_name]["Quantity"]} ".ljust(14) 
                  + f"| {self.list_items[item_name]["Price per Item"]} ".ljust(13) + "|")
        
        print("+"+"-"*4 + "+"+"-"*14 + "+"+"-"*13 + "+"+"-"*12 + "+")
    
    def display_total_order(self):
        self.total_price_per_item()
        print("+"+"-"*4 + "+"+"-"*14 + "+"+"-"*13 + "+"+"-"*12 + "+"+"-"*13+"+")
        print("| No " + "| Nama Item ".ljust(15) + "| Jumlah Item " + "| Harga/Item " + "| Total Harga | ")
        print("+"+"-"*4 + "+"+"-"*14 + "+"+"-"*13 + "+"+"-"*12 + "+"+"-"*13+"+")
        
        for num, item_name in enumerate(self.final_list_items):
            print(f"| {num+1} ".ljust(5) + f"| {self.final_list_items[item_name]["Original Name"]} ".ljust(15) 
                  + f"| {self.final_list_items[item_name]["Quantity"]} ".ljust(14) 
                  + f"| {self.final_list_items[item_name]["Price per Item"]} ".ljust(13) 
                  + f"| {self.final_list_items[item_name]["Total Price"]}".ljust(13) + " |")
        
        print("+"+"-"*4 + "+"+"-"*14 + "+"+"-"*13 + "+"+"-"*12 + "+"+"-"*13+"+")

    def total_price_per_item(self):
        self.final_list_items = self.list_items.copy()
        for item_name in self.final_list_items:
            self.final_list_items[item_name]['Total Price'] = (
                self.final_list_items[item_name]['Quantity'] *
                self.final_list_items[item_name]['Price per Item']
                )
        return self.final_list_items
    
    def total_price(self):
        total_price_every_item = [self.final_list_items[item_name]['Total Price'] 
                                  for item_name in self.final_list_items]
        total_price_all_item = sum(total_price_every_item)
        diskon = 0
        if total_price_all_item > 500000:
            diskon = 0.1
        elif total_price_all_item > 300000:
            diskon = 0.08
        elif total_price_all_item > 200000:
            diskon = 0.05
        total_price_all_item_after_discount = total_price_all_item - (total_price_all_item*diskon)
        # Improved clarity:
        if diskon > 0:
            print(f'Anda mendapatkan diskon sebanyak {diskon*100:.0f}% '
                  f'karena telah berbelanja senilai Rp.{total_price_all_item:,.0f} (sebelum diskon).')
            print(f'\nTotal Belanja yang harus dibayarkan adalah Rp.{total_price_all_item_after_discount:,.0f}')
        else:
            print(f'\nTotal Belanja yang harus dibayarkan adalah Rp.{total_price_all_item_after_discount:,.0f}')
    
    def _get_y_n_choice(self, prompt):
        while True:
            again = input(f"\n{prompt} (y/n): ")
            again = again.lower()
            
            if again == 'n':
                return False
            elif again == 'y':
                return True
            else:
                print('Error: Salah input, hanya input sesuai pilihan (y/n)')
    
    def _normalize_name(self, name):
        """Normalizes an item name for consistent comparison."""
        return name.strip().replace(" ", "").lower()
    
    def _get_choice_1_2(self, prompt):
        while True:
            try:
                user_input = int(input(f"\n{prompt} (1/2): "))
                if user_input == 1:
                    return True
                elif user_input == 2:
                    return False
                else:
                    print('Error: Salah input, hanya input sesuai pilihan (1/2)')
            except ValueError:
                print('Error: Salah input, hanya input sesuai pilihan (1/2)')
    
    def _is_item_name_empty(self, item_name):
        if not item_name.strip():
            return True # Ini berarti "ya, nama item ini kosong/hanya spasi"
        return False # Ini berarti "tidak, nama item ini tidak kosong"
    
    def _is_less_than_1(self, data):
        if data < 1:
            return True
        return False
