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
    
    def _hash(self, item, seed):
        """
        Генерує хеш-значення для елемента з використанням seed.
        """
        hash_obj = hashlib.md5()
        hash_obj.update(f"{item}{seed}".encode('utf-8'))
        return int(hash_obj.hexdigest(), 16) % self.size
    
    def add(self, item):
        if item is None or item == "":
            return

        item = str(item)
        for seed in range(self.num_hashes):
            index = self._hash(item, seed)
            self.bit_arr[index] = 1   

    def contains(self, item):
        if item is None or item == "":
            return
        item = str(item)
        for seed in range(self.num_hashes):
            index= self._hash(item, seed)
            if self.bit_arr[index] == 0:
                return False
        return True
    
def check_password_uniqueness(bloom_filter, new_passwords):
    """
    Перевіряє унікальність списку нових паролів.
    
    Параметри:
    - bloom_filter: екземпляр BloomFilter з існуючими паролями
    - new_passwords: список паролів для перевірки
    
    Повертає: словник {пароль: статус}
    """
    results = {}
    for passw in new_passwords:
        if bloom_filter.contains(passw):
            results[passw] = "already used"
        else:
            results[passw] = "unique"
    return results




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
