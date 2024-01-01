<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Connexion</title>

  <link rel="stylesheet" href="/static/styles.css">
  <link rel="icon" type="image/png" href="/static/img/logo.png">
</head>
<body class="login">

<div class="logo-container">
    <img src="/static/img/logo.png" alt="Logo">
  </div>

<div class="container">

  <h2 class="login">Bon retour!</h2>
  <form id="loginForm" action="/connexion" method="post">
    <div class="form-group">
    {% if error %}
    <p style="color: red;">{{ error }}</p>
    {% endif %}
      <input type="text" id="username" name="username" placeholder="E-mail" required>
    </div>
    <div class="form-group">
      
      <input type="password" id="password" name="password" placeholder="mot de passe" required>
    </div>
    <div class="form-group">
      <input type="submit" value="Connexion">
      <p class="login">Vous n'avez pas de compte ?  <a href="/inscription">Inscrivez-vous ici.</a></p>
    </div>
  </form>
  <hr class="login">
  <div id="g_id_onload"
     data-client_id="190726678896-th1h58l6snfh1qvbll4phpntg8a080lf.apps.googleusercontent.com"
     data-context="signin"
     data-ux_mode="popup"
     data-login_uri="http://localhost:8000/connexion"
     data-auto_prompt="false">
</div>

<div class="g_id_signin"
     data-type="standard"
     data-shape="rectangular"
     data-theme="filled_black"
     data-text="signin_with"
     data-size="large"
     data-logo_alignment="left"
     data-width="300px">
</div>  
</div>


<script src="https://accounts.google.com/gsi/client" async></script>
</body>
</html>
