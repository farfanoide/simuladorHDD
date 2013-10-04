Algunas consideraciones previas:
=============

Acerca de...

**pymulator.ini.example**:
	Este es un archivo que contiene configuraciones iniciales para que al correr por primera vez el simulador ya se encuentre listo para ejecutarse.

**Atajos de teclado**:
	
	Aunque se encuentran los respectivos botones "configurar", existe un atajo de teclado
	con el que se puede configurar el simulador en cualquier momento y desde cualquier 
	pantalla. Basta presionar <F1> y se lanzara la pantalla de configuraciones.

	La tecla <ESC> provee una forma rapida de salida del simulador (de la pantalla de 
	configuraciones, si se encontrase en ella).

=============

**Uso del software**:
=============

Configurar
=============

En esta pantalla encontraran todas las opciones para configurar el estado inicial del simulador y los requisitos que se atenderan.

**Direccion inicial** hace referencia a la direccion que tiene el cabezal del disco al 
momento de comenzar a atender los requerimientos.

**Posicion inicial** se refiere a la posicion en la que se encuentra el cabezal al momento de 
comenzar a atender los requerimientos.

**Archivo** permite proporcionarle al simulador un archivo de texto plano donde se encuentren los requerimientos.

**Lista de Requerimientos** permite ingresar el lote de requerimientos por teclado.

**Carga aleatoria**

	El software tiene la opcion de generar una lista de requerimientos al azar.

	**Requerimientos** sirve para configurar la cantidad de requerimientos al azar que se desean.

	**Page Faults** sirve para configurar la cantidad de page faults al azar que se desean.

El Simulador toma por defecto una lista aleatoria de 25 requisitos en total. En la pantalla de
configuraciones, se toma como entrada la ultima modificada por el usuario.
Supongamos que se configura una ruta a un archivo y luego se ingresa manualmente un lote de requisitos; se tomara como entrada para la simulacion el lote ingresado manualmente.

Los **requerimientos** deben ingresarse separados por un espacio y los **page-faults** antepuestos con un signo "-".
Ej: 23 512 -34 44 200 -500 344

Graficar:
=============

En la parte izquierda de la pantalla se encuentra el menu con las opciones:

	*-FCFS, SSTF, SCAN, CSCAN, LOOK, CLOOK*: algoritmos de atencion de requerimientos.

	-*Configurar*: Pantalla de configuracion del simulador.

	-*"x"*: borrar el grafico de la pantalla.

	-*"<"*: volver al menu principal.

La **grafica** consta de dos partes:
	
	**-Atencion de Requisitos** donde se muestra el orden en que fueron siendo atendidos los
	mismos. En color rojo se dibujan los Page-Faults, mientras que el resto se encuentra en
	color verde.

	**- Resultados** donde se informa al usuario la **cantidad de movimientos** que realizo el cabezal lector, la **direccion** con la que finalizo el mismo y el **algoritmo** utilizado.

==============================

