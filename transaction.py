class Transaction:
    def __init__(self):
        self.list_items = []
    
    def add_item(self):
        print(("\n"+"-" * 15 + " Menu Buat Pesanan " + "-" * 15 +"\n"))
        
        self.item_name = input("Nama item: ")
        self.item_name = self.item_name.title()

        while True:
            try:
                self.item_qty = int(input("Jumlah item: "))
                break
            except ValueError:
                print('Error: Salah input, hanya input angka saja')
        while True:    
            try:
                self.price_per_item = int(input("Harga per item: "))
                break
            except ValueError:
                print('Error: Salah input, hanya input angka saja')

        self.list_items.append({
            "Item Name" : self.item_name,
            "Quantity": self.item_qty,
            "Price per Item": self.price_per_item
        })

        return self.display_order("Item yang dibeli adalah:")
    
    def update_item_name(self):
        while True:
            
            self.old_item_name = input("Nama item lama: ")
            self.old_item_name = self.old_item_name.title()
            
            for item in self.list_items:
                if item["Item Name"] == self.old_item_name:
                    self.new_item_name = input("Nama item baru: ")
                    self.new_item_name = self.new_item_name.title()
                    item["Item Name"] = self.new_item_name
                    return self.display_order(f"Item yang dibeli adalah\n" 
                                              f"(setelah merubah nama item {self.old_item_name} "
                                              f"menjadi {self.new_item_name})")
            
            print("Error: Tidak ditemukan nama item yang dimasukkan")
    
    def update_item_qty(self):
        while True:
            
            self.item_name = input("Nama item: ")
            self.item_name = self.item_name.title()

            self.match_name = any([item["Item Name"] == self.item_name for item in self.list_items])
            if self.match_name:
                break
            else:
                print("Error: Tidak ditemukan nama item yang dimasukkan")

        while True:
            try:
                self.new_item_qty = int(input("Jumlah item baru: "))
                if self.new_item_qty > 0:
                    for item in self.list_items:
                        if item["Item Name"] == self.item_name and item["Quantity"] != self.new_item_qty:
                            item["Quantity"] = self.new_item_qty
                            return self.display_order(f"Item yang dibeli adalah\n" 
                                              f"(setelah merubah jumlah item {self.item_name} "
                                              f"menjadi {self.new_item_qty} buah)")
                else:
                    print("Error: Jumlah item tidak boleh kurang dari 1")
            except ValueError:
                print('Error: Salah input, hanya input angka saja')
        
    
    def update_price_per_item(self):
        while True:
            
            self.item_name = input("Nama item: ")
            self.item_name = self.item_name.title()

            self.match_name = any([item["Item Name"] == self.item_name for item in self.list_items])
            if self.match_name:
                break
            else:
                print("Error: Tidak ditemukan nama item yang dimasukkan")
        
        while True:
            try:
                self.new_price_per_item = int(input("Jumlah item baru: "))
                if self.new_price_per_item > 0:
                    for item in self.list_items:
                        if item["Item Name"] == self.item_name and item["Price per Item"] != self.new_price_per_item:
                            item["Price per Item"] = self.new_price_per_item
                            return self.display_order(f"Item yang dibeli adalah\n" 
                                              f"(setelah merubah harga per item {self.item_name} "
                                              f"menjadi {self.new_price_per_item} buah)")
                else:
                    print("Error: harga per item tidak boleh 0")
            except ValueError:
                print('Error: Salah input, hanya input angka saja')
    
    def delete_item(self):
        while True:
            
            self.item_name = input("Nama item: ")
            self.item_name = self.item_name.title()

            self.match_name = any([item["Item Name"] == self.item_name for item in self.list_items])
            if self.match_name:
                break
            else:
                print("Error: Tidak ditemukan nama item yang dimasukkan")

        self.new_list_items = [item for item in self.list_items if item["Item Name"] != self.item_name]

        self.list_items = self.new_list_items

        if len(self.list_items) < 1:
            return f"\nSemua item berhasil dihapus"
        else:
            return self.display_order(f"Item yang dibeli adalah\n"
                                      f"(setelah menghapus item {self.item_name})")
    
    def reset_transaction(self):
        self.list_items.clear()
        print("Semua item berhasil di-delete!\n")
    
    def check_order(self):
        for item in self.list_items:

            if (not item.get('Item Name', '').strip() or
                item.get('Quantity', 0) <= 0 or
                item.get('Price per Item', 0) <= 0):
                return False
            
        return True
    
    def display_order(self, prompt):
        self.prompt = prompt
        print(f"\n{self.prompt}")
        print("+"+"-"*4 + "+"+"-"*14 + "+"+"-"*13 + "+"+"-"*12 + "+")
        print("| No " + "| Nama Item ".ljust(15) + "| Jumlah Item " + "| Harga/Item |")
        print("+"+"-"*4 + "+"+"-"*14 + "+"+"-"*13 + "+"+"-"*12 + "+")
        
        for num, item in enumerate(self.list_items):
            print(f"| {num+1} ".ljust(5) + f"| {item['Item Name']} ".ljust(15) + f"| {item['Quantity']} ".ljust(14) + f"| {item['Price per Item']} ".ljust(13) + "|")
        
        print("+"+"-"*4 + "+"+"-"*14 + "+"+"-"*13 + "+"+"-"*12 + "+")
    
    def display_total_order(self):
        self.total_price_per_item()
        print("+"+"-"*4 + "+"+"-"*14 + "+"+"-"*13 + "+"+"-"*12 + "+"+"-"*13+"+")
        print("| No " + "| Nama Item ".ljust(15) + "| Jumlah Item " + "| Harga/Item " + "| Total Harga | ")
        print("+"+"-"*4 + "+"+"-"*14 + "+"+"-"*13 + "+"+"-"*12 + "+"+"-"*13+"+")
        
        for num, item in enumerate(self.final_list_items):
            print(f"| {num+1} ".ljust(5) + f"| {item['Item Name']} ".ljust(15) + f"| {item['Quantity']} ".ljust(14) + f"| {item['Price per Item']} ".ljust(13) + f"| {item['Total Price']}".ljust(13) + " |")
        
        print("+"+"-"*4 + "+"+"-"*14 + "+"+"-"*13 + "+"+"-"*12 + "+"+"-"*13+"+")

    def total_price_per_item(self):
        self.final_list_items = self.list_items.copy()
        for item in self.final_list_items:
            item['Total Price'] = item['Quantity']*item['Price per Item']
        return self.final_list_items
    
    def total_price(self):
        self.total_price_every_item = [item["Total Price"] for item in self.final_list_items if item['Total Price'] !=0]
        self.total_price_all_item = sum(self.total_price_every_item)
        print("+"+"-"*4 + "+"+"-"*14 + "+"+"-"*13 + "+"+"-"*12 + "+"+"-"*13+"+")
        print("| No " + "| Nama Item ".ljust(15) + "| Jumlah Item " + "| Harga/Item " + "| Total Harga | ")
        print("+"+"-"*4 + "+"+"-"*14 + "+"+"-"*13 + "+"+"-"*12 + "+"+"-"*13+"+")
        
        for num, item in enumerate(self.final_list_items):
            print(f"| {num+1} ".ljust(5) + f"| {item['Item Name']} ".ljust(15) + f"| {item['Quantity']} ".ljust(14) + f"| {item['Price per Item']} ".ljust(13) + f"| {item['Total Price']}".ljust(13) + " |")
        
        print("+"+"-"*4 + "+"+"-"*14 + "+"+"-"*13 + "+"+"-"*12 + "+"+"-"*13+"+")
        print(f'\nTotal Belanja yang harus dibayarkan adalah Rp.{self.total_price_all_item}')
    
    def transaction_again(self, prompt):
        self.prompt = prompt
        while True:
            self.again = input(f"\n{self.prompt} (y/n): ")
            self.again = self.again.lower()
            
            if self.again == 'n':
                return False
            elif self.again == 'y':
                return True
            else:
                print('Error: Salah input, hanya input sesuai pilihan (y/n)')
    
    



