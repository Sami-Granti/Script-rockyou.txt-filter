# Script-rockyou.txt-filter
Esse é um script simples em python que filtra uma wordlist em encode latin-1 por palavras de um determinado tamanho. 
A saída é um arquivo txt.
O arquivo foi criado com a finalidade de filtrar a wordlist rockyou.txt para o desafio crack_the_hash do site TryHackMe.

-------------------------------------------------------------------------------------------------------------------------

No Kali Linux, o rockyou.txt vem comprimido como rockyou.txt.gz na pasta /usr/share/wordlists/.
Para descomprimir, use os seguintes comandos:

# 1. Navegue até a pasta
cd /usr/share/wordlists/

# 2. Descomprima o arquivo
sudo gunzip rockyou.txt.gz

Quando rodar o script com: 'python rockyouFilter', use como arquivo de leitura a seguinte string '/usr/share/wordlists/rockyou.txt'.
