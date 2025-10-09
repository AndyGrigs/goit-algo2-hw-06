import  hashlib

class BloomFilter:
    """
    Фільтр Блумича для перевірки унікальності елементів.
    
    Параметри:
    - size: розмір бітового масиву
    - num_hashes: кількість хеш-функцій
    """
    def __init__(self, size, num_hashes):
        """Ініціалізація фільтру"""
        self.size = size # Це розмір бітового масиву
        self.num_hashes = num_hashes # Тут кількість функцій
        self.bit_arr = [0] * size # Народження нульового біт масиву
    
    def hash():
        pass
        



if __name__ == "__main__":
    # Ініціалізація фільтра Блума
    bloom = BloomFilter(size=1000, num_hashes=3)

    # Додавання існуючих паролів
    existing_passwords = ["password123", "admin123", "qwerty123"]
    for password in existing_passwords:
        bloom.add(password)

    # Перевірка нових паролів
    new_passwords_to_check = ["password123", "newpassword", "admin123", "guest"]
    results = check_password_uniqueness(bloom, new_passwords_to_check)

    # Виведення результатів
    for password, status in results.items():
        print(f"Пароль '{password}' - {status}.")
