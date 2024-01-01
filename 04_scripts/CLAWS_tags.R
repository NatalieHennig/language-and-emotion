#https://ucrel.lancs.ac.uk/bnc2/bnc2guide.htm#m2prep


map_to_tags_r <- function(word_class) {
  case_mapping <- list(
    "PROPN"  = c("NP0", "NP0-NN1"),
    "NOUN"   = c("NN1", "NN2", "NN0", "NN1-NP0", "NN1-VVB", "NN1-VVG", "NN2-VVZ"),
    "VERB"   = c("VBB", "VBD", "VBG", "VBI", "VBN", "VBZ", "VDB", "VDD", "VDG", "VDI", "VDN", "VDZ", "VHB", "VHD", "VHG", "VHI", "VHN", "VHZ", "VVB", "VVD", "VVG", "VVI", "VVN", "VVZ", "VVB-NN1", "VVD-VVN", "VVD-AJ0", "VVG-AJ0", "VVG-NN1", "VVZ-NN2"),
    "AUX"    = c("VM0"),
    "ADJ"    = c("AJ0", "AJC", "AJS", "AJ0-NN1", "AJ0-VVG", "AJ0-VVN"),
    "ADV"    = c("AV0", "AVQ", "AV0-AJ0"),
    "PART"   = c("AVP", "XX0"),
    "PRON"   = c("AT0", "DPS", "DT0", "DTQ", "PNP", "PNI", "PNQ", "PNX"),
    "ADP"    = c("PRP", "PRF", "AVP", "PRP-AVP"),
    "CCONJ"  = c("CJC", "CJS", "CJT", "CJS-PRP", "PRP-CJS"),
    "NUM"    = c("CRD", "ORD", "CRD-PNI", "PNI-CRD"),
    "SCONJ"  = c("TO0"),
    "INTJ"   = c("ITJ")
  )
  
  # Convert input to lowercase for case-insensitive comparison
  word_class_lower <- tolower(word_class)
  
  # Find matching tag or default to "X"
  matched_tag <- ifelse(
    any(sapply(case_mapping, function(tags) any(word_class_lower %in% tolower(tags)))),
    names(case_mapping)[sapply(case_mapping, function(tags) any(word_class_lower %in% tolower(tags)))],
    "X"
  )
  return(matched_tag)
}

process_frequency <- function(input_df, top_n = 25000) {
  input_df$mapped_pos <- sapply(input_df$Tag, map_to_tags_r)
  
  result_df <- input_df %>%
    select("Word", "Frequency", "mapped_pos") %>%
    slice_head(n = top_n) %>%
    group_by(Word, mapped_pos) %>%
    summarise(frequency = sum(Frequency))
  
  return(result_df)
}