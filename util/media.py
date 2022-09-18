import csv
import math

def list_to_csv(list,file):
    with open(file, 'w',newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        #writer.writerow(['local','preco','metragem','quartos','garagens','banheiros','bairro'])
        writer.writerows(list)

imoveis = []
with open('imoveis.csv', 'r', encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        
        imovel = []
        for r in row:
            
            if '-' in r:
                this_row = r.split('-')
                try:
                    r = math.ceil((int(this_row[0])+int(this_row[1]))/2)
                except:
                    pass
            imovel.append(r)
        imoveis.append(imovel)
        



list_to_csv(imoveis,'imoveis_media.csv')