import json
import os

# Lire le fichier JSONL avec spécification de l'encodage
with open('test8.jsonl', 'r', encoding='utf-8') as file:
    lines = file.readlines()

new_data = []

# Traiter chaque ligne du fichier JSONL
for line in lines:
    line_data = json.loads(line.strip())
    messages = line_data.get("messages", [])
    
    # Regrouper tous les messages en un seul dictionnaire "message"
    combined_messages = []
    for message in messages:
        combined_messages.extend(message["messages"])

    combined_message = {"messages": combined_messages}
    new_data.append(combined_message)

# Écrire le résultat dans un nouveau fichier JSONL avec spécification de l'encodage
with open('training.jsonl', 'w', encoding='utf-8') as new_file:
    for data in new_data:
        new_file.write(json.dumps(data, ensure_ascii=False)  + '\n')
