
# Service xử lý logic
class Service:
    @classmethod
    def plus(cls, request):
        return request.num1 + request.num2

    @classmethod
    def minus(cls, request):
        return request.num1 - request.num2

    @classmethod
    def multiple(cls, request):
        return request.num1 * request.num2

    @classmethod
    def divide(cls, request):
        return request.num1 / request.num2

    # handle các logic thành 1 method
    @classmethod
    def handle(cls, request):
        match request.operation:
            case "+":
                return Service().plus(request)
            case "-":
                return Service().minus(request)
            case "*":
                return Service().multiple(request)
            case "/":
                return Service().divide(request)
