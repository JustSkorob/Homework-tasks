def count_lines_in_file(file_path):
    """Функция для подсчета количества строк в файле."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return sum(1 for _ in file)


def line_counter(output_file, *input_files):
    """Функция для объединения файлов по количеству строк."""
    files_with_line_counts = [(file, count_lines_in_file(file)) for file in input_files]
    sorted_files = sorted(files_with_line_counts, key=lambda x: x[1])

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for file, line_count in sorted_files:
            outfile.write(f'Файл: {file}\n')
            outfile.write(f'Количество строк: {line_count}\n\n')

            # Записываем содержимое файла
            with open(file, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                outfile.write('\n')


# Пример использования
incoming_files = ['1.txt', '2.txt', '3.txt']
result_file = 'Final_file.txt'

line_counter(result_file, *incoming_files)
