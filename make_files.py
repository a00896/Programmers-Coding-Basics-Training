import os

folder_name = "programmers/coding_basics_training"


for i in range(2, 125):
    file_path = os.path.join(folder_name, f"{i}.py")
    with open(file_path, "w") as f:
        f.write(f"# {i}.py\n")

    