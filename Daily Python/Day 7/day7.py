import fire

class TerminalCalculator():
#Init
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return num1 + num2

    def subtraction(self):
        if num1 > num2:
            return num1 - num2
        else:
            return num2 - num1

    def multiplicationh(self):
        return num1 * num2

    def division(self):
        return num1 / num2

    def modulos(self):
        return num1 % num2

fire.Fire(TerminalCalculator(30,5))