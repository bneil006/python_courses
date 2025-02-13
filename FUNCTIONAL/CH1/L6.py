numbers = [30, 18, 14, 22]

def get_median_font_size(font_sizes):
    font_sizes = sorted(font_sizes)
    if len(font_sizes) == 0:
        return None
    if len(font_sizes) % 2 == 0:
        return font_sizes[int(len(font_sizes) / 2 - 1)]
    else:
        font_sizes = font_sizes[len(font_sizes)//2:]
        return font_sizes[0]
    

def main():
    print(get_median_font_size(numbers))

main()