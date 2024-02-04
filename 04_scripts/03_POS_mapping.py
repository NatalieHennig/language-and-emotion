import pandas as pd

df = pd.read_csv('/Users/nataliehennig/Documents/language-and-emotion/01_data/frequency_whole.csv', encoding="latin-1")

tag_mapping = {
    "PROPN": ["NP0", "NP0-NN1"],
    "NOUN": ["NN1", "NN2", "NN0", "NN1-NP0", "NN1-VVB", "NN1-VVG", "NN2-VVZ", "NN1-AJ0"],
    "VERB": ["VBB", "VBD", "VBG", "VBI", "VBN", "VBZ", "VDB", "VDD", "VDG", "VDI", "VDN", "VDZ", "VHB", "VHD", "VHG", "VHI", "VHN", "VHZ", "VVB", "VVD", "VVG", "VVI", "VVN", "VVZ", "VVB-NN1", "VVD-VVN", "VVD-AJ0", "VVG-AJ0", "VVG-NN1", "VVZ-NN2"],
    "AUX": ["VM0"],
    "ADJ": ["AJ0", "AJC", "AJS", "AJ0-NN1", "AJ0-VVG", "AJ0-VVN", "AJ0-VVD"],
    "ADV": ["AV0", "AVQ", "AV0-AJ0"],
    "PART": ["AVP", "XX0"],
    "PRON": ["AT0", "DPS", "DT0", "DTQ", "PNP", "PNI", "PNQ", "PNX"],
    "ADP": ["PRP", "PRF", "AVP", "PRP-AVP"],
    "CCONJ": ["CJC", "CJS", "CJT", "CJS-PRP", "PRP-CJS"],
    "NUM": ["CRD", "ORD", "CRD-PNI", "PNI-CRD"],
    "SCONJ": ["TO0"],
    "INTJ": ["ITJ"]
}

# reverse mapping
reverse_mapping = {value: key for key, values in tag_mapping.items() for value in values}

df['Tag'] = df['Tag'].replace(reverse_mapping)

df.to_csv('/Users/nataliehennig/Documents/language-and-emotion/05_output/mapped_pos_frequency.csv', index=False)


