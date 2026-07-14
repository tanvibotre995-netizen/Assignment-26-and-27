class Numbers:

    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False

        return True

    def ChkPerfect(self):
        sum = 0

        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum = sum + i

        if sum == self.Value:
            return True
        else:
            return False

    def Factors(self):
        print("Factors are :")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i)

    def SumFactors(self):
        sum = 0

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                sum = sum + i

        return sum


num = int(input("Enter number : "))

obj = Numbers(num)

print("Prime :", obj.ChkPrime())
print("Perfect :", obj.ChkPerfect())

obj.Factors()

print("Sum of Factors :", obj.SumFactors())
