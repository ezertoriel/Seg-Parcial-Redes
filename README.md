# Seg-Parcial-Redes

## Link del Video


## Propósito
Tener servicio de SNMP en la red, un Router DHCP que este dando direcciones IP a los dispositivos, y un servicio Zabbix para monitorear los dispositivos (Router y Switch). Complementado con direccionamiento VLAN, y por Seguridad un Servidor Radius de NPS por Windows Server

##descripción de lo implementado


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

## Direccionamiento IP
| Red | Equipo/Puerto | IP |
| :--- | :---: | ---: |
| LAN | Router GIG0/0 | 10.8.63.1 |
| LAN | Switch VLAN1 | 10.8.63.5 |
| LAN | Server e0 | DHCP |
