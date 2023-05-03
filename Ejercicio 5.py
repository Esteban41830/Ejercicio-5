import csv
class PlanAhorro:
    __codigo = 0
    __modelo = ''
    __version = ''
    __valor = 0
    __cuotas = 0
    __cuotas_pagar = 0
    
    
    def __init__(self,cod,mod,ver,val,cuo,cuo_p):
        self.__codigo = cod
        self.__modelo = mod
        self.__version = ver
        self.__valor = val
        self.__cuotas = cuo
        self.__cuotas_pagar = cuo_p
    
    
    def mostrar(self):
        print('Codigo: {}; Modelo: {}; Version: {}'.format(self.__codigo,self.__modelo,self.__version))
    
    
    def getCodigo(self):
        return self.__codigo

    
    def getModelo(self):
        return self.__modelo
    
    def getVersion(self):
        return self.__version
    
    def getValor(self):
        return self.__valor
    
    def modificarValor(self,nuevo):
        self.__valor = nuevo
    
    
    def licitar(self):
        return self.__cuotas_pagar * self.__valor
    
    
    def modCuotasParalicitar(self,nuevo):
        self.__cuotas_pagar = nuevo


if __name__ == '__main__':
    
    planes = []
    archivo = open('planes.csv')
    reader = csv.reader(archivo,delimiter=';')
    for fila in reader:
        unPlan = PlanAhorro(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
        planes.append(unPlan)
        
    
    archivo.close()
    
    opcion = ''
    while opcion == 's':
        print('a-Actualizar valor')
        print('b-Mostrar codigo del plan')
        print('c-Mostrar monto para solicitar')
        print('d-Modificar cantidad de cuotas')
        print('s-Salir')
        opcion = input()
        
        if opcion == 'a':
            for i in range(len(planes)):
                planes[i].mostrar()
            
            cod = int(input('Ingrese codigo: '))
            mod = input('Ingrese modelo: ')
            ver = input('Ingrese version: ')
            
            indice = 0
            i = 0
            while indice == 0:
                if cod == planes[i].getCodigo() and mod == planes[i].getModelo() and ver == planes[i].getVersion():
                    indice = i    
                else:
                    i = i+1
                    
            valor = int(input('Ingrese el nuevo valor: '))
            planes[indice].modificarValor(valor)
            
            print('¿Que desea hacer ahora?\n')
        
        elif opcion == 'b':
            valor = int(input('Ingrese el valor: '))
            for i in range(len(planes)):
                if valor > planes[i].getValor():
                    planes[i].mostrar()
            
            print('¿Que desea hacer ahora?\n')
            
        elif opcion == 'c':
            for i in range(len(planes)):
                print('Para licitar el vehiculo: {}, {}'.format(planes[i].getModelo(),planes[i].getVersion()))
                print('El monto es de: {}\n\n'.format(planes[i].licitar()))
            
            print('¿Que desea hacer ahora?\n')
            
        elif opcion == 'd':
            cod = int(input('Ingrese el codigo: '))
            i = 0
            ban = False
            while ban == False:
                if cod == planes[i].getCodigo():
                    ban = True
                else:
                    i = i+1
            
            valor = int(input('Ingrese la cantidad de cuotas: '))
            planes[i].modCuotasParalicitar(valor)
            
            print('¿Que desea hacer ahora?\n')
        
        elif opcion == 's':
            print('\n------FIN DEL PROGRAMA-------\n')
            
        else:
            print('Ingreso mal la opcion\n')
        
