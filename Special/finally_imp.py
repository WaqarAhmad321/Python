# finally keyword is always executed whether the value is returned or not
def func():
    try:
        l = [1, 2, 3, 4]
        i = int(input("Enter an index :"))
        print(l[i])
        return 1
    except:
        print("Invalid Input!")
        return 0
    finally:
        print("I will always execute.")


x = func()
print(x)
