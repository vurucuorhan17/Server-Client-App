#Author: Orhan Furkan VURUCU

from threading import *
from socket import *
import sys
from termcolor import colored


def tcp_denetle(istemci_soket):

    request = istemci_soket.recv(4096)
    dosya = open("kaydedilen-dosya.png","wb")
    dosya.write(request)
    dosya.close()
    print(colored("[*] Dosya kaydedildi.",color="green"))
    print(colored("\n[*] Programdan çıkmak için q tuşuna basarak enter deyin...\n",color="red"))
    istemci_soket.close()


def main():
    
    baslangic_metni="""
    ********************************************************
    *                                                      *
    *               Server - Client Programı               *
    *              Yazar: Orhan Furkan VURUCU              *    
    *                                                      *
    ********************************************************
    """

    sunucu_ip = "localhost"
    sunucu_port = 17100
    sunucu = socket(AF_INET,SOCK_STREAM)
    sunucu.bind((sunucu_ip,sunucu_port))
    sunucu.listen(5)

    print(baslangic_metni) 
    print(colored("[*] %s:%d dinleniyor..." %(sunucu_ip,sunucu_port),color="green"))
    
    
    while True:
        
        istemci,adres = sunucu.accept()
        print(colored("[*] %s:%d adresinden gelen bağlantı kabul edildi" %(adres[0],adres[1]),color="green"))
        thread = Thread(target=tcp_denetle,args=(istemci,))
        thread.start()

        tus = input()
        if(tus=='q'):
            sys.exit()

if __name__ == "__main__":
    main()