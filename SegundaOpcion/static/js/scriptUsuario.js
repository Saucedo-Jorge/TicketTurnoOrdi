let curp = document.getElementById("CURP");
let municipio = document.getElementById("Municipio");
municipio.onchange = () => {
  let municipioId = document.getElementById("MunicipioID");
  municipioId.value = municipio.value;
};
curp.onchange = () => {
  let js_curp = getTextByID("CURP");
  fetch("get-alumno", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ curp: js_curp }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data["null"] === undefined) {
        let js_nombre = document.getElementById("Nombre");
        js_nombre.value = data["nombre"];
        js_nombre.readOnly = true;

        let js_paterno = document.getElementById("Paterno");
        js_paterno.value = data["paterno"];
        js_paterno.readOnly = true;

        let js_materno = document.getElementById("Materno");
        js_materno.value = data["materno"];
        js_materno.readOnly = true;

        let js_telefono = document.getElementById("Telefono");
        js_telefono.value = data["telefono"];
        js_telefono.readOnly = true;

        let js_celular = document.getElementById("Celular");
        js_celular.value = data["celular"];
        js_celular.readOnly = true;

        let js_correo = document.getElementById("Correo");
        js_correo.value = data["correo"];
        js_correo.readOnly = true;

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
      } else {
        let js_nombre = document.getElementById("Nombre");
        js_nombre.readOnly = false;
        js_nombre.value = "";

        let js_paterno = document.getElementById("Paterno");
        js_paterno.readOnly = false;
        js_paterno.value = "";

        let js_materno = document.getElementById("Materno");
        js_materno.readOnly = false;
        js_materno.value = "";

        let js_telefono = document.getElementById("Telefono");
        js_telefono.readOnly = false;
        js_telefono.value = "";

        let js_celular = document.getElementById("Celular");
        js_celular.readOnly = false;
        js_celular.value = "";

        let js_correo = document.getElementById("Correo");
        js_correo.readOnly = false;
        js_correo.value = "";

        let js_municipio = document.getElementById("Municipio");
        js_municipio.value = "0";
        for (var i = 0; i < js_municipio.options.length; i++) {
          js_municipio.options[i].disabled = false;
        }

        let js_nivel = document.getElementById("Nivel");
        js_nivel.value = "0";
      }
    })
    .catch((error) => {
      console.error(error);
    });
};