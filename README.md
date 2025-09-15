# Script rockyouFilter.py

Esse é um script simples em python que filtra uma wordlist em encode latin-1 por palavras de um determinado tamanho.\n
A saída é um arquivo txt.\n
O arquivo foi criado com a finalidade de filtrar a wordlist rockyou.txt para o desafio crack_the_hash do site TryHackMe.

-------------------------------------------------------------------------------------------------------------------------

No Kali Linux, o rockyou.txt vem comprimido como rockyou.txt.gz na pasta /usr/share/wordlists/.\n
Para descomprimir, use os seguintes comandos:

1. Navegue até a pasta\n
cd /usr/share/wordlists/

2. Descomprima o arquivo\n
sudo gunzip rockyou.txt.gz

Quando rodar o script com: 'python rockyouFilter', use como arquivo de leitura a seguinte string '/usr/share/wordlists/rockyou.txt'.\n
