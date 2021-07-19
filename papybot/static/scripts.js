
$(document).ready(function () {
    $('form').on('submit', function (event) {
        event.preventDefault();

        $('#wiki_paragraph').empty();
        $('#alert_error').empty();
        $('#here_address').empty();
        $('#papy_history').empty();

        // Si map a du contenu,
        // Supprimer le contenu de la balise MAP.
        if ($('#map').children().length > 0) {
            $('#map').remove();
            $('#map-wrapper').append('<div id="map"></div>');
        }

        // + Effacer les datas précedentes à chaque nouvelle réquete
        $.ajax({

            data: {
                userText: $('#userText').val(),
            },
            type: 'GET',
            url: '/ajax',
            beforeSend: function () {
                $('#spinner').removeClass('visually-hidden');
            },
            complete: function () {
                $('#spinner').addClass('visually-hidden');
            }

        }).done(function (data, textStatus, jqXHR) {
             // + Envoyer le message d'erreur si data non trouvé (requete échouée)
             if (data[1] >= 201 && data[1] <= 599) {
                displayError();
                console.exception(jqXHR);
            } else {
                $('#userText').val('');
                constructMap(data[1]);
                $('#papy_history').append("<h5>" + "Haha laisses papou te raconter une petite histoire et te donner l'adresse: " + "</h5>");
                displayWiki(data[0]);
                displayHere(data[2])
            }

        }).fail(function (jqXHR, textStatus, errorThrown) {
            console.log(jqXHR);
            console.exception(errorThrown);
            displayError();
        });
    });
});


function constructMap(cord) {
    var map = L.map('map').setView([cord.lat, cord.lng], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    L.marker([cord.lat, cord.lng]).addTo(map)
        .bindPopup('Hohoho mon petit.<br> Voici le point sur la carte que tu cherches.')
        .openPopup();


}

function displayError(){
    $('#alert_error').append(
        $('<div>').addClass('alert alert-danger d-flex align-items-center').attr('role', 'alert')
        .append(
            $('<p>').text("Clarifie ta demande mon petit")
            )
            )

}

function displayWiki(text){
    $('#wiki_paragraph').append(
        $('<div>').addClass('alert alert-primary d-flex align-items-center').attr('role', 'alert')
        .append(
            "<p>" + text + "</p>",
            )
            )

}

function displayHere(address){
    $('#here_address').append(
        $('<div>').addClass('alert alert-success d-flex align-items-center').attr('role', 'alert')
        .append(
            "<p>" + address + "</p>"
            )
            )

}
