$(document).ready(function() {
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');


    $("#btn-add-player").on('click', function (){
        $("#players-list").append('<input type="text" class="form-control mb-3 player-name" placeholder="Name of the player" />')
    });

    $("#btn-register").on('click', function (){

        players_name =[]
        $(".player-name").each(function(){
            players_name.push($(this).val())
        });

        registration_data={
            "team_name":$("#team-name").val(),
            "manager_name":$("#manager-name").val(),
            "coach_name":$("#coach-name").val(),
            "players_name":players_name
        }

        var request = $.ajax({
            url: "",
            headers: {'X-CSRFToken': csrftoken},
            type: "POST",
            contentType: 'application/json',
            data : JSON.stringify({"data": registration_data})
        });
        request.done(function( response ) {
            alert("Your are successfully registered");
            location.reload();

        });

    });
});