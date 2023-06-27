// Botón de responder
const btnResponder = document.querySelectorAll('.btnResponder')
const mensaje = document.getElementById('mensaje')

// Eventos para el botón de responder
btnResponder.forEach(btn => {
    btn.addEventListener('click', (e) => {
        mensaje.value = e.target.value
    })
});