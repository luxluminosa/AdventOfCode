compiler_is_broken = False

if not compiler_is_broken:
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
                
else:
    with open("day1.txt", "r") as data:
        dial = 50
        count = 0
        count_d2 = 0
        for line in data:
            line = line.strip()
            if line != "":
                previous_dial = dial
                if line[0] == "R":
                    dial += int(line[1:])
                    if previous_dial < 0 and dial >= 0:
                        count_d2 += 1
                elif line[0] == "L":
                    dial -= int(line[1:])
                    if previous_dial > 0 and dial <= 0:
                        count_d2 += 1
                else:
                    print("Error reading line:")
                    print(line)
                if dial % 100 == 0:
                    count += 1
                while dial <= -100:
                    count_d2 += 1
                    dial += 100
                while dial >= 100:
                    count_d2 += 1
                    dial -= 100
        print(count, count_d2)