filesystem = [
    "file1.txt",
    [
        "folder1",
        "file2.txt",
        [
            "folder2",
            "file3.txt"
        ]
    ]
]

def print_filesystem(items):
    for item in items:
        if isinstance(item, list):
            print_filesystem(item)
        else:
            print(item)

print_filesystem(filesystem)