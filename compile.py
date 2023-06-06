import os


def to_pdf(file_path: str, out_file_name: str = None, output_path: str = None):
    if output_path is None:
        output_path = "components/pdfs/"
    
    file_name = file_path.split("/")[-1].split(".")[0]
    
    if out_file_name is None:
        out_file_name = file_name

    os.system(f"mdpdf {file_path} -o {output_path}{out_file_name}.pdf")
    print(f"Compiled {file_name}.md to {out_file_name}.pdf")


def research_document():
    order = ['architecture.md', 'comparative-study.md', 'technical-stacks.md',
             'justification-zigbee-mqtt.md', 'communication-flow.md', 'functionalities.md']

    content = ""

    with open("base.md", "r") as f:
        content = f.read()

    for file in order:

        if file.endswith(".md"):
            with open(f"components/md/{file}", "r") as f:
                content += f.read()

    with open("readme.md", "w") as f:
        f.write(content)

    to_pdf("readme.md","research-document")



def compile_all():
    for file in os.listdir("components/md"):
        if file.endswith(".md"):
            to_pdf(f"components/md/{file}", '/components/pdf/')

    print("All files compiled to pdf")


if __name__ == "__main__":
    compile_all()
    research_document()
