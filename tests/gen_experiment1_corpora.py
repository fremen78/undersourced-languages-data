import glob

def merge_files(lang, pattern):
    output = "experiment1/undersourced_language_experiment_corpus_" + lang + ".txt"
    with open(output, "a") as fout:
        for fname in glob.glob(pattern):
            with open(fname) as fin:
                text = fin.read()
                fout.write(text + "\n")


merge_files("wol", "../*/*wol*.txt")
merge_files("snk", "../*/*snk*.txt")
merge_files("zgh", "../*/*wol*.txt")
merge_files("zgh", "../*/*tzm*.txt")
merge_files("zgh", "../*/*kab*.txt")
merge_files("fuf", "../*/*fuf*.txt")
merge_files("fuf", "../*/*fuc*.txt")
merge_files("bam", "../*/*bam*.txt")
