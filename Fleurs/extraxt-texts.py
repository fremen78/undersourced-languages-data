from datasets import load_dataset
from huggingface_hub import login
import os
from datasets import get_dataset_split_names

import pandas as pd

token = os.environ["HF_TOKEN"] # is a gated dataset ?

login(token)

def extract_dataset(lang, isplit):
    filename = "fleurs_" + lang + "_" + isplit + ".tsv"
    df = pd.read_csv(filename, sep="\t", engine="python", on_bad_lines="warn", header=None)
    df.to_csv("hf_fleurs-" + lang + "-dataset_" + isplit + ".csv")
    print(df.columns)
    df = df[[2]]
    df.columns = ['text']
    print(df.head())
    full_text = ""
    for it in df.iterrows():
        text_i = it[1]['text'] + "\n\n"
        full_text = full_text + text_i   
    with open("hf_fleurs-" + lang + "-dataset_" + isplit + "_text_only.txt", "w") as f:
        f.write(full_text)


for lang in ['wolof', 'pulaar']:
    for spt in ["train", "test", "dev"]:
        extract_dataset(lang, spt)
