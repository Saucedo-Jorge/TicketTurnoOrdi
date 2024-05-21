// src/controllers/municipioController.js
import { getAllMunicipios, addMunicipio } from "../models/municipioModel";

export const handleFormSubmit = async (request) => {
  if (request.method === "POST") {
    const formData = await request.formData();
    const idmuni = parseInt(formData.get("idmuni"), 10);
    const nombremuni = formData.get("nombremuni");
    if (!isNaN(idmuni) && typeof nombremuni === "string") {
      await addMunicipio(idmuni, nombremuni);
    }
  }
};

export const loadMunicipios = async () => {
  return await getAllMunicipios();
};
