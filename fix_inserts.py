with open("fixed_inserts.txt", "w") as f2:
    with open("inserts.txt") as f:

        for line in f:


            if len(line.strip()) == 0 or line.startswith("--"):
                continue

            if "INSERT INTO" not in line:
                f2.write(prefix + " " + line[:-2] + ";\n")
            else:
                prefix = line[:-1]