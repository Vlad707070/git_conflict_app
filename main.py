def add(a, b):
    return a + b

def main():
    print("=== Калькулятор ===")
    print("1. Сложение")
    choice = input("Выберите операцию: ")
    
    if choice == "1":
        x = float(input("Число 1: "))
        y = float(input("Число 2: "))
        print(f"Результат: {add(x, y)}")

if __name__ == "__main__":
    main()
