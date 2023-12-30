import jsonlines

def regrouper_conversations(chemin_fichier_entree, chemin_fichier_sortie, nb_messages_par_conversation):
    conversations = []
    with jsonlines.open(chemin_fichier_entree) as reader:
        conversation = {"messages": []}
        for ligne in reader:
            if len(conversation["messages"]) < nb_messages_par_conversation:
                conversation["messages"].append(ligne)
            else:
                conversations.append(conversation)
                conversation = {"messages": [ligne]}

        # Ajouter la dernière conversation si elle est incomplète
        if conversation["messages"]:
            conversations.append(conversation)

    # Écrire les conversations regroupées dans un nouveau fichier JSONL
    with jsonlines.open(chemin_fichier_sortie, mode='w') as writer:
        for conversation in conversations:
            writer.write(conversation)

# Utilisation : spécifiez le chemin du fichier d'entrée, le chemin du fichier de sortie et le nombre de messages par conversation
chemin_fichier_entree = 'test5.jsonl'
chemin_fichier_sortie = 'test8.jsonl'
nb_messages_par_conversation = 2  # ou 7, selon votre choix

regrouper_conversations(chemin_fichier_entree, chemin_fichier_sortie, nb_messages_par_conversation)
