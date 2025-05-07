function enviar() {
    let email = document.getElementById('email').value;
    alert("Gracias por contactarnos " + email);
    document.getElementById('msg').innerHTML = "<script>alert('XSS en mensaje')</script>";
}
