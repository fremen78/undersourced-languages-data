from datasets import load_dataset
from huggingface_hub import login
import os
from datasets import get_dataset_split_names

import pandas as pd

import json

token = os.environ["HF_TOKEN"] # is a gated dataset ?

login(token)

def get_text(fname):
    print("READING", fname)
    full_text = ""
    with open(fname, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = json.loads(line)
            text_i = data['text']
            text_i = text_i . replace("\\n", "\n")
            full_text = full_text + text_i + "\n"
    return full_text

def extract_dataset(isplit):
    filename = "../madlad-400_hassaniya_" + isplit + "_text_only.txt"
    full_text = ""
    for n in range(10):
        input1 = isplit + "_docs_v2-0000" + str(n) + "-of-00010.jsonl"
        text1 = get_text(input1)
        full_text = full_text + text1 + "\n"
    with open(filename, "w") as f:
        f.write(full_text)


extract_dataset("clean")
extract_dataset("noisy")
