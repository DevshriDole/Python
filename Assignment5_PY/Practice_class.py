class Pharmacy:
    Medicine_name = ""
    Price = ""
    Expiry_date = ""

    def set_inventory(self, mn, p, ed):
        self.Medicine_name = mn
        self.Price = p
        self.Expiry_date = ed

    def get_inventory(self):
        print(f"Medicine information: \n Medicine name: {self.Medicine_name}\n Price: {self.Price}\n Expiry date: {self.Expiry_date}")

# if __name__ == '__main__':
#     pharmacy = Pharmacy()
# pharmacy.set_inventory(mn="Dolo650", p= 50, ed= '12-10-2025')

# pharmacy.get_inventory()

medicine_dict = {}
medicine_dict["Dolo650"] = Pharmacy("Dolo650", 50, "12-10-2025")
medicine_dict["Paracetamol"] = Pharmacy("Paracetamol", 35, "11-09-2025")
medicine_dict["Solvin_cold"] = Pharmacy("Solvin_cold", 80, "10-01-2026")

print("Enter medicine name for details:")

for i in medicine_dict: 