import math

file_path = "./large.vcf"
total_parts = 0
output_file_size = 30000

def split_file(file_path):
    global total_parts
    global output_file_size

    with open(file_path, 'r') as file:
        lines = list(file)
        total_lines = len(lines)
        
        header_lines = []
        for line in lines:
            if line.startswith('#'):
                header_lines.append(line)
            else:
                break
        
        num_header_lines = len(header_lines)
        lines_per_part = output_file_size
        
        if total_lines <= num_header_lines + lines_per_part:
            # If the total lines are smaller or equal to the chunk size
            total_parts = 1
            output_file = f"RUNID_part_1_of_{total_parts}.txt"

            with open(output_file, 'w') as output:
                output.writelines(lines)
            
            print(f"Part 1 written to {output_file} with {total_lines} lines.")
            print("Total lines:", total_lines)
            return

        total_parts = math.ceil((total_lines - num_header_lines) / lines_per_part)

        for part in range(total_parts):
            start_index = num_header_lines + (part * lines_per_part)
            end_index = start_index + lines_per_part
            output_file = f"RUNID_part_{part+1}_of_{total_parts}.txt"

            with open(output_file, 'w') as output:
                output.writelines(header_lines)  # Write header lines
                output.writelines(lines[start_index:end_index])

            print(f"Part {part+1} written to {output_file} with {end_index - start_index} lines.")

        print("Total lines:", total_lines)

split_file(file_path)
