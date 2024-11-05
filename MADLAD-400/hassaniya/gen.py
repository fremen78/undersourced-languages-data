

link = "https://huggingface.co/datasets/allenai/MADLAD-400/resolve/main/data-v1p5/mey/clean_docs_v2-00000-of-00010.jsonl.gz"

for n in range(10):
	 l = link.replace("-00000-", "-0000" + str(n) + "-")
	 print("wget " + l)
	 print("wget " + l.replace("clean", "noisy"))
	 
