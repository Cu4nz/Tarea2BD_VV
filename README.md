# Tarea 2 de Bases de Datos

## Cliente

### Requisitos
- **Lenguaje**: Python
- **Dependencias**: `requests`

### Archivos
- `requirements.txt`: Contiene las dependencias del cliente.
- `README.txt`: Instrucciones detalladas para ejecutar el cliente.

### Instrucciones para ejecutar el cliente
1. Clonar el repositorio.
2. Navegar a la carpeta del cliente.
3. Instalar las dependencias con: `pip install -r requirements.txt`
4. Ejecutar el cliente con: `python cliente.py`

### Funcionalidad del cliente
- Realizar consultas HTTP a la API.
- Mostrar menú de opciones:
  1. Enviar un correo.
  2. Ver información de una dirección de correo electrónico.
  3. Ver correos marcados como favoritos.
  4. Marcar correo como favorito.
  5. Terminar ejecución del cliente.

## API

### Requisitos
- **Lenguaje**: JavaScript/TypeScript
- **Framework**: Elysia (sobre Bun)
- **Base de datos**: PostgreSQL
- **ORM**: PrismaJS

### Archivos
- `requirements.txt`: Contiene las dependencias de la API.
- `README.txt`: Instrucciones detalladas para ejecutar la API.

### Instrucciones para ejecutar la API
1. Clonar el repositorio.
2. Navegar a la carpeta de la API.
3. Instalar las dependencias con: `bun install`
4. Configurar la base de datos PostgreSQL.
5. Ejecutar las migraciones de Prisma con: `npx prisma migrate dev`
6. Iniciar la API con: `bun run start`

### Endpoints
1. **Registrar usuario**
   - **Ruta**: `/api/registrar`
   - **Método**: POST
   - **Formato del request**:
     ```json
     {
       "nombre": "Daniel",
       "correo": "daniel.duenas@usm.cl",
       "clave": "clavecita123",
       "descripcion": "Descripción del usuario"
     }
     ```
   - **Respuesta exitosa**:
     ```json
     {
       "estado": 200,
       "mensaje": "Usuario registrado correctamente"
     }
     ```

2. **Bloquear usuario**
   - **Ruta**: `/api/bloquear`
   - **Método**: POST
   - **Formato del request**:
     ```json
     {
       "correo": "daniel.duenas@usm.cl",
       "clave": "clavecita123",
       "correo_bloquear": "fernando.banz@sansano.usm.cl"
     }
     ```
   - **Respuesta exitosa**:
     ```json
     {
       "estado": 200,
       "mensaje": "Usuario bloqueado correctamente"
     }
     ```

3. **Obtener información pública de usuario**
   - **Ruta**: `/api/informacion/:correo`
   - **Método**: GET
   - **Respuesta exitosa**:
     ```json
     {
       "estado": 200,
       "nombre": "Daniel",
       "correo": "daniel.duenas@usm.cl",
       "descripcion": "Descripción del usuario"
     }
     ```

4. **Marcar correo como favorito**
   - **Ruta**: `/api/marcarcorreo`
   - **Método**: POST
   - **Formato del request**:
     ```json
     {
       "correo": "daniel.duenas@usm.cl",
       "clave": "clavecita123",
       "id_correo_favorito": 1
     }
     ```
   - **Respuesta exitosa**:
     ```json
     {
       "estado": 200,
       "mensaje": "Correo marcado como favorito correctamente"
     }
     ```

5. **Desmarcar correo como favorito**
   - **Ruta**: `/api/desmarcarcorreo`
   - **Método**: DELETE
   - **Formato del request**:
     ```json
     {
       "correo": "fernando.banz@sansano.usm.cl",
       "clave": "clavecita123",
       "id_correo_favorito": 1
     }
     ```
   - **Respuesta exitosa**:
     ```json
     {
       "estado": 200,
       "mensaje": "Correo desmarcado como favorito correctamente"
     }
     ```

### Procedimientos para inicializar la base de datos
1. Crear una nueva base de datos en PostgreSQL.
2. Configurar la conexión en el archivo `.env`.
3. Ejecutar las migraciones de Prisma: `npx prisma migrate dev`
4. Poblar la base de datos con datos iniciales si es necesario.

