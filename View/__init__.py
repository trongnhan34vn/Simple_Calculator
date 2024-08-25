from SimpleCalculator.Model import Request
from SimpleCalculator.Controller import Controller
from SimpleCalculator.Model import Response


class View:
    def __init__(self):
        print("--------------------- Trang's Calculator ---------------------")
        print("1. Cộng")
        print("2. Trừ")
        print("3. Nhân")
        print("4. Chia")
        print("5. Exit")
        print("--------------------- Trang's Calculator ---------------------")

    @staticmethod
    def handleView(operation):
        print("Nhập số thứ nhất: ")
        num1 = int(input())
        print("Nhập số thứ hai: ")
        num2 = int(input())
        request = Request(num1, num2, operation)
        result = Controller().handleController(request)
        num1Str = str(request.num1)
        num2Str = str(request.num2)
        resultStr = str(result)
        Response(num1Str, num2Str, operation, resultStr)


