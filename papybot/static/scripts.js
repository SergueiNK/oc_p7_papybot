
$(document).ready(function () {
    $('form').on('submit', function (event) {
        event.preventDefault();
        // + Effacer les datas précedentes à chaque nouvelle réquete
        // + Envoyer le message d'erreur si data non trouvé (requete échouée)
        $.ajax({
            data: {
                userText: $('#userText').val(),
            },
            type: 'GET',
            url: '/ajax',
            beforeSend: function () {
                $('#spinner').removeClass('visually-hidden');
            },
            complete: function() {
                $('#spinner').addClass('visually-hidden');
            }
        }).done(function (data) {
            constructMap(data[1]);
            $('#wiki_paragraph').append("<p>" + data[0] + "</p>");
        });
    });
});

function constructMap(cord) {
    console.log(cord);
    var map = L.map('map').setView([cord.lat, cord.lng], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    L.marker([cord.lat, cord.lng]).addTo(map)
        .bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
        .openPopup();


}

