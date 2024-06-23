import { Elysia } from 'elysia';
import { PrismaClient } from '@prisma/client';

const app = new Elysia();
const prisma = new PrismaClient();


// Endpoint para registrar un usuario
app.post('/api/registrar', async (req, res) => {
    const { nombre, correo, clave, descripcion } = req.body;
    try {
        // Crear un nuevo usuario en la base de datos
        const usuario = await prisma.usuario.create({
            data: {
                nombre: nombre,
                dir_correo: correo,
                descripcion: descripcion,
                clave: clave,            //
                fecha_creacion: new Date(), // Establecer la fecha de creación
            },
        });
        // Respuesta exitosa
        res.json({ estado: 200, mensaje: 'Usuario registrado correctamente', usuario });
    } catch (error) {
        // Manejo de errores
        res.json({ estado: 400, mensaje: 'Error al registrar usuario', error: error.message });
    }
});


// Endpoint para bloquear un usuario
app.post('/api/bloquear', async (req, res) => {
    const { correo, clave, correo_bloquear } = req.body;
    try {
        // Buscar usuario por correo
        const usuario = await prisma.usuario.findUnique({
            where: { dir_correo: correo }
        });
        if (usuario) {
            // Crear entrada de dirección bloqueada
            const bloqueado = await prisma.direccionBloqueada.create({
                data: {
                    direccion_bloqueada: correo_bloquear,
                    fecha_bloqueo: new Date(), // Establecer fecha de bloqueo
                    user_id: usuario.user_id, // Conectar usando el ID del usuario
                },
            });
            // Respuesta exitosa
            res.json({ estado: 200, mensaje: 'Usuario bloqueado correctamente', bloqueado });
        } else {
            // Usuario no encontrado
            res.json({ estado: 404, mensaje: 'Usuario no encontrado' });
        }
    } catch (error) {
        // Manejo de errores
        res.json({ estado: 400, mensaje: 'Error al bloquear usuario', error: error.message });
    }
});



// Endpoint para obtener información de un usuario
app.get('/api/informacion/:correo', async (req, res) => {
    const { correo } = req.params;
    try {
        // Buscar usuario por correo
        const usuario = await prisma.usuario.findUnique({
            where: { dir_correo: correo },
        });
        if (usuario) {
            // Respuesta con información del usuario
            res.json({ estado: 200, nombre: usuario.nombre, correo: usuario.dir_correo, descripcion: usuario.descripcion });
        } else {
            // Usuario no encontrado
            res.json({ estado: 404, mensaje: 'Usuario no encontrado' });
        }
    } catch (error) {
        // Manejo de errores
        res.json({ estado: 400, mensaje: 'Error al obtener información del usuario', error: error.message });
    }
});


// Endpoint para marcar un correo como favorito
app.post('/api/marcarcorreo', async (req, res) => {
    const { correo, clave, id_correo_favorito } = req.body;
    try {
        // Buscar usuario por correo
        const usuario = await prisma.usuario.findUnique({
            where: { dir_correo: correo }
        });
        if (usuario) {
            // Verificar que el correo pertenece al usuario
            const correo = await prisma.correo.findUnique({
                where: { id_correo: id_correo_favorito }
            });
            if (correo && correo.destinatario_id === usuario.user_id) {
                // Actualizar el estado de favorito del correo
                const correoFavorito = await prisma.correo.update({
                    where: { id_correo: id_correo_favorito },
                    data: {
                        es_favorito: true,
                    },
                });
                // Respuesta exitosa
                res.json({ estado: 200, mensaje: 'Correo marcado como favorito', correoFavorito });
            } else {
                res.json({ estado: 404, mensaje: 'Correo no encontrado o no pertenece al usuario' });
            }
        } else {
            // Usuario no encontrado
            res.json({ estado: 404, mensaje: 'Usuario no encontrado' });
        }
    } catch (error) {
        // Manejo de errores
        res.json({ estado: 400, mensaje: 'Error al marcar correo como favorito', error: error.message });
    }
});
  

// Endpoint para desmarcar un correo como favorito
app.delete('/api/desmarcarcorreo', async (req, res) => {
    const { correo, clave, id_correo_favorito } = req.body;
    try {
        // Buscar usuario por correo
        const usuario = await prisma.usuario.findUnique({
            where: { dir_correo: correo }
        });
        if (usuario) {
            // Verificar que el correo pertenece al usuario
            const correo = await prisma.correo.findUnique({
                where: { id_correo: id_correo_favorito }
            });
            if(correo && correo.destinatario_id === usuario.user_id){
                //Actualizar el estado del correo a no favorito
                await prisma.correo.update({
                    where: {id_correo: id_correo_favorito },
                    data: {
                        es_favorito: false,
                    },
                });
                //Respuesta exitosa
                res.json({ estado: 200, mensaje: 'Correo desmarcado como favorito'});
            } else{
                res.json({ estado : 404, mensaje: ' Correo no encontrado o no pertenece al usuario'});
            }
    } else{
        //usuario no encontrado
        res.json({ estado: 404, mensaje: 'Correo no encontrado'});
    }
} catch (error) {
    // Manejo de errores
    res.json({ estado: 400, mensaje: 'Error al desmarcar correo como favorito', error: error.message });
}

});



// Endpoint para iniciar sesión
app.post('/api/login', async (req, res) => {
    const { correo, clave } = req.body;
    try {
        // Buscar usuario por correo
        const usuario = await prisma.usuario.findUnique({
            where: { dir_correo: correo }
        });
        if (usuario) {
            // Verificar que la clave coincide
            if (usuario.clave === clave) {
                res.json({ estado: 200, mensaje: 'Inicio de sesión exitoso', usuario });
            } else {
                res.json({ estado: 400, mensaje: 'Contraseña incorrecta' });
            }
        } else {
            res.json({ estado: 404, mensaje: 'Usuario no encontrado. Por favor, regístrese.' });
        }
    } catch (error) {
        // Manejo de errores
        res.json({ estado: 400, mensaje: 'Error al iniciar sesión', error: error.message });
    }
});




// Crear servidor HTTP y pasar el manejador de Elysia
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Servidor Elysia iniciado en http://localhost:${PORT}`);
});