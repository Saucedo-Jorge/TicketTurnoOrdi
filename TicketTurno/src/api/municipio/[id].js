// src/api/municipio/[id].js
import { fetchMunicipioById } from "../../controllers/municipioController.js";

export async function get({ params }) {
  const { id } = params;
  const municipio = await fetchMunicipioById(id);
  if (municipio) {
    return new Response(JSON.stringify(municipio), { status: 200 });
  } else {
    return new Response(JSON.stringify({ error: "Municipio no encontrado" }), { status: 404 });
  }
}
