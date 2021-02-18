with open ("imenik.csv", "r") as data_file:
    vsebina = data_file.read().splitlines()

    for row in vsebina:
        row_data = row.split(",")
        print(f"{row_data[0]} is {row_data[1]} years old and {row_data[2]}")