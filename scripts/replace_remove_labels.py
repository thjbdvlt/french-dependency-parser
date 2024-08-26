import conllu
import matcher

fp_lookup = "./lookup_labels.txt"
with open(fp_lookup, 'r') as f:
    lines = f.readlines()

lines = [i.strip() for i in lines]
lines = [i for i in lines if i != ""]

label_to_remove = set()
lookup = {}
for i in [i for i in lines if not i.startswith('#')]:
    if i.startswith('-'):
        label_to_remove.add(i[1:])
    elif i.count(' ') == 1:
        x, y = i.split(' ')
        lookup[x] = y
    else:
        raise ValueError("failed to parse lookup.txt:", i)


def low(s):
    return s["form"].lower()


for i in ("dev", "train", "test"):
    fp = f"{i}.conllu"

    with open(fp, "r") as f:
        file_content = f.read()

    sentences = conllu.parse(file_content)

    with open(fp, "w") as f:
        f.write("")

    with open(fp, "a") as f:
        for s in sentences:

            # remove unused attributes so i can see something
            for i in s:
                for a in (
                    "upos",
                    "xpos",
                    "feats",
                    "misc",
                    "deps",
                    "lemma",
                ):
                    i[a] = None

            # match the pattern 'du de le' and similar patterns
            for m in matcher.matchmany(
                s,
                [
                    [
                        lambda i: low(i) in "du",
                        lambda i: low(i) == "de",
                        lambda i: low(i) == "le",
                    ],
                    [
                        lambda i: low(i) == "au",
                        lambda i: low(i) == "à",
                        lambda i: low(i) == "le",
                    ],
                    [
                        lambda i: low(i) == "aux",
                        lambda i: low(i) == "à",
                        lambda i: low(i) == "les",
                    ],
                    [
                        lambda i: low(i) == "des",
                        lambda i: low(i) == "de",
                        lambda i: low(i) == "les",
                    ],
                ],
            ):
                m[2]["deprel"] = "case:det"
                m[2]["form"] = m[0]["form"]
                m[1]["form"] = None
                m[1]["deprel"] = None

            for i in s:
                dep = i['deprel']
                if dep in lookup:
                    i['deprel'] = lookup[dep]

            # some sentences contains labels that i do not want
            if not any(
                [
                    i["deprel"] and (i["deprel"] in label_to_remove)
                    for i in s
                ]
            ):
                f.write(s.serialize())
