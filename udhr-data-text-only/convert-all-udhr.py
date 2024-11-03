import requests
import xml.etree.ElementTree as ET

def convert_file(lang):
    print("PROCESSING_UDHR_LANGUAGE", lang)
    html = None
    url = "https://raw.githubusercontent.com/eric-muller/udhr/refs/heads/main/data/udhr/udhr_" + lang + ".xml"
    r = requests.get(url)
    # print len(r.content)
    xml = r.content
    tree = ET.fromstring(xml)
    notags = ET.tostring(tree, encoding='utf8', method='text')
    # print(notags.decode()[:100])
    with open("udhr_" + lang + ".txt", "w") as f:
        f.write(notags.decode())
    return xml

for lang in ["arb", "wol", "snk", "fuf", "zgh", "tzm", "bam"]:
    convert_file(lang)
