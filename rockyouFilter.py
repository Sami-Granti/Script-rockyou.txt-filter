print('Esse programa recebe um arquivo com encoding=latin-1 e filtra por palavras do tamanho que preferir.')
print('O script foi feito para filtrar preferencialmente o rockyou.txt\n')
nome_arquivo = input('Escreva o arquivo de leitura com seu pwd: ')
tamanho = int(input('Escreva o tamanho das strings que selecionarei: '))
with open(nome_arquivo, 'r', encoding='latin-1') as arquivoLeitura:
    nome_destino = input('Escreva nome de seu arquivo destino: ') + '.txt'
    with open(nome_destino, 'w', encoding='utf-8') as arquivoFim:
        for linha in arquivoLeitura:
            linhaLimpa = linha.strip()
            if len(linhaLimpa) == tamanho:
                arquivoFim.write(linhaLimpa + '\n')