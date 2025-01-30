import time

def main():
    print("🚀 Python сервер запущен. Ожидание команд...")
    while True:
        command = input(">>> ")
        if command.lower() in ["exit", "quit"]:
            print("👋 Выход из сервера...")
            break
        else:
            try:
                exec(command)
            except Exception as e:
                print(f"⚠ Ошибка: {e}")

if __name__ == "__main__":
    main()
