# INTA - Custom Addons módulo HR de Odoo.

### Descripción:
Módulos personalizados de Odoo (custom addons) que crean nuevos modelos y sobreescriben los existentes de acuerdo a los requerimientos del proyecto.

### Estructura del proyecto:

- Archivo ".env-example": es un archivo de ejemplo, se debe renombrar o crear un nuevo que tenga el nombre ".env".  Contiene las diferentes variables de entorno para la conexión de la aplicación a la base de datos, y a la aplicación en sí.
- Directorio "config": contiene un archivo de nombre "odoo.conf" donde se indican las credenciales de base de datos a utilizar por Odoo, y además la ruta donde se van a copiar los módulos personalizados dentro del contenedor de Docker.
- Directorio "custom_addons": contiene un directorio de nombre "custom_addons_hr_inta" que a su vez será el nombre del módulo instalable en la aplicación de Odoo.
    - Directorio "models": Se definen en archivos de extensión .py todos los modelos de Odoo heredados o nuevos.  En el archivo __init__.py se deben importar todos los archivos que contengan modelos descritos.
    - Directorio "security": contiene un archivo tipo CSV (Comma Separated Value) donde se indican los permisos para los modelos que se han creado nuevos.  Es requerido.
    - Directorio "views": contiene las vistas descritas en archivos de extensión .xml.
    - Archivo "__init__.py": realiza la importación de todo el directorio "models".
    - Archivo "__manifest__.py": se describe nombre del módulo, versión, autor, licencia, website, el módulo dependiente, las rutas de donde provendrán los datos, y finalmente indicamos si queremos que sea un módulo instalable, y si queremos que sea una aplicación.

### Instalación:

- Se clona el repositorio del mencionado proyecto.
    ```git clone https://git.com/repositorio/my_odoo_project -b my_branch odoo```
- Se configuran las credenciales en el archivo .env
- Se hace build y up del contenedor de docker:
    ```docker compose up --build -d```
- Se expone el puerto "8069" para modo desarrollo.  Para entornos de producción, se debe cambiar la siguiente línea en el "docker-compose.yml" en el tag "odoo_server", de esta forma dentro del contenedor escucha en el puerto 8069, pero desde afuera se accede con el puerto 80:
    ```
        ports:
      - "80:8069" 
    ```
- Y 'voilá', realizamos petición al "http://myip" y debemos ver la ventana de login de Odoo para introducir "email" y "password".