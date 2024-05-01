import json

content = ""
dialog = ["", ""]
history = []
histories = []

r = []

with open("origin.txt", "r", encoding="utf-8") as f:
    for i in f.readlines():
        i = i.rstrip()
        if i.startswith("[-你-]:"):
            # AI 已经说完话了，所以在这里把 AI 的话放进 dialog
            dialog[1] = content
            # 然后存进 history
            if len(dialog[0]) > 0:
                history.append(dialog)
                dialog = ["", ""]
            # 是时候处理你说的话了
            i = i.removeprefix("[-你-]:")
            content = i
        elif i.startswith("[-AI-]:"):
            # 你已经说完话了，所以在这里把你的话放进 dialog
            dialog[0] = content
            # 是时候处理 AI 说的话了
            i = i.removeprefix("[-AI-]:")
            content = i
        elif i == "[-剧终-]":
            # 那这时候肯定是 AI 说完话了
            # 把 AI 的话放进 dialog
            dialog[1] = content
            # 然后存进 history
            if len(dialog[0]) > 0:
                history.append(dialog)
                dialog = ["", ""]
            # 放进 histories
            # print(history)
            histories.append(history)
            history = []
        elif i.startswith("[-注释-]:"):
            continue
        else:
            content = content + "\n" + i

for i in histories:
    s = {}
    if len(i) == 0:
        pass
    elif len(i) == 1:
        s["instruction"] = i[0][0]
        s["input"] = ""
        s["output"] = i[0][1]
        s["system"] = ""
        s["history"] = []
    else:
        s["instruction"] = i[len(i)-1][0]
        s["input"] = ""
        s["output"] = i[len(i)-1][1]
        s["system"] = ""
        s["history"] = []
        for j in range(len(i)-1):
            k = i[j]
            s["history"].append(k.copy())
    r.append(s)

with open("converted.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(r))
