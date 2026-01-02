import yaml
import os

def contains_index(item):
    if isinstance(item, str):
        return os.path.basename(item) == "index.md"
    if isinstance(item, dict):
        for v in item.values():
            if contains_index(v):
                return True
    if isinstance(item, list):
        for i in item:
            if contains_index(i):
                return True
    return False

def sort_nav(x, is_root=True):
    if isinstance(x, list):
        r = [sort_nav(i, is_root=False) for i in x]
        if not is_root:
            # 仅对非根级别列表排序
            def key(i):
                if contains_index(i):
                    return ("", "")  # index.md 排前
                if isinstance(i, str):
                    return ("z", i.lower())
                if isinstance(i, dict):
                    k = list(i.keys())[0]
                    return ("z", str(k).lower())
                return ("z", str(i))
            r.sort(key=key)
        return r
    if isinstance(x, dict):
        return {k: sort_nav(v, is_root=False) for k, v in x.items()}
    return x

with open("mkdocs.yml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

data["nav"] = sort_nav(data["nav"], is_root=True)

with open("mkdocs.yml", "w", encoding="utf-8") as f:
    yaml.dump(data, f, allow_unicode=True, sort_keys=False)
