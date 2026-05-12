import csv
import re
import os.path

def search_file(file_path, search_string):
    results = []
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, 1):
            if search_string in line:
                results.append((line_number, line.strip()))
    return results

def write_to_file(results, output_file, file_type):
    if file_type == 'csv':
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Line Number', 'Line Content'])
            writer.writerows(results)
    else:  # txt
        with open(output_file, 'w') as txtfile:
            for line_number, line_content in results:
                txtfile.write(f"Line {line_number}: {line_content}\n")

def main():
    # Ask for the input file
    input_file = input("Enter the path to the file you want to search: ")
    while not os.path.isfile(input_file):
        print("File not found. Please try again.")
        input_file = input("Enter the path to the file you want to search: ")

    # Ask for the search string
    search_string = input("Enter the string you want to search for: ")

    # Perform the search
    results = search_file(input_file, search_string)

    # Print the number of results
    print(f"Number of results found: {len(results)}")

    # Ask for output file type
    while True:
        file_type = input("Enter the output file type (csv/txt): ").lower()
        if file_type in ['csv', 'txt']:
            break
        print("Invalid file type. Please enter either 'csv' or 'txt'.")

    # Ask for output file name
    output_file = input(f"Enter the name for the output {file_type} file: ")
    if not output_file.endswith(f'.{file_type}'):
        output_file += f'.{file_type}'

    # Write results to the output file
    write_to_file(results, output_file, file_type)

    print(f"Results have been written to {output_file}")

if __name__ == "__main__":
    main()