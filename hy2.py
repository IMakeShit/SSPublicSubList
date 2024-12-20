import socket
import sys

def extract_ip(input_string):
    # Отсечем все перед '@' и после '#'
    try:
        ip_part = input_string.split('@')[1].split('#')[0]
        return ip_part.split(':')[0]  # Возвращаем только IP без порта
    except IndexError:
        return None

def check_ip(ip_address):
    try:
        # Проверяем доступность IP адреса
        socket.gethostbyaddr(ip_address)
        return True
    except socket.herror:
        return False
    except socket.gaierror:  # Обработка ошибки "Name or service not known"
        return False

def main(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()  # Убираем пробелы и символы новой строки
                ip_address = extract_ip(line)

                if ip_address:
                    # Проверка работоспособности IP адреса
                    if check_ip(ip_address):
                        print(f"{line}")
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":  # Исправлено с name на __name__
    if len(sys.argv) != 2:
        print("Использование: python script.py <имя_файла>")
    else:
        main(sys.argv[1])

