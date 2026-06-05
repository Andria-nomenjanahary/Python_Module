#!/usr/bin/env python3


def secure_archive(
    file_path: str, action: str = "r", file_content: str = ""
) -> tuple[bool, str]:
    is_success = False
    content = ""
    try:
        with open(file_path, action) as file:
            if action == "r":
                is_success = True
                content = file.read()
            elif action == "w":
                is_success = True
                file.write(file_content)
                content = "Content successfully written to file"
    except FileNotFoundError as e:
        content = str(e)
    except PermissionError as e:
        content = str(e)

    return (is_success, content)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(f"{secure_archive("ancient_fragment.txt")}\n")
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(f"{secure_archive("/etc/master.passwd")}\n")
    print("Using 'secure_archive' to read from a regular file:")
    content = secure_archive("ex3/ancient_fragment.txt")
    print(f"{content}\n")
    actual_content = content[-1]
    print("Using 'secure_archive' to write previous content to a new file:")
    print(
        f"{secure_archive("ex3/ancient_fragment1.txt", "w", actual_content)}"
    )
