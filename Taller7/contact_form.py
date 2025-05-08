#Importamos los elementos necesarios
import os
from zipfile import ZipFile

#se definne la estructura base del proyecto
more_html = """<!DOCTYPE html>
<html>
<head>
    <title>Formulario de Contacto</title>
    <link rel="stylesheet" href="contact.css">
</head>
<body>
    <h2>Contáctanos</h2>
    <form id="contact-form" onsubmit="enviar(); return false;">
        <label for="name">Nombre</label>
        <input type="text" id="name"><br>

        <label for="email">Correo</label>
        <input type="text" id="email"><br>

        <label for="msg">Mensaje</label>
        <textarea id="msg"></textarea><br>

        <button type="submit">Enviar</button>
    </form>
    <script src="contact.js"></script>
</body>
</html>
"""

contact_css = """h2 {
    color: lime;
    background-color: black;
}
form {
    width: 150%;
    padding: 50px;
}
label, input, textarea {
    display: block;
    margin-bottom: 20px;
}
"""

contact_js = """function enviar() {
    let email = document.getElementById('email').value;
    alert("Gracias por contactarnos " + email);
    document.getElementById('msg').innerHTML = "<script>alert('XSS en mensaje')</script>";
}
"""

# Ruta donde se crean los archivos (.HTLM, .JS, .CSS)
project_path = r'D:\UCundinamarca\Semestre4\Taller7'

# Guardar nuevos archivos
with open(f"{project_path}/contact.html", "w") as f:
    f.write(more_html)

with open(f"{project_path}/contact.css", "w") as f:
    f.write(contact_css)

with open(f"{project_path}/contact.js", "w") as f:
    f.write(contact_js)

# Reempaquetar el proyecto en un nuevo archivo ZIP
extended_zip_path = os.path.join(project_path, "Proyecto_Web_Erroneo_Extendido.zip")
with ZipFile(extended_zip_path, 'w') as zipf:
    for root, _, files in os.walk(project_path):
        for file in files:
            file_path = os.path.join(root, file)
            zipf.write(file_path, arcname=os.path.relpath(file_path, project_path))

extended_zip_path