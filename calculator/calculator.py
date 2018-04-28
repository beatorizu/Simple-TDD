class Calculator(object):

    def sum(self, valueA: float, valueB: float) -> float:
        return valueA + valueB

    def sub(self, valueA: float, valueB: float) -> float:
        return valueA - valueB

    def div(self, valueA: float, valueB: float) -> float:
        try:
            return valueA / valueB
        except ZeroDivisionError:
            raise ZeroDivisionError
