from multiprocessing import Pool
import hashlib
from itertools import product #набор комбинаций для работы с данными, массивами
from string import ascii_lowercase #алфавит
import time


def checkPassword (password):
    hash_object = hashlib.sha256(password.encode('utf-8')) #функция sha256 из модуля hashlib хэширует
    hex_dig = hash_object.hexdigest() #перевод в шестнадцатеричное число
    return hex_dig
# print(hex_dig)


def thread_job(combinations):

    hashes = [
        '1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad',
        '3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b',
        '74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f'
    ]

    for cur in combinations:
        variant = ''.join(cur)
        hash_variant = checkPassword(variant)
        if hash_variant in hashes:
            print (variant, "- найденный код; hash =", hash_variant)
#break

def run_threads(process_count, combinations):
    chunksize = len(combinations) // process_count
    chunks = [combinations[i:i+chunksize] for i in range(0, len(combinations), chunksize)]
    t_start = time.perf_counter()
    with Pool(processes=process_count) as pool:
        results = pool.map(thread_job, chunks)
    t_finish = time.perf_counter()
    all_time = t_finish - t_start
    print("Время:", all_time)

print("generating")

chars = ascii_lowercase
all_combinations = list(product(chars, repeat=5))

print("generated")
# mode = int(input("Выберете режим однопоточности или многопоточности: "))
# process_count = int(input("Process count: "))
process_count = 5

run_threads(process_count, all_combinations)
print("finish")
