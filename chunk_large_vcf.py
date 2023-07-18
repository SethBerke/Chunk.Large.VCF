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
        print("NUM HEADERLINES: ", num_header_lines)

        if total_lines <= num_header_lines + output_file_size:
            # If the total lines are smaller or equal to the output file size
            total_parts = 1
            lines_per_part = total_lines - num_header_lines
            output_file = f"RUNID_part_1_of_{total_parts}.txt"

            with open(output_file, 'w') as output:
                output.writelines(lines)
            
            print(f"Part 1 written to {output_file} with {total_lines} lines.")
            print("Total lines:", total_lines)
            return

        total_parts = math.ceil((total_lines - num_header_lines) / output_file_size)
        lines_per_part = (total_lines - num_header_lines) // total_parts
        remainder_lines = (total_lines - num_header_lines) % total_parts

        line_index = num_header_lines
        for part in range(total_parts):
            output_file = f"RUNID_part_{part+1}_of_{total_parts}.txt"
            lines_in_part = lines_per_part
            if part < remainder_lines:
                lines_in_part += 1
            end_index = line_index + lines_in_part

            with open(output_file, 'w') as output:
                output.writelines(header_lines)  # Write header lines
                output.writelines(lines[line_index:end_index])

            print(f"Part {part+1} written to {output_file} with {lines_in_part} lines.")
            line_index = end_index

        print("Total lines:", total_lines)

split_file(file_path)
