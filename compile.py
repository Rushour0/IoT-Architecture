import os


def to_pdf(file_path: str, output_path: str = None):
    file_name = file_path.split("/")[-1].split(".")[0]
    os.system(f"mdpdf {file_path} -o {output_path}{file_name}.pdf")
    print(f"Compiled {file_name}.md to {file_name}.pdf")


def research_document():
    order = ['architecture.md', 'comparative-study.md', 'technical-stacks.md',
             'justification-zigbee-mqtt.md', 'communication-flow.md', 'functionalities.md']
    content = ""
    for file in order:

        if file.endswith(".md"):
            with open(f"components/md/{file}", "r") as f:
                content += f.read()

    with open("research-document.md", "w") as f:
        f.write(content)

    to_pdf("research-document.md")


def compile_all():
    for file in os.listdir("components/md"):
        if file.endswith(".md"):
            to_pdf(f"components/md/{file}", '/components/pdf/')

    print("All files compiled to pdf")


if __name__ == "__main__":
    compile_all()
    research_document()
