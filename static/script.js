//------------------------------------------------INDEX-------------------------------------------------
/*
window.onload = function() {
  // Affiche une boîte de dialogue demandant le prénom de la personne
  const prenom = prompt("Entrez votre prénom:");

  // Vérifie si l'utilisateur a saisi un prénom et affiche un message correspondant
  if (prenom != null && prenom.trim() !== "") {
    const dataToSend = { sender: prenom, message: `Hi my name is ${prenom}` };
    const url = '/data';

    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(dataToSend),
    })
      .then(response => response.json())
      .then(responseData => {
        ajouterMessage('Kimy', responseData.response, 'bot-message');
        const imageData = { sender: 'Pharci', message: responseData.response };
        const imgUrl = '/views/data_img';
        fetch(imgUrl, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(imageData),
        })
          .then(imageResponse => imageResponse.json())
          .then(imageData => {
            document.body.style.backgroundImage = `url(${imageData.response})`;
          })
          .catch(error => {
            console.error('Erreur lors de la récupération de l\'image :', error);
            // Gérer les erreurs ici
          });
      })
      .catch(error => {
        console.error('Erreur lors de la récupération de la réponse :', error);
        // Gérer les erreurs ici
      });

  } else {
    alert("Vous n'avez pas saisi de prénom. Merci de recharger la page et d'entrer votre prénom.");
  }
};
*/

function ajouterMessage(nom, message, classe) {
    const chatBox = document.getElementById('chatBox');
    const newMessage = document.createElement('div');
    newMessage.classList.add('message', classe);
  
    const messageContent = document.createElement('div');
    messageContent.classList.add('message-content');
  
    const senderName = document.createElement('span');
    senderName.classList.add('sender-name');
    senderName.textContent = nom + ': ';
  
    const messageText = document.createElement('span');
    messageText.classList.add('message-text');
    messageText.textContent = message;
  
    messageContent.appendChild(senderName);
    messageContent.appendChild(messageText);
    newMessage.appendChild(messageContent);
  
    chatBox.appendChild(newMessage);
  
    // Scroll vers le dernier message ajouté
    chatBox.scrollTop = chatBox.scrollHeight;
  }
  
  
  
  
  
  
  
  function envoyerMessage() {
    // Start the typewriting animation when a message is sent
    var chatBox = document.querySelector('.chat-box');
    var typingIndicator = document.createElement('div');
    typingIndicator.className = 'typewriting';
    typingIndicator.innerHTML = '<div class="typewriting-dot"></div>'.repeat(3);
    chatBox.appendChild(typingIndicator);
  
    // Rest of your existing 'envoyerMessage' function ...
  
    const inputField = document.querySelector('.input-field');
    const messageContent = inputField.value.trim();
  
    if (messageContent !== '') {
      ajouterMessage('You', messageContent, 'user-message');
      inputField.value = ''; // Efface le champ de saisie après l'envoi
  
      // Envoi de données JSON à votre serveur Flask
      const dataToSend = { sender: 'Pharci', message: messageContent };
      const url = '/data';
  
      fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(dataToSend),
      })
        .then(response => response.json())
        
  .then(responseData => {
          // Remove the typewriting animation once the message response is received
          if (typingIndicator.parentNode === chatBox) {
            chatBox.removeChild(typingIndicator);
          }
          ajouterMessage('Mia', responseData.response, 'bot-message');
          const imageData = { sender: 'Pharci', message: responseData.response };
          const imgUrl = '/views/data_img';
          fetch(imgUrl, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(imageData),
          })
            .then(imageResponse => imageResponse.json())
            .then(imageData => {
              document.body.style.backgroundImage = `url(${imageData.response})`;
            })
            .catch(error => {
              console.error('Erreur lors de la récupération de l\'image :', error);
              // Gérer les erreurs ici
            });
        })
        .catch(error => {
          console.error('Erreur lors de la récupération de la réponse :', error);
          // Gérer les erreurs ici
        });
    }
  }
  
  const inputField = document.querySelector('.input-field');
  inputField.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
      event.preventDefault();
      envoyerMessage();
    }
  });
  
  const sendButton = document.querySelector('.send-button');
  sendButton.addEventListener('click', () => {
    envoyerMessage();
  });
  
  
  document.addEventListener('DOMContentLoaded', function() {
  
    const chatBox = document.querySelector('.chat-box');
    const typingIndicator = document.createElement('div');
    typingIndicator.className = 'typewriting';
    typingIndicator.innerHTML = '<div class="typewriting-dot"></div>'.repeat(3);
    chatBox.appendChild(typingIndicator);
  
    // Simule une attente de 2 secondes (2000 millisecondes) avant d'afficher le message par défaut
    setTimeout(function() {
      ajouterMessage('Mia', "OMG salut!! ça fait des heures je m'ennuie, il m'ai arrivé un truc de fou aujourd'hui, tu vas pas en croire tes oreilles !!", 'bot-message');
      chatBox.removeChild(typingIndicator); // Supprime l'animation une fois le message affiché
    }, 2000); // Modifier le délai d'attente si nécessaire
  });
  
//------------------------------------------------LOGIN-------------------------------------------------
