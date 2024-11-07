from datasets import load_dataset
from huggingface_hub import login
import os
from datasets import get_dataset_split_names

token = os.environ["HF_TOKEN"] # Is this dataset a gated dataset ?

login(token)

def download_dataset(lang, isplit):
    # Specify the language code.
    try:
        dataset = load_dataset("CohereForAI/aya_dataset", split=isplit)
    except Exception as e:
        print("LOAD_DATASET_ERROR", lang, " ERROR : ", str(e))
        print("FAILED_TO_LOAD_LANGUAGE", lang)
        return
    # A data point consists of stories in the specified language code.
    # To see a story:
    print("NON_FILTERED_DATA")
    print(dataset)
    print(dataset['inputs'][0])
    print(dataset['targets'][0])
    print(dataset['language_code'][0])
    filtered = dataset.filter(lambda example: (example['language_code']==lang))
    print("FILTERED_DATA")
    print(filtered)
    if(len(filtered['inputs']) == 0):
        return
    print(filtered['inputs'][0])
    print(filtered['targets'][0])
    
    df = filtered.to_pandas()
    df.to_csv("hf_aya_dataset-" + lang + "-dataset_" + isplit + ".csv")
    print(df.columns)
    print(df.head())
    full_text = ""
    for it in df.iterrows():
        entry = it[1]
        text_i = it[1]['inputs'] + "\n" # + it[1]['targets'] + "\n"
        full_text = full_text + text_i   
    with open("hf_aya_dataset-" + lang + "-dataset_" + isplit + "_text_only.txt", "w") as f:
        f.write(full_text)


for lang in ['wol']:
    for spt in ["train", "test"]:
        download_dataset(lang, spt)
