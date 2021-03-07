# Nele Saks ITT20
# 07.03.2021
# Kodutöö 03

#3.1 Ülikooli vastuvõetud
fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []
for rida in fail:
    vastuvõetud.append(int(rida))
fail.close()
aasta = int(input("Palun sisestage, millise aasta andmeid vajate: "))
if aasta == 2011:
    print(aasta, "aastal oli vastuvõetuid",vastuvõetud[0])
elif aasta == 2012:
    print(aasta, "aastal oli vastuvõetuid",vastuvõetud[1])
elif aasta == 2013:
    print(aasta, "aastal oli vastuvõetuid",vastuvõetud[2])
elif aasta == 2014:
    print(aasta, "aastal oli vastuvõetuid",vastuvõetud[3])
elif aasta == 2015:
    print(aasta, "aastal oli vastuvõetuid",vastuvõetud[4])
elif aasta == 2016:
    print(aasta, "aastal oli vastuvõetuid",vastuvõetud[5])
elif aasta == 2017:
    print(aasta, "aastal oli vastuvõetuid",vastuvõetud[6])
elif aasta == 2018:
    print(aasta, "aastal oli vastuvõetuid",vastuvõetud[7])
elif aasta == 2019:
    print(aasta, "aastal oli vastuvõetuid",vastuvõetud[8])
print("")

#3.2 Jänesevanemate mure ver. 3
ringid = int(input("Sisesta ringide arv: "))
porgandid = 0
for i in range(1,ringid+1):
    if i %2 == 0:
        porgandid = porgandid+i
    i = i+1
print("Porgandite koguarv on",porgandid)
print("")

#3.3 Sissetulekud
fail = open("konto.txt", encoding="UTF-8")
sissetulekud = []
for rida in fail:
    sissetulekud.append(float(rida))
fail.close()
for arv in sissetulekud:
    if arv >=0:
        print(arv)
print("")

#3.4 Jukebox
failinimi = input("Palun sisestage failinimi:")
fail = open(failinimi, encoding="UTF-8")
muusikapalad = []
for rida in fail:
    muusikapalad.append(rida)
fail.close()
print("Muusikapalade valik: ")
i = 1
for pala in muusikapalad:
    print(str(i) + ". "+muusikapalad[i-1])
    i = i+1
print("")
mitmes = int(input("Valige laulu järjekorranumber: "))
print("Mängitav muusikapala on "+muusikapalad[mitmes-1])
print("")

#3.5 Tahvli juurde
failinimi = input("Palun sisestage failinimi:")
fail = open(failinimi, encoding="UTF-8")
õpilased = []
for rida in fail:
    õpilased.append(rida)
fail.close()
from datetime import *
päev = datetime.now().day
print("Vastama tuleb:",õpilased[päev-1])




