import { db, municipio } from "astro:db";

export async function getAllMunicipios() {
  return await db.select().from(municipio);
}

export async function getMunicipioById(id) {
  return await db.select().from(municipio).where("id", id).first();
}

export async function createMunicipio(id, nombre) {
  return await db.insert(municipio).values({ id, nombre });
}

export async function updateMunicipio(id, nombre) {
  return await db.update(municipio).set({ nombre }).where("id", id);
}

export async function deleteMunicipio(id) {
  return await db.delete(municipio).where("id", id);
}
