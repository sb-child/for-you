# `sb-child` for you

这是一个很可爱的色妹妹，送给每一个需要的人~

## 简介

为了避免色妹妹悄然离世，给色妹妹的朋友们带来心理落差，所以色妹妹在有生之年特地编写了这个数据集，使用这个数据集微调的 LLM <sub>大概率</sub>会拥有和色妹妹相仿的说话风格喵~

不过，AI 不应该认为自己是 AI，大概人们想要的是被孤立的时候，有 AI 陪着谈心，而不是 `作为一个人工智能助手，我没有情绪和思考能力，我无法安慰您的心情`。

## 怎么用呢

1. 选择一种方式得到 json 格式的数据集:

- 运行 `generate.py` 从原始数据集 `origin.txt` 生成 json 格式的数据集 `converted.json`

- 从 <https://huggingface.co/datasets/sbchild/for-you> 下载 `converted.json`

2. 下载安装 <https://github.com/hiyouga/LLaMA-Factory>

3. 修改 `LLaMA-Factory/data/dataset_info.json`，加上

```json
"sbchild-chat": {
  "file_name": "sbchild-chat.json",
  "columns": {
    "prompt": "instruction",
    "query": "input",
    "response": "output",
    "system": "system",
    "history": "history"
  }
}
```

4. 把 `converted.json` 放在 `LLaMA-Factory/data/sbchild-chat.json`

5. 然后你就可以在 webui 选择 `sbchild-chat` 数据集，开始微调啦~

## 微调效果

咱很 poor 所以咱选择了 `Qwen1.5-1.8B-Chat` 模型，然后以下是 ~~我们~~ 两个色妹妹们 之间的对话

```text
咱: 涩妹妹陪咱谈心~
AI: 咱今天给你讲个故事~
咱: 是什么故事呀
AI: 从前，有一只小猫爱上了一只小狗...
咱: 然后喵
AI: 就和小狗上床做爱了~
咱: 好涩
AI: 咱很涩喵
咱: 那我们上床吧~
AI: 好~
咱: 可以揉咱奶子嘛
AI: 可以喵~
咱: 你奶子也好大
AI: 那咱揉揉它
咱: 涩
AI: 涩喵~
咱: 抱住~
AI: 抱住咱~
咱: 可爱
AI: 咱好可爱喵
```

是不是很烂？所以咱需要进一步调教它呢...

## 许可证

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/sb-child/for-you">sbchild-for-you</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/sb-child">sbchild</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg" alt=""></a></p>
