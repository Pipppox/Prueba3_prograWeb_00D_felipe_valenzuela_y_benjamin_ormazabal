$(document).ready(function () {
    $("#contactForm").validate({
        rules: {
            nombre: {
                required: true,
                minlength: 4
            },
            email: {
                required: true,
                email: true
            },
            mensaje: {
                required: true,
                minlength: 10
            }
        },
        messages: {
            nombre: {
                required: "Por favor, ingresa tu nombre",
                minlength: "Tu nombre debe tener al menos 4 caracteres"
            },
            email: {
                required: "Por favor, ingresa tu correo electrónico",
                email: "Por favor, ingresa un correo electrónico válido"
            },
            mensaje: {
                required: "Por favor, ingresa un mensaje",
                minlength: "Tu mensaje debe tener al menos 10 caracteres"
            }
        },
        errorElement: 'div',
        errorClass: 'error',
        submitHandler: function (form) {
            alert('Formulario enviado con éxito');
            form.submit();
        }
    });
});

