# Software-Defined Networks

Implementación de una topología dinámica y un *Firewall* a nivel de capa de enlace a partir de la utilización de *OpenFlow*. La emulación del comportamiento de la topología se realiza a través de *mininet*.

### Requerimientos

- Python (https://www.python.org/downloads/)
- Mininet (https://mininet.org/)
- Wireshark (https://www.wireshark.org/)

Para confirmar que las instalaciones se hayan realizado de forma correcta se puede realizar la siguiente ejecución con *Mininet* desde el directorio compartido donde se posea el archivo ```topo.py``` con la topología implementada, seleccionando arbitrariamente un número de switches (en este caso n=3).

```console
$ sudo mn --custom topo.py --topo=chaintopo,3
```

También se puede probar utilizando el comando *pingall* en el entorno de Mininet y poder registrar el envío y recepción de los mensajes en *Wireshark*.

```console
$ sudo mn --custom topo.py --topo chaintopo,3 --test pingall
```
