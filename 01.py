def separa_ip_em_octetos(endereco_ip):
    return endereco_ip.split('.')


def valida_ip(endereco_ip):
    octetos = separa_ip_em_octetos(endereco_ip)

    for octeto in octetos:
        octeto = int(octeto)
        if octeto < 0 or octeto > 255:
            return False
    return True


def le_arquivo(arquivo):
    arquivo_entrada = open(f'{arquivo}', 'r')
    retorno = arquivo_entrada.readlines()
    arquivo_entrada.close()
    return retorno


def escreve_ip(arquivo, lista_ip):
    for i in range(len(lista_ip)):
        arquivo.write(lista_ip[i])


def grava_arquivo(arquivo, validos_ips, invalidos_ips):
    arquivo = open(f'{arquivo}', 'w')

    arquivo.write('[IPs Validos]\n')
    escreve_ip(arquivo, validos_ips)

    arquivo.write('\n[IPs Invalidos]\n')
    escreve_ip(arquivo, invalidos_ips)

    arquivo.close()


if __name__ == '__main__':
    ips_validos = []
    ips_invalidos = []

    linhas_do_arquivo = le_arquivo('01_entrada.txt')

    for ip in linhas_do_arquivo:
        if valida_ip(ip):
            ips_validos.append(ip)
        else:
            ips_invalidos.append(ip)
    grava_arquivo('01_saida.txt', ips_validos, ips_invalidos)
