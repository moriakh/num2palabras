import math
def num2palabras(num):
    primeros15 = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete',
                  'ocho', 'nueve', 'diez', 'once', 'doce', 'trece', 'catorce', 'quince']
    decenas_num = [0,0,0, 30, 40, 50, 60, 70, 80, 90]
    decenas_palabras = ['','','','treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']
    centenas_num = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]
    centenas_palabras = [0, 'ciento', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seiscientos', 'setescientos', 'ochocientos', 'novecientos']
    miles_num = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]

    if num <= 15:
        return primeros15[num]
    elif len(str(num))==2:
        if num <= 19: # 17
            return 'dieci' + num2palabras(num - 10)
        elif num == 20:
            return 'veinte'
        elif num <= 29:
            return 'veinti' + num2palabras(num - 20)
        else:
            if num%10 == 0:
                return decenas_palabras[num//10]
            else:
                return decenas_palabras[num//10] + ' y ' + num2palabras(num%10)
    elif len(str(num))==3:
        if num == 100:
            return 'cien'
        else:
            return f'{centenas_palabras[num//100]} '+ num2palabras(num - centenas_num[num//100])
    elif len(str(num))==4:
        if num == 1000:
            return 'mil'
        elif num <= 1999:
            return 'mil ' + num2palabras(num%1000)
        else:
            return num2palabras(num//1000) + ' mil ' + num2palabras(num%1000)    
    elif len(str(num))<=6:
        if num == 10000:
            return "diez mil"
        else:
            return num2palabras(num//1000) + ' mil ' + num2palabras(num%1000)
    elif len(str(num))<=9:
        if num == 1000000:
            return 'un millón'
        elif num <= 1999999:
            return 'un millón ' + num2palabras(num%1000000)
        else:
            return num2palabras(num//1000000) + ' millones ' + num2palabras(num%1000000)
    elif len(str(num))<=15:
        if num == 1000000000:
            return 'un billón'
        elif num <= 1999999999:
            return 'un billón ' + num2palabras(num%1000000000)
        else:
            return num2palabras(num//1000000000) + ' billones ' + num2palabras(num%1000000000)
    else:
        return 'No implementado'

print(num2palabras(999999999999999))
