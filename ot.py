
with open("base.md", "r") as f:
    content = f.read()
    
    for i in range(1, 9):
        file = f"{i}.md"
        if file.endswith(".md"):
            with open(f"md/{file}", "r") as f:
                content += f.read()

    with open("readme.md", "w") as f:
        f.write(content)
