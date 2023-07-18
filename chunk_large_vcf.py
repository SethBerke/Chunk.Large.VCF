import math

file_path = "./large.vcf"

def split_file(file_path):
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
        num_parts = math.ceil((total_lines - num_header_lines) / 30000)
        lines_per_part = math.ceil((total_lines - num_header_lines) / num_parts)

        for part in range(num_parts):
            start_index = num_header_lines + (part * lines_per_part)
            end_index = start_index + lines_per_part
            output_file = f"output_part_{part+1}.txt"

            with open(output_file, 'w') as output:
                output.writelines(header_lines)  # Write header lines
                output.writelines(lines[start_index:end_index])

            print(f"Part {part+1} written to {output_file} with {end_index - start_index} lines.")

        print("Total lines:", total_lines)

split_file(file_path)
