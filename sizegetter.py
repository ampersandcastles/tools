import re
import sys

def calculate_total_size(filename, keyword):
    pattern = re.compile(rf'{re.escape(keyword)}.*?(\d+(?:\.\d+)?)\s(MiB|GiB)')
    total_size_mib = 0

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            match = pattern.search(line)
            if match:
                size, unit = match.groups()
                size = float(size)
                if unit == "GiB":
                    size *= 1024  # Convert GiB to MiB
                total_size_mib += size

    total_size_gib = total_size_mib / 1024
    return total_size_mib, total_size_gib

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <path to file> <keyword>")
        sys.exit(1)

    filename = sys.argv[1]
    keyword = sys.argv[2]
    total_size_mib, total_size_gib = calculate_total_size(filename, keyword)
    print(f"Total size of files containing '{keyword}': {total_size_gib:.2f} GiB ({total_size_mib:.0f} MiB)")
