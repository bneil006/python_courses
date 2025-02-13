
def format_line(line):
    strip = line.strip()
    capital = strip.capitalize()
    replace = capital.replace('.', '')
    all_caps = replace.upper()
    formatted_line = f"{all_caps}..."
    return formatted_line
    
def main():
    test_line = "She's our friend and she's crazy!"
    print(format_line(test_line))

main()