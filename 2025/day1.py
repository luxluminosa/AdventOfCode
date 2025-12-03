with open("day1.txt", "r") as data:
    print("opened day1.txt")
    with open("day1_data.h", "w") as data_cpp:
        print("opened day1_data.h")
        first = True
        for line in data:
            line.strip()
            if line != "":
                if line[0] == "R":
                    right = "true"
                elif line[0] == "L":
                    right = "false"
                else:
                    print("parsing error for:")
                    print(line)
                    continue
                if not first:
                    data_cpp.write(",\n")
                data_cpp.write(f"Rotation<{right},{line[1:-1]}>{{}}")
                first = False
            
