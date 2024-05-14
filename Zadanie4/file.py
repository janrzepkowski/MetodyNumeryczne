def read_file():
    data = []
    for _ in range(99):
        data.append([])

    with open("laguerre.txt", "r") as f:
        pattern = 'n = '
        for line in f:
            if line.strip():
                if pattern in line:
                    n = int(line.split('=')[1].strip())
                else:
                    parts = line.split()
                    if len(parts) >= 2:
                        x = float(parts[0])  # waga
                        y = float(parts[1])  # X
                        data[n - 2].append([x, y])
                    else:
                        print(line)
    return data
