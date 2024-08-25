from SimpleCalculator.Service import Service

# Controller nhận request của view và lấy kết quả từ service trả về
class Controller:
    @classmethod
    def handleController(cls, request):
        return Service().handle(request)
