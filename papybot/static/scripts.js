
$(document).ready(function () {
    $('form').on('submit', function (event) {
        event.preventDefault();
        // Si map a du contenu,
        // Supprimer le contenu de la balise MAP.
        if ($('#map').children().length > 0) {
            $('#map').remove();
            $('#map-wrapper').append('<div id="map"></div>');
        }
            ($('#wiki_paragraph').children().length > 0) ;{
            $('#wiki_paragraph').remove();
            $('#wiki_paragraph-wrapper').append('<div id="wiki_paragraph"></div>');
        }

            ($('#alert_error').children().length > 0) ;{
            $('#alert_error').remove();
            $('#alert_error-wrapper').append('<div id="alert_error"></div>');

        }

            ($('#here_address').children().length > 0) ;{
            $('#here_address').remove();
            $('#here_address-wrapper').append('<div id="here_address"></div>');

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
                $('#wiki_paragraph').append("<p>" + "Laisses papi te raconter une petite histoire:", data[0] + "</p>");
                console.log(data[2]);
                $('#here_address').append("<p>" + "Haha papou a même une adresse pour toi:", data[2] + "</p>");
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
