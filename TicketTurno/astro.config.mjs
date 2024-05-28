import { defineConfig } from 'astro/config';
import auth from "auth-astro";
import vercel from "@astrojs/vercel/serverless";
import preact from "@astrojs/preact";
import tailwind from "@astrojs/tailwind";

import db from "@astrojs/db";

// https://astro.build/config
export default defineConfig({
  integrations: [auth(), preact(), tailwind(), db()],
  output: "server",
  adapter: vercel()
});