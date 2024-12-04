import random
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def create_file(filename):
    with open(filename, 'w') as f:
        for _ in range(100):
            numbers = ' '.join(str(random.randint(0, 100)) for _ in range(20))
            f.write(numbers + '\n')

def process_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    processed_lines = []
    for line in lines:
        numbers = list(map(int, line.split()))
        filtered_numbers = list(filter(lambda x: x > 40, numbers))
        processed_lines.append(filtered_numbers)
    return processed_lines

def write_to_file(filename, data):
    with open(filename, 'w') as f:
        for numbers in data:
            f.write(' '.join(map(str, numbers)) + '\n')

def read_file_as_generator(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()

@measure_time
def main():
    filename = 'random_numbers.txt'

    create_file(filename)

    processed_data = process_file(filename)

    write_to_file(filename, processed_data)

    for line in read_file_as_generator(filename):
        print(line)

if __name__ == "__main__":
    main()

