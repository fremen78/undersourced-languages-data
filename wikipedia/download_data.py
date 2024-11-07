from datasets import load_dataset
from huggingface_hub import login
import os
from datasets import get_dataset_split_names

token = os.environ["HF_TOKEN"] # Is this dataset a gated dataset ?

login(token)

lang_names = {"wo" : "wol", "ff" : "fuf", "bm" : "bam"}

def download_dataset(lang, isplit):
    # Specify the language code.
    lang_name = lang_names.get(lang, lang)
    try:
        dataset = load_dataset("wikimedia/wikipedia", "20231101." + lang, split=isplit)
    except Exception as e:
        print("LOAD_DATASET_ERROR", lang, " ERROR : ", str(e))
        print("FAILED_TO_LOAD_LANGUAGE", lang)
        return
    # A data point consists of stories in the specified language code.
    # To see a story:
    print(dataset['title'][0])
    print(dataset['text'][0])
    
    df = dataset.to_pandas()
    df.to_csv("hf_wikipedia-" + lang_name + "-dataset_" + isplit + ".csv")
    print(df.columns)
    print(df.head())
    full_text = ""
    for it in df.iterrows():
        text_i = it[1]['title'] + "\n" + it[1]['text'] + "\n\n"
        full_text = full_text + text_i   
    with open("hf_wikipedia-" + lang_name + "-dataset_" + isplit + "_text_only.txt", "w") as f:
        f.write(full_text)


for lang in ['bm', 'ff', 'wo', 'zgh']:
    for spt in ["train"]:
        download_dataset(lang, spt)
