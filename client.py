#Author: Orhan Furkan VURUCU

from socket import *
import os 
import sys
from termcolor import colored

def main():

    baslangic_metni="""
    ********************************************************
    *                                                      *
    *               Server - Client Programı               *
    *              Yazar: Orhan Furkan VURUCU              *    
    *                                                      *
    ********************************************************
    """
    print(baslangic_metni)

    sunucu_ip = "localhost"
    sunucu_port = 17100
    dosya_ismi = input(colored("[*] Sunucuya yollamak istediğiniz dosyanın uzantısını giriniz:",color="green"))
    dosya_dizini = dosya_ismi
    blocksize = 4096
    
    
    client = socket(AF_INET,SOCK_STREAM)
    client.connect((sunucu_ip,sunucu_port))
    
    if os.path.exists(dosya_dizini):
        with open(dosya_dizini,"rb") as f:
            paket = f.read(blocksize)
            
            while paket != '':
                client.send(paket)
                paket = f.read(blocksize)
                print(colored("[*] Dosya sunucuya gönderildi.",color="green"))
                print(colored("\n[*] Programdan çıkmak için q tuşuna basarak enter deyin...\n",color="red"))
                tus = input()
                if(tus=='q'):
                    sys.exit()

  

if __name__ == "__main__":
    main()