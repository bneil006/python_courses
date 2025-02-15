def file_type_getter(file_extension_tuples, file):
    type_dict = {}
    for item in file_extension_tuples:
        for i in item:
            for tuple in i:
                doc_type = tuple[0]
                doc_extension = tuple[1]
                for each in doc_extension:
                    type_dict[each] = doc_type

    if file in type_dict:
        return type_dict[file]
    else:
        raise Exception("Unknown file type")

def main():
    file = ".jpg"
    run_cases = [
        (
            [
                ("document", [".doc", ".docx"]), 
                ("image", [".jpg", ".png"])
            ],
        )
    ]
    print(file_type_getter(run_cases, file))


main()