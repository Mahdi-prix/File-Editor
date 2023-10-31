


import os

def duzenlemek():
    klasor = input("LÜTFEN DÜZENLEMEK İSTEDİĞİNİZ DOSYANIN ADRESİNİ GİRİNİZ:")
    dosyalar = list()                   #dosyalar depolanacak
    uzantilar = list()                  #uzantılar depolanacak
    def list_dir():
        for dosya in os.listdir(klasor):
            if os.path.isdir(os.path.join(klasor,dosya)) == True:         #dosyamız bir klasör mü
                continue
            if dosya.startswith("."):            #dosyamızın bir gizli dosya olup olmadığını kontrol etmek
                continue
            else:
                dosyalar.append(dosya)
    list_dir()
    for dosya in dosyalar:                        #dosyalarımızı uzantılarına göre sınıflandırmak
        uzanti = dosya.split(".")[-1]
        if uzanti in uzantilar:                     #uzanti daha önce eklendi mi
            continue
        else:
            uzantilar.append(uzanti)
    for uzanti in uzantilar:                        # klasörler oluşturuluyor
        if os.path.isdir(os.path.join(klasor,uzanti)):
            continue
        else:
            os.mkdir(os.path.join(klasor,uzanti))
    for dosya in dosyalar:
        uzanti = dosya.split(".")[-1]
        os.rename(os.path.join(klasor,dosya),os.path.join(klasor,uzanti,dosya))

if __name__ == "__main__":
    duzenlemek()