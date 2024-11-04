from datasets import load_dataset
from huggingface_hub import login
import os
from datasets import get_dataset_split_names

token = os.environ["HF_TOKEN"] # Is this dataset a gated dataset ?

login(token)


def download_dataset(lang, isplit):
    # Specify the language code.
    try:
        lang_pair = "eng_Latn-" + lang
        if(lang in ['bam_Latn']):
            lang_pair = lang + "-eng_Latn"            
        dataset = load_dataset("allenai/nllb", name=lang_pair, split=isplit)
    except Exception as e:
        print("LOAD_DATASET_ERROR", lang, " ERROR : ", str(e))
        print("FAILED_TO_LOAD_LANGUAGE", lang)
        return
    # A data point consists of stories in the specified language code.
    # To see a story:
    print(dataset['translation'][0][lang])
    
    df = dataset.to_pandas()
    df.to_csv("hf_nllb-" + lang + "-dataset_" + isplit + ".csv")
    print(df.columns)
    print(df.head())
    full_text = ""
    for it in df.iterrows():
        text_i = it[1]['translation'][lang] + "\n"
        full_text = full_text + text_i   
    with open("hf_nllb-" + lang + "-dataset_" + isplit + "_text_only.txt", "w") as f:
        f.write(full_text)


for lang in ['bam_Latn', 'tzm_Tfng', 'wol_Latn']:
    for spt in ["train", "test", "validation"]:
        download_dataset(lang, spt)
