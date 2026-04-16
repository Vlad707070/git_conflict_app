def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def main():
    print("=== Калькулятор ===")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    choice = input("Выберите операцию: ")
    
    if choice == "1":
        x = float(input("Число 1: "))
        y = float(input("Число 2: "))
        print(f"Результат: {add(x, y)}")
    elif choice == "2":
        x = float(input("Число 1: "))
        y = float(input("Число 2: "))
        print(f"Результат: {sub(x, y)}")
    elif choice == "3":
        x = float(input("Число 1: "))
        y = float(input("Число 2: "))
        print(f"Результат: {mul(x, y)}")

if __name__ == "__main__":
    main()
