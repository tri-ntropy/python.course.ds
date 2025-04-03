# El entorno de desarrollo básico para la Ciencia de Datos

## Creación y respaldo del entorno de desarrollo
Para empezar, se debe crear el entorno de desarrollo con las herramientas básicas que permitirán a Python tener todo el abanico de herramientas para realizar cálculo númerico a alta velocidad y así, empezar a trabajar la ciencia de datos.

Para ello, con conda por medio del Terminal (Anaconda Prompt Powershell en Windows) usamos el siguiente comando

```bash
conda create -n sci python numpy scipy pandas matplotlib seaborn jupyter ipython sympy
```

Se debe recordar que 

```bash
conda create 
```

es el comando para crear un nuevo entorno

```bash
-n <nombre>
```

el nombre que queremos darle al entorno (en este caso **sci**), y finalmente

```bash
<paquete1> <paquete2> <paquete3>
```

la lista de paquetes que deseamos se instalen en el entorno, para los cuales conda resolvera todas las dependencias.

Dado que no se están especificando versiones, conda creará el entorno de tal manera que se ofrezca la versión más reciente de cada una de las paqueterías **LIBRE** de problemas de dependencias. 

Esto último significa que no siempre instalará la versión más reciente de alguna paquetería, por lo cual, dependiendo el proyecto, será necesario de revisar más a detalle según sea el caso. Por el contrario, si el proyecto requiere una versión más antigua de alguna paquetería, también se debe revisar a detalle.

La manera de preservar y compartir entornos de desarrollo mediante conda es crear un archivo `.yml` que contenga la descripción y especificaciones del entorno, para ello, teniendo activado el ambiente que desea preservar, se emplea el siguiente comando

```bash
conda env export > <nombre>.yml
```

de nuevo, `<nombre>` es el nombre que le dimos al ambiente. Escrito de esta manera, el archivo `.yml` será creado en la ruta *raíz*, es decir, en distribuciones Linux será el **home**, mientras que en Windows será en `users/nombre_de_usuario`.

El archivo `.yml` creado contiene todas las especificaciones del entorno, así como la versión precisa de cada paquetería y dependencia del mismo. Es altamente recomendable que, una vez asegurado que el entorno funciona correctamente para nuestro proyecto y se cree el archivo `.yml`, no se edite manualmente a menos que 

1. Se sepa exactamente lo que se está haciendo
2. Sea parte del proyecto editarlo manualmente
3. Recrear el ambiente paso a paso y luego exportar el archivo sea mucho más complicado

Esto es debido a que los archivos `.yml` tienen una sintaxis específica y que las especificaciones para cada paquetería son bastante precisas y refieren a una versión en particular del repositorio/canal de conda.

Para crear un entorno a partir del archivo `.yml` simplemente usa el comando

```bash
conda env create -f <nombre>.yml
```