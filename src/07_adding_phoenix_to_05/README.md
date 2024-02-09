# Description
Loads the orca-mini model and feeds it restuls of another model run. 
The model's task is to compare the set of answers to the control answers.

An llm observability tool, Phoenix is also intagrated in this project.
To see the Activity Dashboard, open http://localhost:6006 in your browser while the model is running.

## Details

- prompt_template.py - contains the prompt and the template, feel free to play around with these
- QA.py - utils for Question Answering, the chain and the retrieval function
- data_handling.py - utils for loading pfd and json data
- embedding.py - utils for fine tuning the model (process the pdf data)
- main.py - runs the model and all the utility code