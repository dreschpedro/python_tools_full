def read_file(file_path, delimiter=','):
    """Reads a file and returns a list of tuples (first_element, second_element, third_element)."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return [line.strip().split(delimiter, 2) for line in lines]

def write_file(file_path, data):
    """Writes the data to a file."""
    with open(file_path, 'w') as file:
        for item in data:
            file.write(','.join(item) + '\n')

def filter_products(choco_products, binary_products):
    """Filters choco products that do not appear in binary products."""
    binary_codes = {binary[1] for binary in binary_products}
    return [choco for choco in choco_products if choco[2] not in binary_codes]

# Read the files
binary_products = read_file('productos_binary.txt')
choco_products = read_file('productos_choco.txt')

# Filter the choco products
filtered_choco_products = filter_products(choco_products, binary_products)

# Write the results to a new file
write_file('filtered_productos_choco.txt', filtered_choco_products)
