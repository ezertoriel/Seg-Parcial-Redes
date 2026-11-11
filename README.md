# Seg-Parcial-Redes

## Link del Video


## Propósito
Tener servicio de SNMP en la red, un Router DHCP que este dando direcciones IP a los dispositivos, y un servicio Zabbix para monitorear los dispositivos (Router y Switch). Complementado con direccionamiento VLAN, y por Seguridad un Servidor Radius de NPS por Windows Server

##descripción de lo implementado
En esta topología se implementó un Servidor Radius para autenticación del usuario del Switch, un Servidor Zabbix con SMB con conexión de solo lectura en el Router, también implemente SSH entre el switch y el Router, y por último hubo un Router DHCP con Router-on-Stick y dos vlan la VLAN10 de servidores y VLAN20 de Usuarios. 

## Diagrama Lógico
<img width="1024" height="765" alt="image" src="https://github.com/user-attachments/assets/170d096a-36a9-41e7-8e3c-2a79c6806b81" />


---
## Topologia
<img width="663" height="457" alt="image" src="https://github.com/user-attachments/assets/e0830fe6-a692-4516-b29c-55bc6e10720a" />



---

## Dispositivos utilizados
1. Router (DHCP)
2. Switch
3. Servidor (SNMP)
4. Servidor (NPS)
5. Usuario (Linux)

---

## Direccionamiento IP (basado en los ultimos digitos de mi matricula 0863)
| Red | Equipo/Puerto | IP |
| :--- | :---: | ---: |
| VLAN10 | Router GIG0/0.10 | 10.8.63.1 |
| VLAN20 | Router GIG0/0.20 | 10.8.64.1 |
| LAN | Switch VLAN10 | 10.8.63.5 |
| VLAN10 | Server Zabbix e1 | DHCP |
| VLAN10 | Server NPS e0 | 10.8.63.10 |
| VLAN20 | Usuario e0 | DHCP |


---

## Configure una comunidad SNMP de solo lectura en el router y demuestre que las lecturas
<img width="1366" height="654" alt="image" src="https://github.com/user-attachments/assets/e40e2ca8-bb61-4156-93c3-9606eb49ea63" />

## Conexión SSH de Router a Switch
<img width="795" height="534" alt="image" src="https://github.com/user-attachments/assets/2c28e8ae-7b46-41c3-b1bc-875c3ccb3ea8" />

## Conexión SSH de Switch a Router
<img width="803" height="393" alt="image" src="https://github.com/user-attachments/assets/ee46141c-9189-4bcc-b9f8-60f702decdca" />

## Router-on-Stick y DHCP
<img width="751" height="485" alt="image" src="https://github.com/user-attachments/assets/c5e4ea88-ec67-40a7-a35b-23581afc8d1b" />

## Switch Conectado al NPS
<img width="805" height="543" alt="image" src="https://github.com/user-attachments/assets/2e664100-95b8-4fbd-b8a0-4c10f8966ce3" />

<img width="811" height="625" alt="image" src="https://github.com/user-attachments/assets/77ac9518-72dc-46d0-9908-872e000470e5" />


