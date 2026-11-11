from netmiko import ConnectHandler
import datetime

switch = {
    'device_type': 'cisco_ios',
    'host':   '10.8.63.5',      
    'username': 'Jimenez',    
    'password': 'Cisco123',   
}

cis_rules = [
    'service password-encryption',         
    'no ip http server',                    
    'no ip http secure-server',           
    'banner motd # ACCESO RESTRINGIDO #',  
    'line vty 0 4',
    'transport input ssh',                  
    'exit'
]

print(f"Conectando al switch {switch['host']}...")
try:
    net_connect = ConnectHandler(**switch)
    
    print("Aplicando reglas CIS...")
  
    config_output = net_connect.send_config_set(cis_rules)
    

    net_connect.save_config()
    
 
    print("Generando informe...")
    verificacion = net_connect.send_command("show run | include service password|http|banner|transport")
    

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("informe_cis_switch.txt", "w") as file:
        file.write(f"--- INFORME DE HARDENING CIS ---\n")
        file.write(f"Fecha: {timestamp}\n")
        file.write(f"Equipo: Switch Cisco IOSvL2 ({switch['host']})\n\n")
        file.write("--- COMANDOS APLICADOS ---\n")
        file.write(config_output + "\n\n")
        file.write("--- VERIFICACIÓN EN LA CONFIGURACIÓN ACTUAL ---\n")
        file.write(verificacion + "\n")
        
    print("¡Éxito! El script terminó y se generó 'informe_cis_switch.txt'.")
    net_connect.disconnect()

except Exception as e:
    print(f"Error al conectar o aplicar configuración: {e}")
