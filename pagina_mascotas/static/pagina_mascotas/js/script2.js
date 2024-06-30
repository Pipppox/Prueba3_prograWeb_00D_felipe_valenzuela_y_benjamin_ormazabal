$(document).ready(function() {
    
    setTimeout(function() {
        let userConsent = confirm("¿Deseas recibir notificaciones?");
        if (userConsent) {
            alert("Has aceptado recibir notificaciones.");
            
        } else {
            alert("Has rechazado recibir notificaciones.");
            
        }
    }, 10000);  /**10 segundos a esperar para que aparezca la alerta*/
});
