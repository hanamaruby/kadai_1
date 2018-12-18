from StudentCard import StudentCard

class MainShopCharger:
    #method 1
    def insert_student_card(self, student_id):
        self.inserted_student_card = StudentCard.get_student_card(student_id)

    #method2
    def charge_money(self, money):
        if self.inserted_student_card is not None:
            self.inserted_student_card.account_balance += money
        else:
            print('Student ID card is not inserted.')

    #method3
    def print_account_balance(self):
        print('Display the balance')
        print('Name:' + self.inserted_student_card.student_name)
        print('Balance:' + str(self.inserted_student_card.account_balance))

    #Execution test
    def main(self):
        student_card_1 = StudentCard(0, "Atsushi")
        student_card_2 = StudentCard(1, "Kanako")

        self.insert_student_card(0)
        self.charge_money(100000000)
        self.print_account_balance()

        self.insert_student_card(1)
        self.charge_money(870)
        self.print_account_balance()
        self.charge_money(445)
        self.print_account_balance()


if __name__ == '__main__':
    main_shop_charger = MainShopCharger()
    main_shop_charger.main()
