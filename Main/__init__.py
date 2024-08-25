import sys

from SimpleCalculator.View import View


class SimpleCalculator:
    @staticmethod
    def render():
        while True:
            View()
            print("Nhập vào lựa chọn của bạn: ")
            choice = int(input())
            operation = ""

            # switch case với từng th của choice
            match choice:
                case 1:
                    print("Cộng")
                    operation = "+"
                case 2:
                    print("Trừ")
                    operation = "-"
                case 3:
                    print("Nhân")
                    operation = "*"
                case 4:
                    print("Chia")
                    operation = "/"
                case 5:
                    print("Bye!")
                    sys.exit(0)

            View.handleView(operation)
            SimpleCalculator.backToMenu()

    # chịu trách nhiệm khởi chạy ứng dụng
    @staticmethod
    def main():
        SimpleCalculator.render()

    # hiển thị yêu cầu quay lại menu
    @staticmethod
    def backToMenu():
        while True:
            print("Press '0' to back to menu")
            choice = int(input())
            if choice == 0:
                SimpleCalculator.render()
                break

# gọi hàm để khởi chạy ứng dụng
SimpleCalculator().main()
