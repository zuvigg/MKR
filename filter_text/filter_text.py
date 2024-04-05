def filter_text(input_file, output_file, keyword):
    input_path = "filter_text/" + input_file
    with open(input_path, 'r') as f:
        lines = f.readlines()

    filtered_lines = [line for line in lines if keyword in line]

    output_path = "filter_text/" + output_file

    with open(output_path, 'w') as f:
        f.writelines(filtered_lines)

if __name__ == "__main__":
    input_file = input("Enter the input file name: ")
    output_file = "filtered.txt"
    keyword = input("Enter the keyword to filter: ")
    filter_text(input_file, output_file, keyword)