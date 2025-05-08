#Importamos los elementos necesarios
import os
from zipfile import ZipFile

#se definne la estructura base del proyecto
more_html = """<!DOCTYPE html>
<html>
<head>
    <title>Contacto</title>
    <link rel="stylesheet" href="contact.css">
</head>
<body>
    <section class="main_cont">
        <h1>Contactanos</h1>
        <section class="form_cont">
            <form id="contact-form" onsubmit="enviar(); return false;">
                <label for="name">Nombre</label>
                <input type="text" id="name"><br>
        
                <label for="email">Correo</label>
                <input type="email" id="email"><br>
        
                <label for="msg">Mensaje</label>
                <textarea id="msg"></textarea><br>
                
                <div class="btn_cont">
                    <button type="submit">Enviar</button>
                </div>
            </form>
        </section>
    </section>   
    <script src="contact.js"></script>
</body>
</html>
"""

contact_css = """*{
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    font-size: 16px;
}
body {
    background-image: url('https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNjUyOXwwfDF8c2VhcmNofDJ8fGdyYXkgbGFuZHNjYXBlfGVufDB8fHx8MTY5MjQ3NTYyMQ&ixlib=rb-1.2.1&q=80&w=1080');
    background-size: cover;
}
h1{
    font-size: 25px;
}
.main_cont {
    text-align: center;
    margin: 100px;
}
.form_cont {
    text-align: left;
    border-radius: 25px;
    background-color: rgb(200, 142, 255);
    width: 30%;
    padding: 50px;
    margin: auto;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    padding: 2rem;
    color: white;
}
.btn_cont {
    text-align: center;
}
form button {
    width: 100%;
    background-color: rgb(0, 0, 0);
    color: white;
    margin: auto;
    padding: 10px 20px;
    border: none;
    border-radius: 100px;
    cursor: pointer;
}
form button:hover {
    background-color: rgb(71, 71, 71);
    transition: all 0.4s;
}
label, input, textarea {
    display: block;
    width: 100%;
    margin-bottom: 20px;
    color: rgb(0, 0, 0);
    font-weight: bold;
    box-sizing: border-box;
}
textarea{
    height: 40px;
    resize: none;
}
input, textarea {
    background: none;
    padding: 10px;
    border: none;
    border-bottom: 1px solid rgba(255, 255, 255, 0.3);
    transition: all 0.3s ease-in-out;
}
input:focus, textarea:focus {
    box-shadow: 0 0 0 0 rgba(0, 0, 0, 0.5) inset;
    border-bottom: 1px solid rgba(255, 255, 255);
    outline: none;
}
"""

contact_js = """//Se rehace el código para eliminar XSS y el .innerHTML maliciosos
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
}

"""

# Ruta donde se crean los archivos (.HTLM, .JS, .CSS)
project_path = r'D:\UCundinamarca\Semestre4\Taller7'

# Guardar nuevos archivos
with open(f"{project_path}/index.html", "w") as f:
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