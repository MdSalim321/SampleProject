class FibboSeries:
    def fibbo(self, n):
        a, b = 0, 1
        for _ in range(n):
            print(a, " ")
            a, b=b, a+b

num = int(input("Enter a number: "))
obj = FibboSeries()
obj.fibbo(num)

