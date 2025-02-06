//cadastro.js
var popup = document.getElementById("idpopup");
        var btn = document.getElementById("opencadastrar");
        var span = document.getElementsByClassName("fechar")[0];

        // Abrir popup
        btn.onclick = function() {
            popup.style.display = "block";
        }

        // Fechar popup no x 
        span.onclick = function() {
            popup.style.display = "none";
        }
