def file_type_getter(file_extension_tuples):
    type_dict = {}
    for item in file_extension_tuples:
        for i in item:
            for tuple in i:
                doc_type = tuple[0]
                doc_extension = tuple[1]
                print(f"TYPE: {doc_type}, EXTENSION: {doc_extension}")
                type_dict[doc_type] = doc_extension

    print(type_dict)


def main():
    run_cases = [
        (
            [
                ("document", [".doc", ".docx"]), 
                ("image", [".jpg", ".png"])
            ],
        )
    ]

    file_type_getter(run_cases)


main()