import yaml

def sort_nav(x):
    if isinstance(x, list):
        r = [sort_nav(i) for i in x]
        def key(i):
            if isinstance(i, str):
                return i
            if isinstance(i, dict):
                return str(list(i.keys())[0])
            return str(i)
        r.sort(key=key)
        return r
    if isinstance(x, dict):
        return {k: sort_nav(v) for k, v in x.items()}
    return x

with open("mkdocs.yml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

data["nav"] = sort_nav(data["nav"])

with open("mkdocs.yml", "w", encoding="utf-8") as f:
    yaml.dump(data, f, allow_unicode=True, sort_keys=False)
