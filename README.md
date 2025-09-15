# 🔍 rockyouFilter.py

Um script Python que filtra uma wordlist rockyou.txt(ou outras com encoding=Latin-1) por palavras de um tamanho específico.
## 🚀 Funcionalidades

- Filtra palavras por tamanho exato de caracteres
- Manipula encoding Latin-1 (formato do rockyou.txt)
- Gera arquivos de saída em UTF-8
- Interface de linha de comando simples e interativa

-------------------------------------------------------------------------------------------------------------------------

No Kali Linux, o rockyou.txt vem comprimido como rockyou.txt.gz na pasta /usr/share/wordlists/.

Para descomprimir, use os seguintes comandos:

1. Navegue até a pasta
   
cd /usr/share/wordlists/

2. Descomprima o arquivo

sudo gunzip rockyou.txt.gz

Quando rodar o script com: 'python rockyouFilter', use como arquivo de leitura a seguinte string '/usr/share/wordlists/rockyou.txt'.
