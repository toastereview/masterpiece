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
def process(l):
    n = 0
    for i in range(len(l)):
        if l[i] == "f":
            if i+1 < len(l):
                if l[i+1] == 'o':
                    if i+2 < len(l):
                        if l[i+2] == 'o':
                            n+=1
    return n

def compute_stats(file_path):
    stats = {}
    with open(file_path) as f:
        for line in f:
            stats["lines"] = stats["lines"] + 1 if "lines" in stats else 1

            wc = 0
            for e in line:
                wc = wc + 1

            if "foo" in stats:
                stats["foo"] += process(line)
            else:
                stats["foo"] = process(line)
            try:
                if not test_line(line):
                    stats["empty_lines"] += 1
            except:
                if not test_line(line):
                    stats["empty_lines"] = 1
    return stats


from sys import argv

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
    new_stats = compute_stats(path)
    old_stats = global_stats[extension] if extension in global_stats else {}
    global_stats[extension] = merge_stats([old_stats, new_stats])


for ext in global_stats:
    print("Extension "+ext)
    v = global_stats[ext]
    for key, value in v.items():
        print("  " + key + ":" + " " + str(value))
    print()


if False:
    # stats = compute_stats("C:\\Users\\Alexandru\\Desktop\\test.txt")
    stats = compute_stats("C:\\Users\\Alexandru\\Desktop\\Python\\Python\\Lab 2\\main.py")
    print(stats)
