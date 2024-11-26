//...Datos
/*const expresiones = {
	nombre: /^[a-zA-ZÀ-ÿ\s]{1,50}$/, // Letras y espacios, pueden llevar acentos.
    apellido: /^[a-zA-ZÀ-ÿ\s]{1,50}$/, // Letras y espacios, pueden llevar acentos.
	correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	telefono: /^\d{8,8}$/ // 8 numeros.
} 

function formulario(){
    var nombreFormulario,apellidoFormulario,correoFormulario,telefonoFormulario;

    nombreFormulario = document.getElementById("Nombre").value;
    apellidoFormulario = document.getElementById("Apellido").value;
    correoFormulario = document.getElementById("Email").value;
    telefonoFormulario = document.getElementById("Telefono").value;

    if(expresiones.nombre.test(nombreFormulario)){
        if(expresiones.apellido.test(apellidoFormulario)){
            if(expresiones.correo.test(correoFormulario)){
                if(expresiones.telefono.test(telefonoFormulario)){
                    window.location="Carrito.html";
                }else{
                    alert("¡Numero Invalido, ingresar solo 8 digitos!");
                }
            }else{
                alert("¡Correo Invalido, ingresar un valor como el siguiente'ejemplo@ejemplo.cl' !");
            }
        }else{
            alert("¡Apellido Invalido, ingresar solo Letras!");
        }
    }else{
        alert("¡Nombre Invalido, ingresar solo Letras!");
    }
}*/

/*var btnEnviar = document.getElementById("btnEnviar")

btnEnviar.addEventListener("click", function() {
    
    //traer los datos del formulario
    let nombre = document.getElementById("nombre").value
    let apellido = document.getElementById("apellido").value
    let email  = document.getElementById("email").value
    let telefono = document.getElementById("telefono").value

    
    
    console.log(nombre)
    console.log(apellido)
    console.log(email)
    console.log(telefono)
})*/

/*Carrito*/

//const producto = document.querySelector('.producto');
//const titulo = document.querySelector('.titulo');
//const imgDef = document.querySelector('.imgDef');

/*try {
    fetch("./api.json")
    .then(respuesta => {
        return respuesta.json()
    })
    .then(datos => {
        var contador = 0;
        var titulo,imgDef;
        while (datos.length > contador){

            titulo = datos[contador].title;
            imgDef = datos[contador].image;

            //titulo.innerHTML = titulo;
            //imgDef.src = imgDef;

            console.log(datos[contador].title);
            console.log(datos[contador].image);
            contador++;
        }
    })
} catch (error) {
    console.log(e);
}*/

/*Reseta*/

