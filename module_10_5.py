def read_info(filename):
    all_data = []
    with open(filename, 'r') as file:
        while True:
            line = file.readline().strip()
            if not line:
                break
            all_data.append(line)
    return all_data
from time import perf_counter

def main():
    filenames = [f'./file_{number}.txt' for number in range(1, 5)]

    # Линейная обработка
    start_linear = perf_counter()
    for filename in filenames:
        data = read_info(filename)
    end_linear = perf_counter()

    linear_time = end_linear - start_linear
    print(f'Линейное выполнение заняло: {linear_time:.6f} секунд')

if __name__ == "__main__":
    main()

from multiprocessing import Pool
from time import perf_counter

def main():
    filenames = [f'./file_{number}.txt' for number in range(1, 5)]  # Предположим, у нас файлы от file_1.txt до file_4.txt

    # Линейная обработка
    start_linear = perf_counter()
    for filename in filenames:
        data = read_info(filename)
    end_linear = perf_counter()

    linear_time = end_linear - start_linear
    print(f'Линейное выполнение заняло: {linear_time:.6f} секунд')

    # Многопроцессорная обработка
    start_multiproc = perf_counter()
    with Pool(processes=4) as pool:
        results = pool.map(read_info, filenames)
    end_multiproc = perf_counter()

    multiproc_time = end_multiproc - start_multiproc
    print(f'Многопроцессорное выполнение заняло: {multiproc_time:.6f} секунд')

if __name__ == "__main__":
    main()