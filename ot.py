content = ""

for i in range(1, 9):
    if i == 3:
        for j in range(2):
            file = f"{i}.{j}.md"
            with open(f"md/{file}", "r") as f:
                content += f.read()
        continue
    file = f"{i}.md"
    if file.endswith(".md"):
        with open(f"md/{file}", "r") as f:
            content += f.read()

with open("readme.md", "w") as f:
    f.write(content)
