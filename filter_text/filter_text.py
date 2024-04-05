def filter_text(input_file, output_file, keyword):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    filtered_lines = [line for line in lines if keyword in line]

    with open(output_file, 'w') as f:
        f.writelines(filtered_lines)

if __name__ == "__main__":
    input_file = input("Enter the input file name: ")
    output_file = "filtered.txt"
    keyword = input("Enter the keyword to filter: ")
    filter_text(input_file, output_file, keyword)