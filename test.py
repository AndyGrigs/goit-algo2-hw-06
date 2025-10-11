# Тестування (потім видалиш)
import hashlib

item = "password123"
seed = 0
size = 1000

hash_obj = hashlib.md5()
hash_obj.update(f"{item}{seed}".encode('utf-8'))
hex_hash = hash_obj.hexdigest()
big_number = int(hex_hash, 16)
index = big_number % size

print(f"Рядок для хешування: {item}{seed}")
print(f"Hex хеш: {hex_hash}")
print(f"Велике число: {big_number}")
print(f"Індекс у масиві: {index}")