# Description
Loads the orca-mini and mistral models and asks questions from them based on the pdf they read.
The results are stored in 'output.json'

## Details

- data_handling.py - contains the data handler functions
- embedding - code related to the model embeddings
- prompt - contains the prompt and the template, feel free to play around with these
- QA - utils for Question Answering, the chain and the retrieval function
- main.py - runs the models and all the utility code, saves the output to a file 