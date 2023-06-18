import openai
import requests

OPENAI_API_KEY = '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'  # Replace with your OpenAI key
openai.api_key = OPENAI_API_KEY

messages = [
    {"role": "system", "content": "produce a .yml file containing protein domains for the following protein with the following format:- domain: type: name: pfam:"},
    {"role": "user", "content": "Ribosome"}
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
    print(alphabets_list)

protein_sequences = []
for sequence_arr in alphabets_list:
    protein_sequences.append("".join(sequence_arr))

print(protein_sequences)