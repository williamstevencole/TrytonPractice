# Tryton en Docker

Este repositorio proporciona configuración para desplegar Tryton 7.6 y PostgreSQL usando Docker Compose en macOS (ARM64) y Linux (AMD64).

## Requisitos

- Docker (20.10+) y Docker Compose (v2+) instalados.

## Estructura de archivos

- `Dockerfile`: define la imagen de Tryton con módulos adicionales.
- `docker-compose.yml`: define servicios `db` y `trytond`.
- `trytond.conf`: configuración del servidor Tryton.
- `README.md`: guía de uso (este archivo).

## 1. Dockerfile

```dockerfile
FROM --platform=linux/amd64 tryton/tryton:7.6

# Cambiar a root para instalar módulos
USER root

RUN pip install --break-system-packages \
    trytond_sale trytond_stock \
    trytond_account trytond_account_invoice \
    trytond_account_invoice_stock trytond_company \
    trytond_country trytond_currency trytond_party \
    trytond_product

# Volver a usuario 'tryton'
USER tryton
```

## 2. trytond.conf

```ini
[database]
uri = postgresql://tryton:tryton@db:5432/tryton

[web]
listen = 0.0.0.0:8000
```

Guarda este archivo en la raíz del proyecto.

## 3. docker-compose.yml

```yaml
services:
  db:
    image: postgres:14
    environment:
      POSTGRES_USER: tryton
      POSTGRES_PASSWORD: tryton
      POSTGRES_DB: tryton
    volumes:
      - tryton-db-data:/var/lib/postgresql/data

  trytond:
    build:
      context: .
      # Forzar plataforma amd64 en macOS ARM
      dockerfile: Dockerfile
      platform: linux/amd64
    depends_on:
      - db
    environment:
      TRYTOND_DATABASE_URI: postgresql://tryton:tryton@db:5432/tryton
    volumes:
      - ./trytond.conf:/etc/tryton/trytond.conf:ro
    ports:
      - "8000:8000"
    platform: linux/amd64

volumes:
  tryton-db-data:
```

> **Nota**: omite la clave `version:` para evitar advertencias de obsolescencia.

## 4. Uso

1. **Clona el repositorio** y entra en él:

   ```bash
   git clone git@github.com:williamstevencole/TrytonPractice.git Tryton
   cd Tryton
   ```

2. **Levanta los servicios**:

   ```bash
   docker compose up -d --build
   ```

3. **Inicializa la base de datos** y crea el usuario admin:

   ```bash
   docker compose exec trytond \
     trytond-admin -c /etc/tryton/trytond.conf -d tryton --all
   ```

   - Cuando pida **email**, usa algo como `admin@gmail.com`.
   - Después define la contraseña (`admin`).

4. **Accede a Tryton** en tu navegador:

   ```
   http://localhost:8000
   ```

## 5. Cliente web SAO (opcional)

1. Instala SAO:

   ```bash
   npm install -g tryton-sao
   ```

2. Lánzalo:

   ```bash
   sao run --server http://localhost:8000
   ```

3. Abre la URL que muestre SAO.

## 6. Personalización

- **Módulos**: añade o quita en el `Dockerfile`.
- **Configuración**: edita `trytond.conf`.
- **Persistencia**: revisa el volumen `tryton-db-data`.

¡Listo! Con esto Tryton debería funcionar correctamente en macOS ARM y Linux. 🎉
