import openai
OPENAI_API_KEY = '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'
openai.api_key = OPENAI_API_KEY
import json
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

#pfam_value1 = response["choices"][0]["message"]["content"].split("pfam: ")[1].split("\n")[0]
#print(pfam_value)


pfam_list = []

choices = response["choices"]
for choice in choices:
    message = choice["message"]
    content = message["content"]
    yaml_data = content.split("\n")[3:]  # Remove the first three lines ("protein: Ribosome", "domains:", and the empty line)
    for line in yaml_data:
        if "pfam" in line:
            pfam_value = line.split(": ")[1]
            pfam_list.append(pfam_value)
            
print(pfam_list)


# Define the API endpoint
url = "https://www.ebi.ac.uk/interpro/api/"

# Specify the endpoint and any required parameters
endpoint = "entry/pfam/"
entry_id = "?annotation=logo"

urlfinal = url + endpoint + pfam_value + entry_id

response = requests.get(urlfinal)

# Check the response status code
if response.status_code == 200:
    # Print the response content
    print(response.json())
else:
    print("Error: Failed to retrieve data from the API.")

print(url + endpoint + pfam_value + entry_id)
