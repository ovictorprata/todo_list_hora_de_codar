$(document).ready(function() {

    var deleteBtn = $('.delete-btn'); //é assim que o Jquery acessa o template
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');

    $(deleteBtn).on('click', function(e) { //quando for clicado, será ativado

        e.preventDefault();

        var deleteLink = $(this).attr('href'); //pega o botão que o usuário cliclou
        var result = confirm('Tem certeza que deseja deletar essa tarefa?');

        if(result) {
            window.location.href = deleteLink;
        }

    });

    // Ao clicar na lupa ativa o submit form
    $(searchBtn).on('click', function() {
        searchForm.submit();
    });
});