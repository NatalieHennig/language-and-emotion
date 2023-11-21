

add_anew_score <- function(text_name) {
  # Get the data frame
  text_in <- get(text_name)
  
  # Add the ANEW column
  text_in$ANEW <- text_in$token |> textstat_valence(dictionary = data_dictionary_ANEW["pleasure"])
  text_in <- unpack(text_in, cols = c(ANEW)) 
  text_in <- subset(select(text_in, -c(doc_id)))
  
  # Update the original data frame
  assign(text_name, text_in, envir = .GlobalEnv)
}

