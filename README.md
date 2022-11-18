# Software-Defined Networks

Implementación de una topología dinámica y un *Firewall* a nivel de capa de enlace a partir de la utilización de *OpenFlow*. La emulación del comportamiento de la topología se realiza a través de *mininet*.

### Requerimientos

- Python (https://www.python.org/downloads/)
- Mininet (https://mininet.org/)
- Wireshark (https://www.wireshark.org/)
- POX (suele venir incluido en la instalación de Mininet pero si no puede obtenerse de http://noxrepo.github.io/pox-doc/html/)

Importante: asegurarse de que la carpeta `tp2-intro` esté en el mismo directorio que la carpeta `pox`.

#### Topología

Para confirmar que las instalaciones se hayan realizado de forma correcta se puede realizar la siguiente ejecución con *Mininet* desde el directorio compartido donde se posea el archivo ```topo.py``` con la topología implementada seleccionando arbitrariamente un número de switches (en este caso 5).

```console
$ sudo mn --custom topo.py --topo=chaintopo,5
```

También se puede probar utilizando el comando *pingall* en el entorno de Mininet, verificando que sea posible registrar el envío y recepción de mensajes en *Wireshark*.

```console
$ sudo mn --custom topo.py --topo chaintopo,5 --test pingall
```

#### Controlador

A continuación, se explica cómo ejecutar controladores desarrollados con POX, una plataforma para desarrollar controladores SDN.
Mininet se conecta al controlador mediante una dirección y puerto específicos (el puerto estándar de OpenFlow es el 6633), por lo que debemos correr el controlador escuchando en dicho socket. Para ello antes de realizar la ejecución debemos realizar los siguientes pasos:

En una terminal con Mininet, crear un symlink en el directorio de pox `/pox/pox/samples`.

```console
$ cd ~/pox/pox/samples/
$ ln -s ../../../tp2-intro/src/firewall.py firewall.py
```

Teniendo el symlink, todas las siguientes veces para levantar el controlador bastará con ejecutar de la siguiente manera, con la opción de elegir el modo *verboso*:

```console
$ cd ~/pox/
$ ./pox.py --verbose samples.firewall forwarding.l2_learning
```

Con el controlador corriendo, podemos testear que la conexión se haya realizado efectivamente, por ejemplo, con un *pingall*. Para ello, sin cerrar la terminal donde levantamos el controlador, abriremos una nueva terminal con Mininet y haremos una ejecución con las siguientes opciones, y veremos el tráfico reflejado en la terminal donde habíamos levantado el controlador.

```console
$ cd ~/tp2-intro/src/
$ sudo mn --custom topo.py --topo chaintopo,5 --mac --switch ovsk --controller remote --test pingall
```
Si se quisiera realizar la ejecución con el modo interactivo, puede hacerse con el siguiente comando que tras la inicialización de la red y la conexión con el controlador se permitirá que el usuario ingrese input. En este caso, simplemente bastará con ingresar `pingall`.

```console
$ cd ~/tp2-intro/src/
$ sudo mn --custom topo.py --topo chaintopo,5 --mac --switch ovsk --controller remote
```
