var curpPattern = /^[A-Za-z]{4}\d{6}[HMhm][A-Za-z]{5}[A-Za-z\d]\d$/;
var telefonoPattern = /^\d{10}$/;
var correoPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

let validation = () => {
  let js_Realizador = getTextByID("nombreRealizador");
  let js_Curp = getTextByID("CURP");
  let js_Nombre = getTextByID("Nombre");
  let js_Paterno = getTextByID("Paterno");
  let js_Materno = getTextByID("Materno");
  let js_Telefono = getTextByID("Telefono");
  let js_Celular = getTextByID("Celular");
  let js_Correo = getTextByID("Correo");
  let js_Nivel = getTextByID("Nivel");
  let js_Municipio = getTextByID("Municipio");
  let js_Asunto = getTextByID("Asunto");

  if (js_Realizador.length == 0) {
    mensaje(
      "error",
      "ERROR",
      "Indique el nombre de quien realiza el ticket",
      null
    );
    return false;
  } else if (!curpPattern.test(js_Curp)) {
    if (js_Curp.length == 0) {
      mensaje("error", "ERROR", "Indique la curp del alumno", null);
    } else {
      mensaje("error", "ERROR", "La curp no es valida", null);
    }
    return false;
  } else if (js_Nombre.length == 0) {
    mensaje("error", "ERROR", "Indique el nombre del alumno", null);
    return false;
  } else if (js_Paterno.length == 0) {
    mensaje("error", "ERROR", "Indique el apellido paterno del alumno", null);
    return false;
  } else if (js_Materno.length == 0) {
    mensaje("error", "ERROR", "Indique el apellido materno del alumno", null);
    return false;
  } else if (!telefonoPattern.test(js_Telefono)) {
    if (js_Telefono.length == 0) {
      mensaje("error", "ERROR", "Indique un número de telefono", null);
    } else {
      mensaje("error", "ERROR", "El número de telefono no es valido", null);
    }
    return false;
  } else if (!telefonoPattern.test(js_Celular)) {
    if (js_Telefono.length == 0) {
      mensaje("error", "ERROR", "Indique un número de celular", null);
    } else {
      mensaje("error", "ERROR", "El número de celular no es valido", null);
    }
    return false;
  } else if (!correoPattern.test(js_Correo)) {
    if (js_Correo.length == 0) {
      mensaje("error", "ERROR", "Indique un correo", null);
    } else {
      mensaje("error", "ERROR", "El correo no es valido", null);
    }
    return false;
  } else if (js_Nivel == "0") {
    mensaje(
      "error",
      "ERROR",
      "Indique el nivel en el que desea o ya está cursando el alumno",
      null
    );
    return false;
  } else if (js_Municipio == "0") {
    mensaje("error", "ERROR", "Indique el municipio del alumno", null);
    return false;
  } else if (js_Asunto == "0") {
    mensaje("error", "ERROR", "Indique el asunto de este ticket", null);
    return false;
  } else {
    return true;
  }
};

let getTextByID = (ID) => {
  return document.getElementById(ID).value.trim();
};

let mensaje = (tipo, titulo, mensaje, link) => {
  Swal.fire({
    type: tipo,
    title: titulo,
    text: mensaje,
    footer: link,
  });
};