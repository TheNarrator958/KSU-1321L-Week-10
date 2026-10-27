# Class : CSE 1321L
# Section : B09
# Term : Fall 2026
# Instructor : Jui Mhatre
# Name : Dominic Lyu
# Lab : Assignment 5C

def read_dimensions(name):
    rows = int(input("Enter rows for Matrix " + name + ": "))
    cols = int(input("Enter columns for Matrix " + name + ": "))
    return rows, cols

def read_matrix(name, rows, cols):
    line = input("Enter Matrix " + name + " values (comma-separated): ")
    values = line.split(",")

    matrix = []
    index = 0
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(int(values[index]))
            index += 1
        matrix.append(row)
    return matrix

def display_matrix(name, matrix):
    print("Matrix " + name + ":")
    for r in range(len(matrix)):
        line = ""
        for c in range(len(matrix[r])):
            if c > 0:
                line += " "
            line += str(matrix[r][c])
        print(line)

def multiply_matrices(a, b, rows_a, cols_a, cols_b):
    result = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += a[i][k] * b[k][j]
            row.append(total)
        result.append(row)
    return result

def main():
    rows_a, cols_a = read_dimensions("A")
    print()
    rows_b, cols_b = read_dimensions("B")
    print()

    # Validate before asking for any values
    if cols_a != rows_b:
        print("Matrix multiplication is not possible.")
        print("Number of columns in Matrix A must equal number of rows in Matrix B.")
        return

    a = read_matrix("A", rows_a, cols_a)
    print()
    b = read_matrix("B", rows_b, cols_b)
    print()

    display_matrix("A", a)
    print()
    display_matrix("B", b)
    print()

    result = multiply_matrices(a, b, rows_a, cols_a, cols_b)
    print("Resulting Matrix:")
    for r in range(len(result)):
        line = ""
        for c in range(len(result[r])):
            if c > 0:
                line += " "
            line += str(result[r][c])
        print(line)

main()