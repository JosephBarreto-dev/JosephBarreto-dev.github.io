//Se rehace el código para eliminar XSS y el .innerHTML maliciosos
function enviar() {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('msg').value;

    if (!name || !email || !message){
        alert("Complete todos los inputs oe");
        return;
    }
    alert("Gracias por llenar todo, serás hackeado")
    //He quitado el XSS porque genera un riesgo en la seguridad
    document.getElementById('msg').value = " ";
}
