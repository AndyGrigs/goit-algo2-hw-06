import re
import time
from hyperloglog import HyperLogLog

def load_data(filename):
    """
    Завантажує IP-адреси з лог-файлу.
    
    Параметри:
    - filename: шлях до лог-файлу
    
    Повертає: список IP-адрес
    """
    ip_addresses = []
    # Регулярний вираз для пошуку IP-адрес
    # Формат: XXX.XXX.XXX.XXX (де XXX - це 1-3 цифри)
    ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

    try:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file: 
                match = ip_pattern.search(line)
                if match:
                    ip_addresses.append(match.group())
    except FileNotFoundError:
        print(f"Error: file {filename} not found!")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []
    return ip_addresses

def set_counting(ip_addresses):
    """
    Точний підрахунок унікальних IP-адрес за допомогою set.
    
    Параметри:
    - ip_addresses: список IP-адрес
    
    Повертає: кількість унікальних IP-адрес"""
    unique_ips = set(ip_addresses)
    return len(unique_ips)

def hll_counting(ip_addresses):

    """
    Наближений підрахунок унікальних IP-адрес за допомогою HyperLogLog.
    
    Параметри:
    - ip_addresses: список IP-адрес
    
    Повертає: приблизна кількість унікальних IP-адрес
    """
    hll = HyperLogLog(0.01)
    for ip in ip_addresses:
        hll.add(ip)
    
    return len(hll)

def compare_counts(ip_addresses):
    """
    Порівнює точний підрахунок та HyperLogLog.
    
    Параметри:
    - ip_addresses: список IP-адрес
    
    Повертає: словник з результатами
    """

    results = {}

    # Точний підрахунок
    start_time = time.time()
    exact_count = set_counting(ip_addresses)
    exact_time = time.time() - start_time
    # HyperLogLog підрахунок
    start_time = time.time()
    hll_count = hll_counting(ip_addresses)
    hll_time = time.time() - start_time

    # Збираємо результати
    results['exact'] = {
        'count': exact_count,
        'time': exact_time
    }
    results['hll'] = {
        'count': hll_count,
        'time': hll_time
    }

    return results



def print_results(results):
    """
    Виводить результати порівняння у вигляді таблиці.
    
    Параметри:
    - results: словник з результатами від compare_methods
    """
    print("\nРезультати порівняння:")
    print(f"{'':25} {'Точний підрахунок':>20} {'HyperLogLog':>15}")
    print(f"{'Унікальні елементи':25} {results['exact']['count']:>20.1f} {results['hll']['count']:>15.1f}")
    print(f"{'Час виконання (сек.)':25} {results['exact']['time']:>20.2f} {results['hll']['time']:>15.2f}")

def main():
    """Головна функція програми."""
    # Назва лог-файлу
    filename = "lms-stage-access.log"
    
    print(f"Завантаження даних з файлу '{filename}'...")
    ip_addresses = load_data(filename)
    
    if not ip_addresses:
        print("Не вдалося завантажити дані. Перевірте файл.")
        return
    
    print(f"Завантажено {len(ip_addresses)} записів.")
    print("Виконання порівняння методів...")
    
    # Порівняння методів
    results = compare_counts(ip_addresses)
    
    # Виведення результатів
    print_results(results)


if __name__ == "__main__":
    main()