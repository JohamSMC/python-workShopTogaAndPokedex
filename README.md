# Python Workshop Toga and API pokeDex

La aplicación fue desarrollada en ***python*** y con la libreria ***toga***.

##  Pasos para ejecutar la Apliación :page_facing_up:

### Primer paso:
> Se sugiere crear un entorno virtual, para lo cual se debe tener instalado ***python*** y el gestor de paquetes ***PIP***

### Segundo paso:
> Instalar **virtualenv**

```
python -m pip install virtualenv
```

### Tercer paso:
> Despues procedemos a crear un entorno virutal

```
python -m venv nombreEntornoVirtual
```

### Cuarto paso:
> Despues de crear el entorno [virtual](#tercer-paso), inicializamos el entorno virtual, para esto nos ubicamos
> en la ruta 

 ``../nombreEntornoVirtual/Scripts/``

>y ejecutamos la siguiente linea:

```
activate
```
>o en Linux
```
source activate
```
### Quinto paso:
> Nos ubicamos en la carpeta donde descargarmos el proyecto y verificamos que existe el archivo
***``requirements.txt``***

> y ejecutamos el comando:

```
pip install -r requirements.txt
```
> Esto instalara las dependencias necesarias entre estas **toga**
> Si se presensta algun error mirrar la documentación [pip toga](https://pypi.org/project/toga/) ó [Your first Toga app](https://toga.readthedocs.io/en/latest/tutorial/tutorial-0.html)

### Sexto paso:
> Despues procedemos a ejecutar la apliación ("Estando Ubicados en la raiz del proyecto"):

```
python -m main
```




