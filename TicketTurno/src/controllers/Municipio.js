import {
    getAllMunicipios,
    getMunicipioById,
    createMunicipio,
    updateMunicipio,
    deleteMunicipio,
  } from "../models/municipioModel.js";
  
  export async function handleFormSubmission(request) {
    if (request.method === "POST") {
      const formData = await request.formData();
      const idmuni = parseInt(formData.get("idmuni"));
      const nombremuni = formData.get("nombremuni");
      const action = formData.get("action");
  
      if (action === "create" && !isNaN(idmuni) && typeof nombremuni === "string") {
        await createMunicipio(idmuni, nombremuni);
      } else if (action === "update" && !isNaN(idmuni) && typeof nombremuni === "string") {
        await updateMunicipio(idmuni, nombremuni);
      } else if (action === "delete" && !isNaN(idmuni)) {
        await deleteMunicipio(idmuni);
      }
    }
    return await getAllMunicipios();
  }
  
  export async function fetchMunicipioById(id) {
    return await getMunicipioById(id);
  }
  