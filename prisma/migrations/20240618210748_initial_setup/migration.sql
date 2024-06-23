-- CreateTable
CREATE TABLE "Usuario" (
    "user_id" SERIAL NOT NULL,
    "dir_correo" TEXT NOT NULL,
    "nombre" TEXT NOT NULL,
    "descripcion" TEXT NOT NULL,
    "fecha_creacion" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "Usuario_pkey" PRIMARY KEY ("user_id")
);

-- CreateTable
CREATE TABLE "Correo" (
    "id_correo" SERIAL NOT NULL,
    "remitente_id" INTEGER NOT NULL,
    "destinatario_id" INTEGER NOT NULL,
    "asunto" TEXT NOT NULL,
    "cuerpo" TEXT NOT NULL,
    "fecha_envio" TIMESTAMP(3) NOT NULL,
    "leido" BOOLEAN NOT NULL,
    "es_favorito" BOOLEAN NOT NULL,

    CONSTRAINT "Correo_pkey" PRIMARY KEY ("id_correo")
);

-- CreateTable
CREATE TABLE "DireccionBloqueada" (
    "user_id" INTEGER NOT NULL,
    "direccion_bloqueada" TEXT NOT NULL,
    "fecha_bloqueo" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "DireccionBloqueada_pkey" PRIMARY KEY ("user_id","direccion_bloqueada")
);

-- CreateTable
CREATE TABLE "DireccionFavorita" (
    "user_id" INTEGER NOT NULL,
    "direccion_favorita" TEXT NOT NULL,
    "fecha_agregado" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "DireccionFavorita_pkey" PRIMARY KEY ("user_id","direccion_favorita")
);

-- AddForeignKey
ALTER TABLE "Correo" ADD CONSTRAINT "Correo_remitente_id_fkey" FOREIGN KEY ("remitente_id") REFERENCES "Usuario"("user_id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Correo" ADD CONSTRAINT "Correo_destinatario_id_fkey" FOREIGN KEY ("destinatario_id") REFERENCES "Usuario"("user_id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "DireccionBloqueada" ADD CONSTRAINT "DireccionBloqueada_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "Usuario"("user_id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "DireccionFavorita" ADD CONSTRAINT "DireccionFavorita_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "Usuario"("user_id") ON DELETE RESTRICT ON UPDATE CASCADE;
