import json, os

with open("print.json") as f:
    cfg = json.load(f)

out = []
for d in cfg["dirs"]:
    for name in sorted(os.listdir(d)):
        if name.endswith(".md"):
            title = os.path.splitext(name)[0]
            with open(os.path.join(d, name), encoding="utf8") as f:
                out.append(f"# {title}\n\n" + f.read().rstrip() + "\n\n---\n\n")

with open("README.md", "w", encoding="utf8") as f:
    f.write("".join(out))

# pandoc README.MD -o blog.pdf --pdf-engine=xelatex