y = 0

print ('#'*10)
print ('\033[41mATENÇÃO\033[m: Os valores numericos deste programa não são alteraveis quando o script é executado, portanto, ele ira gerar apenas datas entre 01/01/1950 a 31/12/2020, então qualquer alteração podera ser feita no script.')
print (' ')
print ('NUMERO MINIMO DE CARACTERES É 8 O E MAXIMO É 10')
print ('#'*10)
print (' ')
print ('Selecione o tipo de formatação das datas')
print (' ')
print ('[1] 31122020 (8 digitos)')
print ('[2] 12312020 (formato Ingles)')
print ('[3] 31/12/2020 (10 digitos)')
print ('[4] 12/31/2020 (formato Ingles)')
print ('[5] 31/12/20 (somente ano abreviado)')
print ('[6] 12/31/20 (formato Ingles abreviado)')
print (' ')
r=int(input('='))
print ('#'*10)
print (' ')
nome=input("nome ou local que o arquivo sera salvo:")

arquivo = open(nome, 'w')

Dia=('01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
Diaa=('10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
Mes=('01','02','03','04','05','06','07','08','09','10','11','12')
Mesa=('10','11','12')
Ano=('1950','1951','1952','1953','1954','1955','1956','1957','1958','1959','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020')
Anoa=('50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20')

if r == 1:
    while y != '31122020':
        for i1 in (Dia):
            for i2 in (Mes):
                for i3 in (Ano):
                    y=(i1+i2+i3)
                    arquivo.write(y+'\n')
                    print(y)
                    if(y=='31122020'):
                        print('Salvo como',nome)
                        arquivo.close()
                        exit()

if r == 3:
    while y != '31/12/2020':
        for i1 in (Dia):
            for i2 in (Mes):
                for i3 in (Ano):
                    y=(i1+'/'+i2+'/'+i3)
                    arquivo.write(y+'\n')
                    print(y)
                    if(y=='31/12/2020'):
                        print('Salvo como',nome)
                        arquivo.close()
                        exit()

if r == 2:
    while y != '12312020':
        for i1 in (Mes):
            for i2 in (Dia):
                for i3 in (Ano):
                    y=(i1+i2+i3)
                    arquivo.write(y+'\n')
                    print(y)
                    if(y=='12312020'):
                        print('Salvo como',nome)
                        arquivo.close()
                        exit()

if r == 4:
    while y != '12/31/2020':
        for i1 in (Mes):
            for i2 in (Dia):
                for i3 in (Ano):
                    y=(i1+'/'+i2+'/'+i3)
                    arquivo.write(y+'\n')
                    print(y)
                    if(y=='12/31/2020'):
                        print('Salvo como',nome)
                        
if r == 5:
    while y != '31/12/20':
        for i1 in (Dia):
            for i2 in (Mes):
                for i3 in (Anoa):
                    y=(i1+'/'+i2+'/'+i3)
                    arquivo.write(y+'\n')
                    print(y)
                    if(y=='31/12/20'):
                        print('Salvo como',nome)
                        arquivo.close()
                        exit()

if r == 6:
    while y != '12/31/20':
        for i1 in (Mes):
            for i2 in (Dia):
                for i3 in (Anoa):
                    y=(i1+'/'+i2+'/'+i3)
                    arquivo.write(y+'\n')
                    print(y)
                    if(y=='12/31/20'):
                        print('Salvo como',nome)
                        arquivo.close()
                        exit()
