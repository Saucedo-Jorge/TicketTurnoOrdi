// src/models/municipioModel.js
import { db, municipio } from "astro:db";

export const getAllMunicipios = async () => {
  return await db.select().from(municipio);
};

export const addMunicipio = async (id, nombre) => {
  return await db.insert(municipio).values({ id, nombre });
};
