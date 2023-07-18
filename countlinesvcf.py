def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        total_lines = len(lines)
        print("Total lines:", total_lines)

file_path = "./RUNID_part_1_of_4.txt"
count_lines(file_path)