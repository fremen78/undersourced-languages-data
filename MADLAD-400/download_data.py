from datasets import load_dataset
from huggingface_hub import login
import os
from datasets import get_dataset_split_names

token = os.environ["HF_TOKEN"] # Is this dataset a gated dataset ?

login(token)

lang_names = {"wo" : "wol", "mey" : "mey", "ber" : "zgh", "bm" : "bam"}

def download_dataset(lang, isplit):
    # Specify the language code.
    lang_name = lang_names[lang]
    try:
        dataset = load_dataset("allenai/madlad-400", name=lang, split=isplit)
    except Exception as e:
        print("LOAD_DATASET_ERROR", lang, " ERROR : ", str(e))
        print("FAILED_TO_LOAD_LANGUAGE", lang)
        return
    # A data point consists of stories in the specified language code.
    # To see a story:
    print(dataset['text'][0])
    
    df = dataset.to_pandas()
    df.to_csv("hf_madlad-400-" + lang_name + "-dataset_" + isplit + ".csv")
    print(df.columns)
    print(df.head())
    full_text = ""
    for it in df.iterrows():
        text_i = it[1]['text'].replace("\\n", "\n") + "\n"
        full_text = full_text + text_i   
    with open("hf_madlad-400-" + lang_name + "-dataset_" + isplit + "_text_only.txt", "w") as f:
        f.write(full_text)


for lang in ['bm', 'mey', 'wo', 'ber']:
    for spt in ["clean", "noisy"]:
        download_dataset(lang, spt)
