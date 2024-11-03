from datasets import load_dataset
from huggingface_hub import login
import os

token = os.environ["HF_TOKEN"] # bloom-lm datste is a gated dataset

login(token)



# Specify the language code.
dataset = load_dataset("sil-ai/bloom-lm", 'snk')

# A data point consists of stories in the specified language code.
# To see a story:
print(dataset['train']['text'][0])

for k in dataset.keys():
    df = dataset[k].to_pandas()
    df.to_csv("hf_bloom-lm-snk-dataset_" + k + ".csv")
    print(df.columns)
    print(df.head())
    full_text = ""
    for it in df.iterrows():
        text_i = it[1]['title'] + "\n\n" + it[1]['text'] + "\n\n\n"
        full_text = full_text + text_i   
    with open("hf_bloom-lm-snk-dataset_" + k + "_text_only.txt", "w") as f:
        f.write(full_text)
