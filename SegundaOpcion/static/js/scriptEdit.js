let buscar = () => {
  let curp = getTextByID("CURP");
  let id = getTextByID("NumeroTurno");
  var data = {
    id: id,
    curp: curp
  };
  fetch("/getTramite", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
      },
    body: JSON.stringify(data)
  })
    .then((response) => response.json())
    .then((data) => {
      if (data["null"] === undefined) {
        let js_curp = document.getElementById("CURP");
        js_curp.readOnly = true;

        let js_nombre = document.getElementById("Nombre");
        js_nombre.value = data["nombre"];

        let js_paterno = document.getElementById("Paterno");
        js_paterno.value = data["paterno"];

        let js_materno = document.getElementById("Materno");
        js_materno.value = data["materno"];

        let js_telefono = document.getElementById("Telefono");
        js_telefono.value = data["telefono"];

        let js_celular = document.getElementById("Celular");
        js_celular.value = data["celular"];

        let js_correo = document.getElementById("Correo");
        js_correo.value = data["correo"];

        let js_municipio = document.getElementById("Municipio");
        js_municipio.value = data["municipioId"];
        for (var i = 0; i < js_municipio.options.length; i++) {
          if (js_municipio.options[i].value !== data["municipioId"]) {
            js_municipio.options[i].disabled = true;
          }
        }

        let js_municipioId = document.getElementById("MunicipioID");
        js_municipioId.value = data["municipioId"];

        let js_nivel = document.getElementById("Nivel");
        js_nivel.value = data["gradoId"];

        let js_nombreRealizador = document.getElementById("nombreRealizador");
        js_nombreRealizador.value = data["NombreRealizador"];

        let js_Asunto = document.getElementById("Asunto");
        js_Asunto.value = data["Asunto"];
      } else {
        let js_nombre = document.getElementById("Nombre");
        js_nombre.value = "";

        let js_paterno = document.getElementById("Paterno");
        js_paterno.value = "";

        let js_materno = document.getElementById("Materno");
        js_materno.value = "";

        let js_telefono = document.getElementById("Telefono");
        js_telefono.value = "";

        let js_celular = document.getElementById("Celular");
        js_celular.value = "";

        let js_correo = document.getElementById("Correo");
        js_correo.value = "";

        let js_municipio = document.getElementById("Municipio");
        js_municipio.value = "0";
        for (var i = 0; i < js_municipio.options.length; i++) {
          js_municipio.options[i].disabled = false;
        }

        let js_nivel = document.getElementById("Nivel");
        js_nivel.value = "0";
        mensaje(
          "error",
          "Turno no existente",
          "No se pudo encontrar el turno",
          null
        );
      }
    });
};