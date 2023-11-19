# ollama_langchain
Experimental code snippets - Ollama &amp; Langchain

Exploring llm training using local models

Each numbered folder in the src folder constains a standalone small experiment

## Requirements

- python 3
- you'll need an editor that can run Jupyter notebooks for example VSCode: https://code.visualstudio.com/

## Install

1. To create and run python virtual environment run these in the main project folder:

    python3 -m venv <your_env>
  
    source <your_env>/bin/activate

2. Install dependencies for project

    pip3 install -r requirements.txt

3. Install kernel for running the Jupyter notebook

    ipython kernel install --user --name=<your_env>

    (you'll most likely need to restart in order for this new kernel to be selectable in step 4)

4. Navigate to one of the named folders.
  Open the .ipynb file and select the kernel from the dropdown at the top of the notebook

5. Create data folder in main project folder and add the desired pdf file

6. Update the name of the pdf file in the Jupyter notebook. Look for this line or similar:
  
  docs = load_pdf_data(file_path=<your_file_name>)

## Run

You can interact with the models via the Jupyter notebooks in the numbered folders in src
Keep adding more cells for new questions

## Tear down

To shut down the virtual environment simply run deactivate in the project root
