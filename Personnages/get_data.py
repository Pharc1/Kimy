import re
import json

# Lire le fichier texte
with open('chat.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Pattern de recherche pour extraire les informations
pattern = r'\[(.*?)\]\s(.*?):\s(.*?)$'
conversations = []
conversation = []

# Parcourir les lignes du fichier texte
for line in lines:
    match = re.match(pattern, line)
    if match:
        timestamp, author, message = match.groups()
        if "audio omis" not in message and "image absente" not in message and "Vous avez supprimé ce message." not in message and "Ce message a été supprimé." not in message and "<Ce message a été modifié>" not in message:
            role = "user" if author.startswith("Pharci") else "assistant"
            content = message.strip()

            # Vérifier si le message précédent a le même rôle
            if conversation and conversation[-1]["role"] == role:
                # Fusionner les messages consécutifs du même utilisateur
                conversation[-1]["content"] += f"\n{content}"
            else:
                conversation.append({"role": role, "content": content})

            # Vérifier si la conversation a au moins 7 messages différents
            if len(set(msg["content"] for msg in conversation)) >= 7:
                conversations.append({"messages": conversation[:7]})
                conversation = []

# Si la dernière conversation n'a pas au moins 7 messages différents, l'ajouter quand même
if conversation and len(set(msg["content"] for msg in conversation)) >= 7 and len(conversation) >= 7:
    conversations.append({"messages": conversation[:7]})

# Écrire dans un fichier JSONL
with open('output.jsonl', 'w', encoding='utf-8') as jsonl_file:
    for conv in conversations:
        jsonl_file.write(json.dumps(conv, ensure_ascii=False) + '\n')
