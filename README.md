# Berkeley AI Hackathon

## Elements of AI in Biotech

New plan is focused on synthesizing protein sequences based on user defined conditions using the GPT 4 language model.

Benefits:
- Fast, easy method to generate fusion proteins with several functions. Does not require extensive literature search.

Limitations:
- Fails to provide consistent and accurate protein sequences with highly specific parameters

List of domain parameters well understood by reccomendation model:
```
antibody, ribosome, cholesterol
```

List of domains not well understood by reccomendation model:
```
pH levels, water solubility, hydrophilicity 
```
```
cli.py:
```
This module is the entry point of the Command Line Interface (CLI) for the application. It prompts the user to input a comma-separated list of keywords, generates a protein sequence based on these keywords, and then saves the result as a FASTA file.


gen_fp_seq_seed.py:
This module is responsible for generating functional fusion proteins (FFPs) based on a given list of keywords.


ai_generate_sequence_list(prompt:str): Generates a list of protein sequences from a given prompt string using the OpenAI API. The function reads the API key from "openai-key.txt", sends a request to the OpenAI API, parses the response to retrieve PFAM values, and then uses these PFAM values to generate protein sequences.


fp_generate(protein_sequences_seq: list): Takes in a list of protein sequences and generates a fusion protein by concatenating the sequences, separated by "GSGSGS". The function also ensures the first character of the fusion protein is "M".


seq_seed_gen(pfam_values: list): Retrieves seed protein sequences from the InterPro API for each given PFAM value. This function also generates a protein sequence based on common sequences among the seed sequences.


seq_logo_gen(pfam_values: list): Retrieves logo sequences from the InterPro API for each given PFAM value and generates a protein sequence from these logos.


create_sequence_based_on_common(sequences): Creates a consensus sequence from the given list of sequences based on the most common character at each position.


rank_sequences_based_on_common(sequences): Ranks the sequences based on their similarity to a consensus sequence created from the given list of sequences.



```
gui.py:
```
This module provides a Graphical User Interface (GUI) for the application using the Tkinter library. Users can input a comma-separated list of keywords, and the application will generate a protein sequence based on these keywords and display it in the GUI. Users can also save the output to a file or fold the protein sequence by sending it to an external API.


class App(Frame): This class provides the structure for the GUI, including input fields, buttons, and output display. It also defines the behavior of the buttons, such as generating a protein sequence, saving the output to a file, and folding the protein.


run_gui(): This function initializes the GUI and starts the main event loop.


send_request_0(protein_sequence: str): This function sends a POST request to a specified API endpoint with the protein sequence as the request body.


send_request_1(protein_sequence: str): This function also sends a POST request to a different API endpoint with the protein sequence as the request body.
