
//Style and custom for JS 
//captur of event for JS
//gonna surch the formular on JS
//gonna surch the formular on JS
let form = document.querySelector("#user-text-form");

function postFormData (url, data){
    return fetch(url, {
        method: "POST",
        body: data
    })
    // Recevoir le texte côté js. Concepte promesse. Fct va renvoyer un objet ce qui nous permet de réagir en cas de succés ou de l'erreur. 
    // 1 Réagir en cas de succées
    // response => response.json() permet de transformer le texte en quelque chose qui rassemble à un objet js
    .then(response => response.json())
    // si il y a une erreur ça me permet de renvoyer l'erreur
    .catch(error => console.log(error)); 
}
//listen the event of submission
form.addEventListener("submit", function (event) {
    //eviter que le comportement par default soitmise en route et d'eviter d'envoyer les données du seveur vers l'exterieur
    event.preventDefault();

    // Envoyer le contenu du fomulaire au serveur
    postFormData("/ajax", new FormData(form))
    .then(response => {
        console.log(response);
    })
})
