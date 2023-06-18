import openai
import requests
import os
from Bio.Seq import Seq
from Bio import AlignIO
#from Bio.Alphabet import *

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
                    

    

    # Create a set of unique pfam_values to prevent duplicate requests
    pfam_values = list(set(pfam_values))
    #data_list = []
    #sequences_list = []
    
    #protein_sequences1 = []
    #protein_sequences2 = []
    protein_sequences_str = seq_seed_gen(pfam_values=pfam_values)
    #protein_sequences2 = seq_logo_gen(pfam_values=pfam_values)
    
    #print()

    fusion_prot = ""
    #protein_sequences = protein_sequences1
    protein_sequences = []
    
    for i in range(len(protein_sequences_str)):
        protein_sequences_str[i] = list(str(protein_sequences_str[i]))
        #protein_sequences2[i] = list(str(protein_sequences2[i]))

        #protein_sequences1_tmp = protein_sequences1
        for j in range(len(protein_sequences_str[i])):
            for element in protein_sequences_str[i]:
                if element == "-" or element == ".":
                    protein_sequences_str[i].remove(element)

        #protein_sequences1 = protein
        #if len(protein_sequences1[i]) != len(protein_sequences2[i]):
        #    print('Warning: sequence logo and seed length do not match')
        #    protein_sequences.append(Seq("".join(protein_sequences1[i])))
        #    continue

        protein_sequences.append(Seq("".join(protein_sequences_str[i])))

    #protein_sequences = 

    for protein_sequence in protein_sequences:
        fusion_prot+=protein_sequence + "GSGSGS"

    fusion_prot = fusion_prot[0:fusion_prot.rfind("GSGSGS")]

    if fusion_prot[0] != "M":
        fusion_prot = "M" + fusion_prot
    
    fusion_prot_seq = Seq(fusion_prot)
    return(fusion_prot_seq)

def seq_seed_gen(pfam_values: list):
    protein_sequences = []
    protein_seed_sequences = []
    url = "https://www.ebi.ac.uk/interpro/api/entry/pfam/"
    for pfam_value in pfam_values:
        response = requests.get(url + pfam_value + "?annotation=alignment:seed")
        if response.status_code == 200:
            with open('tmp.txt', 'w') as f:
                f.write(response.text)
            align = AlignIO.read('tmp.txt', "stockholm")
            os.remove('tmp.txt')
            for record in align:
                protein_seed_sequences.append(record.seq)
                #print(record.seq)
            #data_list.append(sequence_response["probs_arr"])
            #print(align)
            
            
            protein_sequence = rank_sequences_based_on_common(protein_seed_sequences)[0][1]
            protein_sequences.append(protein_sequence)
            protein_seed_sequences = []
        else:
            print(f"Warning: Failed to retrieve data for pfam_value {pfam_value}.")
    
    return protein_sequences

def seq_logo_gen(pfam_values: list):
    protein_sequences  = []
    url = "https://www.ebi.ac.uk/interpro/api/entry/pfam/"
    data_list = []
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
        protein_sequences.append(Seq("".join(sequence_arr)))
    
    return protein_sequences

def create_sequence_based_on_common(sequences):
    # Assumption! All sequences are the same length
    length = len(sequences[0])

    # Find the most common letter at each position
    # If there is a tie, choose the first one    
    consensus = ""
    for i in range(length):
        # Get the ith letter from each sequence
        letters = [seq[i] for seq in sequences]
        # Find the most common letter
        most_common = max(set(letters), key=letters.count)
        consensus += most_common

    return consensus

def rank_sequences_based_on_common(sequences):
    # Assumption! All sequences are the same length
    length = len(sequences[0])

    # Find the most common letter at each position
    # If there is a tie, choose the first one    
    consensus = ""
    for i in range(length):
        # Get the ith letter from each sequence
        letters = [seq[i] for seq in sequences]
        # Find the most common letter
        most_common = max(set(letters), key=letters.count)
        consensus += most_common

    # Rank the sequences based on how many letters they have in common with the consensus
    ranked_sequences = []
    for seq in sequences:
        score = 0
        for i in range(length):
            if seq[i] == consensus[i]:
                score += 1
        ranked_sequences.append((score, seq))

    # Sort the sequences by their score
    ranked_sequences.sort(reverse=True)

    return ranked_sequences


def run():
    prompt = input('Provide comma-seprated list of keywords\n')
    result = generate_fp_sequence(prompt)
    print(result)

run()