import conllu
import matcher


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
                m[2]["deprel"] = f"{m[1]['deprel']}:{m[2]['deprel']}"
                m[2]["form"] = m[0]["form"] 
                m[1]["form"] = None
                m[1]["deprel"] = None
            f.write(s.serialize())
