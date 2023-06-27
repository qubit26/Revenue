// Referencias HTML
const cantKilosDisplay = document.getElementById('cantKilosDisplay')
const cantValorDisplay = document.getElementById('cantValorDisplay')
const cantidad = document.getElementById('cantidad')
const valor = document.getElementById('valor')

// Seteamos el valor de cantKilosDisplay
cantKilosDisplay.innerHTML = `${cantidad.value} Kg.`

// Seteamos el valor de cantValorDisplay
cantValorDisplay.innerHTML = `+${(valor.value > 1 ? valor.value : 0)} $`


// EVENTOS
// Evento para cambiar de forma dinámica la cantidad en Kilos
cantidad.addEventListener('change', (e) => {
    cantKilosDisplay.innerHTML = `${e.target.value} Kg.`
})

// Evento para cambiar de forma dinámica el valor
valor.addEventListener('input', (e) => {
    cantValorDisplay.innerHTML = `+${e.target.value} $`
})