$(function() { // quando o documento estiver pronto/carregado
    
    $.ajax({
        url: 'http://localhost:5000/listar_animais',
        method: 'GET',
        dataType: 'json', // os dados são recebidos no formato json
        success: listar, // chama a função listar para processar o resultado
        error: function() {
            alert("erro ao ler dados, verifique o backend");
        }
    });

    function listar (animais) {
        // percorrer a lista de pessoas retornadas; 
        for (var i in animais) { //i vale a posição no vetor
            lin = '<tr>' + // elabora linha com os dados da pessoa
            '<td>' + animais[i].id + '</td>' + 
            '<td>' + animais[i].nome + '</td>' + 
            '<td>' + animais[i].idade + '</td>' +
            '<td>' + animais[i].sexo + '</td>' + 
            '<td><a href=# id="excluir_' + animais[i].id + '" ' + 
              'class="excluir_animal"><img src="../img/lixeira.png" '+
              'alt="Excluir animal" title="Excluir animal" height="25"></a>' + 
            '</td>' + 
            '</tr>';
            // adiciona a linha no corpo da tabela
            $('#corpoTabelaAnimais').append(lin);
        }
    }
    });
