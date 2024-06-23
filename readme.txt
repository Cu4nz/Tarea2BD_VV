# Instrucciones para ejecutar la API

1. Instala Bun siguiendo las instrucciones en https://bun.sh
2. Clona el repositorio del proyecto.
3. Navega a la carpeta de la API.
4. Ejecuta `bun install` para instalar las dependencias.
5. Configura las variables de entorno en el archivo `.env`.
6. Ejecuta `npx prisma migrate dev --name init` para aplicar las migraciones de la base de datos.
7. Inicia la API con `bun run start`.
8. La API estará disponible en http://localhost:3000
