def merge_stats(stats_list):
    merged_stats = {}
    for stats in stats_list:
        for key in stats:
            if key not in merged_stats:
                merged_stats[key] = stats[key]
            else:
                merged_stats[key] += stats[key]
    return merged_stats




def test_line(line):
    ok = False
    for e in line:
        if e != " " and e != "\t":
            ok = True
    return ok

# def process(l, e):
#     n = 0
#     for i in range(len(l)):
#         if e in l:
#             n=n+1
#     return n

from sys import argv

if False:
    # argv = ["C:\\Users\\Alexandru\\Desktop\\test.txt"]
    argv = ["C:\\Users\\Alexandru\\Desktop\\Python\\Python\\Lab 2\\main.py"]

if len(argv) < 2:
    print("usage: python3 main.py <FILES>")
    exit(1)

paths = []
for filename in argv[1:]:
    import os.path
    if not os.path.isfile(filename):
        raise FileNotFoundError("File " + filename + " does not exist")
    if filename not in paths:
        paths += [filename]

global_stats = {}
for path in paths:
    extension = "None"
    for i in range(len(path) - 1, -1, -1):
        if path[i] == ".":
            extension = path[i + 1 :]
            break
    extension = extension.upper()
    stats = {}
    with open(path) as f:
        for line in f:
            stats["lines"] = stats["lines"] + 1 if "lines" in stats else 1

            wc = 0
            for e in line:
                wc = wc + 1

            c = 0
            for i in range(len(line)):
                if i + 2 < len(line):
                    if line[i:i+3] == "foo":
                        c+=1

            if "foo" in stats:
                stats["foo"] += c
            else:
                stats["foo"] = c

            if not test_line(line):
                if "empty_lines" in stats:
                    stats["empty_lines"] += 1
                else:
                    stats["empty_lines"] = 1
    new_stats = stats
    old_stats = global_stats[extension] if extension in global_stats else {}
    global_stats[extension] = merge_stats([old_stats, new_stats])


for ext in global_stats:
    print("Extension "+ext)
    v = global_stats[ext]
    for key, value in v.items():
        print("  " + key + ":" + " " + str(value))
    print()
