class ExceptionPrintData(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return  f"Err: {self.message}"

class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"Печать: {str(data)}")

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintData('Принтер игнорит')

    def send_to_print(self, data):
        return False

p = PrintData()
try:
    print(p.print("123"))

except ExceptionPrintData:
    print("Принтер проигнорил жёска")