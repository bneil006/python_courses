def deduplicate(f_list, s_list, reversed):
    item_set = set(f_list + s_list)
    items_in_order = sorted(list(item_set))
    items_in_reverse = []
    if reversed == False:
        return items_in_order
    else:
        for n in range(len(items_in_order)-1, -1, -1):
            items_in_reverse.append(items_in_order[n])
        return items_in_reverse

def main():
    list_one = ["milk", "bread", "eggs", "cheese", "apples"]
    list_two = ["milk", "bananas", "bread", "oranges", "cheese"]

    print(deduplicate(list_one, list_two, False))
    

main()