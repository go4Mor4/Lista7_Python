def validaIP(ipAddress):
    blocos = ipAddress.split('.')
    for i in blocos:
        i = int(i)
        if i < 0 or i > 255:
            return False
    return True
arquivoEntrada = open('01_entrada.txt', 'r')
linhas = arquivoEntrada.readlines()
arquivoEntrada.close()
ipsValidos = []
ipsInvalidos = []
for ip in linhas:
    if validaIP(ip) == True:
        ipsValidos.append(ip)
    else:
        ipsInvalidos.append(ip)
arquivoSaida = open('01_saida.txt', 'w')
arquivoSaida.write('[IPs Validos]\n')
for i in range(len(ipsValidos)):
    arquivoSaida.write(ipsValidos[i])
arquivoSaida.write('\n[IPs Invalidos]\n')
for i in range(len(ipsInvalidos)):
    arquivoSaida.write(ipsInvalidos[i])
arquivoSaida.close()