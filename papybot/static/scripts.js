
$(document).ready(function () {
    $('form').on('submit', function (event) {
        event.preventDefault();

        // Delete the existing data
        $('#wiki_paragraph').empty();
        $('#alert_error').empty();
        $('#here_address').empty();
        $('#papy_history').empty();

        // Delete the existing data if exist
        if ($('#map').children().length > 0) {
            $('#map').remove();
            $('#map-wrapper').append('<div id="map"></div>');
        }

        $.ajax({
            // ajax request get
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
             // Send the error message if data not find
             if (data[1] >= 201 && data[1] <= 599) {
                displayError();
                console.exception(jqXHR);
            } else {
                //Display the map
                $('#userText').val('');
                constructMap(data[1]);
                //Display the wiki paragraph and address
                $('#papy_history').append("<h5>" + "Haha laisses papou te raconter une petite histoire et te donner l'adresse: " + "</h5>");
                displayWiki(data[0]);
                displayHere(data[2])
            }

        }).fail(function (errorThrown) {
            //Display error if problem with user request data
            displayError();
        });
    });
});


function constructMap(cord) {
    // Construction map
    var map = L.map('map').setView([cord.lat, cord.lng], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    L.marker([cord.lat, cord.lng]).addTo(map)
        .bindPopup('Hohoho mon petit.<br> Voici le point sur la carte que tu cherches.')
        .openPopup();
}

function displayError(){
    // Dispaly error
    $('#alert_error').append(
        $('<div>').addClass('alert alert-danger d-flex align-items-center').attr('role', 'alert')
        .append(
            $('<p>').text("Clarifie ta demande mon petit")
            )
            )
}

function displayWiki(text){
    // Display wiki paragraph
    $('#wiki_paragraph').append(
        $('<div>').addClass('alert alert-primary d-flex align-items-center').attr('role', 'alert')
        .append(
            "<p>" + text + "</p>",
            )
            )
}

function displayHere(address){
    // Display Here address
    $('#here_address').append(
        $('<div>').addClass('alert alert-success d-flex align-items-center').attr('role', 'alert')
        .append(
            "<p>" + address + "</p>"
            )
            )
}
