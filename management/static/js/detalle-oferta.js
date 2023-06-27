const imagen_principal = document.getElementById('imagen-principal')
const imagenes_galeria = document.querySelectorAll('.imagen-galeria')

imagenes_galeria.forEach(imagen => {
    imagen.addEventListener('click', (e) => {
        imagenes_galeria.forEach(i => i.classList.remove('activo'))
        e.target.classList.add('activo')
        imagen_principal.src = e.target.src
    })
})