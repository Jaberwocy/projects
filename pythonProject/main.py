
depo = float(input('Введите сумму депозита в долларах: '))
years = int(input("На какой срок открываете депозит?: "))
percent = 1.04
for year in range(1, years):
    depo = depo*percent
    print('В конце {} года получите {:.2f} долларов'.format(year, depo))

