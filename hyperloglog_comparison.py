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
        pass
    except:
        pass
    return ip_addresses