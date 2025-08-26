class MyFibbo:
    def fibboSeries(self, n):
        print("Fibbo series print: ")
        a, b = 0, 1
        for _ in range(n):
            print(a, end=", ")
            a, b = b, a+b

obj = MyFibbo()
n = int(input("Enter a fibbo series range: "))
obj.fibboSeries(n)
