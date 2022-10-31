
$(document).on('click', "#btnImprimir", function () {
    alert('aqui');
    $.post('produto_del.html', function (retorno) {
        $("#modalImprimir").modal({ backdrop: 'static' });
        $("#tela").html(retorno);
    });
});