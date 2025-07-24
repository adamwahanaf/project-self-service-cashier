from transaction import*

class Menu:
    def __init__(self):
        pass

    def main_menu(self):
        print(("\n"+"-" * 15 + " Python Cashier " + "-" * 15))
        print("1. Buat Pesanan\n"
            "2. Perbarui Pesanan\n"
            "3. Hapus Pesanan\n"
            "4. Cek pesanan\n"
            "5. Keluar")
        
        return self.get_menu_choice("\nPilih Menu (1/2/3/4/5): ", 5)
    
    def update_item(self):
        print(("\n"+"-" * 15 + " Menu Perbarui Pesanan " + "-" * 15 +"\n"))
        print("1. Perbarui nama item\n"
          "2. Perbarui jumlah item\n"
          "3. Perbarui harga per item\n")
        
        return self.get_menu_choice("\nPilih Menu (1/2/3): ", 3)
    
    def delete_item(self):
        print(("\n"+"-" * 15 + " Menu Hapus Pesanan " + "-" * 15 +"\n"))
        print("1. Hapus satu item\n"
          "2. Hapus seluruh item\n")
        
        return self.get_menu_choice("\nPilih Menu (1/2): ", 2)
    
    def total_price(self):
        print(("/n"))
        print("1. Lihat total belanja anda\n"
          "2. Kembali ke menu awal\n")
        
        return self.get_menu_choice("\nPilih Menu (1/2): ", 2)
    
    def get_menu_choice(self, prompt, number_of_menu):
        while True:
            self.prompt = prompt
            self.number_of_menu = number_of_menu
            self.choice = input(f"{self.prompt}")
            
            try:
                self.choice = int(self.choice)
                if 1 <= self.choice <= number_of_menu:
                    return self.choice
                else:
                    print('Error: Salah input, hanya input sesuai pilihan menu diatas')
            except ValueError:
                print('Error: Salah input, hanya input sesuai pilihan menu diatas')
