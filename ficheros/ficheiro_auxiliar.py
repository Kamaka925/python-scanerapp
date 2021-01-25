import nmap
nm = nmap.PortScanner()

class DIS:

    def __init__(self, ip, mac, fabricante, estado):
        self.ip = ip
        self.mac = mac
        self.fabricante = fabricante
        self.estado = estado


class ESCANEO:

    def __init__(self, ip, tipo):
        self.ip = ip
        self.tipo = tipo

    def lista_hosts():
        nm = nmap.PortScanner()
        nm.scan(hosts='192.168.0.1/24', arguments='-sP')
        dispositivos = []
        for ip in nm.all_hosts():
            host = nm[ip]
            mac = "indisponível"
            vendorName = "indisponível"
            if 'mac' in host['addresses']:
                mac = host['addresses']['mac']
                if mac in host['vendor']:
                    vendorName = host['vendor'][mac]
            if host['status']['state'] == 'up':
                status = 'Ativo'
            else:
                status = 'Desativado'
            dispositivos.append(DIS(ip, mac, vendorName, status))
        return dispositivos
