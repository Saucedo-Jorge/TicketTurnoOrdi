 import { defineDb, defineTable, column } from 'astro:db';

const municipio = defineTable({
  columns: {
    id: column.number({ primaryKey: true, autoIncrement: true }),
    nombre: column.text(),
  },
});


const alumno = defineTable({
  columns: {
    curp: column.text({ primaryKey: true}),
    nombre: column.text(),
    apellidoP: column.text(),
    apellidoM: column.text(),
    nivelcursa: column.text(),
    idmunicipio: column.number({references:()=> municipio.columns.id},),
  },

});





const cita = defineTable({
  columns: {
    id: column.number({ primaryKey: true}),
    quienR: column.text(),
    telefono: column.text(),
    correo: column.text(),
    status: column.text(),
  }
});


const detalleCita = defineTable({
  columns:{
    idcita: column.number({references:()=> cita.columns.id}),
    curpa: column.text({references:()=> alumno.columns.curp}),
    numTurno: column.number(),
    asuntoTratar: column.text(),
  }
});

// https://astro.build/db/config
export default defineDb({
  tables: {
    municipio,
    alumno,
    cita,
    detalleCita,
  }
});
