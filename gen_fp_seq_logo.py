import openai
import requests
from Bio.Seq import Seq

def generate_fp_sequence(prompt:str):

    OPENAI_API_KEY = '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'  # Replace with your OpenAI key
    openai.api_key = OPENAI_API_KEY

    messages = [
        {"role": "system", "content": "For the following protein, create a .yml file containing a single protein per protein domain with the following format. - domain: type: name: pfam:"},
        {"role": "user", "content": prompt}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        max_tokens=512,
        temperature=0,
        messages=messages
    )

    pfam_values = []
    choices = response["choices"]
    for choice in choices:
        message = choice["message"]
        content = message["content"]
        yaml_data = content.split("\n")[3:]
        for line in yaml_data:
            if "pfam" in line:
                try:
                    pfam_value = line.split(": ")[1]
                    pfam_values.append(pfam_value)
                except IndexError:
                    print("Warning: Unexpected data format. Skipping.")
                    

    url = "https://www.ebi.ac.uk/interpro/api/entry/pfam/"

    # Create a set of unique pfam_values to prevent duplicate requests
    pfam_values = list(set(pfam_values))
    data_list = []
    sequences_list = []
    for pfam_value in pfam_values:
        response = requests.get(url + pfam_value + "?annotation=logo")
        if response.status_code == 200:
            sequence_response = response.json()
            data_list.append(sequence_response["probs_arr"])
        else:
            print(f"Warning: Failed to retrieve data for pfam_value {pfam_value}.")

    alphabets_list = []
    for data in data_list:
        last_strings = [lst[-1] for lst in data]
        alphabets_list.append(s.split(':')[0] for s in last_strings)

    protein_sequences = []
    for sequence_arr in alphabets_list:
        protein_sequences.append("".join(sequence_arr))

    fusion_prot = ""

    for protein_sequence in protein_sequences:
        fusion_prot+=protein_sequence + "GSGSGS"

    fusion_prot = fusion_prot[0:fusion_prot.rfind("GSGSGS")]

    if fusion_prot[0] != "M":
        fusion_prot = "M" + fusion_prot
    
    fusion_prot_seq = Seq(fusion_prot)
    return(fusion_prot_seq)

def run():
    prompt = input('Provide comma-seprated list of keywords\n')
    result = generate_fp_sequence(prompt)
    print(result)

run()