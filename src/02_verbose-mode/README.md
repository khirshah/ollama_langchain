# Description
Loads the orca-mini model and trains it on a pdf of your choice
You can then ask questions of the trained model and it will answer it based on the provided pdf
The response will contains details about what text part the models used to answer the question

## Details

- data_handling.py - contains the data handler functions
- embedding - code related to the model embeddings
- prompt - contains the prompt and the template, feel free to play around with these
- QA - utils for Question Answering, the chain and the retrieval function
- Main.ipynb is the interactive notebook where you can import the model, train it and ask questions. 
