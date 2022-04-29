import csv
class PlanAhorro:
    __CodigoDePlan = 0
    __modelo = ''
    __version = ''
    __ValorAuto = 0.0
    __cantidadCuotas = 0
    __Cuotasparalicitar = 0
    __ValorCuota = 0.0
    
    def __init__(self,CodigoDePlan,Modelo,Version,ValorAuto,CantidadCuotas,Cuotasparalicitar):
        self.__CodigoDePlan = CodigoDePlan
        self.__Modelo = Modelo
        self.__Version = Version
        self.__ValorAuto = ValorAuto
        self.__CantidadCuotas = CantidadCuotas
        self.__Cuotasparalicitar = Cuotasparalicitar
        self.__ValorCuota = (self.__ValorAuto/self.__CantidadCuotas) + self.__ValorAuto * 0.10
    
    def Mostrar(self):
        return 'Codigo de Plan: {}\nModelo: {}\nVersion: {}'.format(self.__CodigoDePlan,self.__Modelo,
                                                             self.__Version)
    
    def Actualziar(self):
        self.__CodigoDePlan = int(input('Valor actual del vehiculo: '))
        self.__Modelo = input('Ingrese nuevo modelo: ')
        self.__Version = input('Ingrese nueva version: ')
        self.__ValorAuto = input('Ingrese nuevo valor del auto: ')
        
    def MostrarXvalor(self,Valor):
        if self.__ValorCuota < Valor:
            return 1
        else:
            return 0
    
    def MostrarMonto(self):
        print('Para licitar el Auto necesita paga: '.format(self.__CantidadCuotas * self.__ValorCuota))
    
    def ModificarCuotas(self):
        self.__Cuotasparalicitar = int(input('Ingrese el nuevo valor: '))
        
    def buscar(self,Codigo,opcion):
        if self.__CodigoDePlan == Codigo:
            if opcion == 'c':
                lista[i].MostrarMonto()
            else:
                lista[i].ModificarCuotas
            return 1
        else:
            return -1
        
        
        
    
    
if __name__=='__main__':
    
    archivo = open('Automoviles.csv')
    reader = csv.reader(archivo,delimiter=',')
    lista = []
    
    for fila in reader:
        Auto = PlanAhorro(fila[0],fila[1],fila[2],fila[3],fila[4])
        lista.append(Auto)
    
    opcion = ''
    print('Ingrese una de las opciones: ')
    while opcion != 's':
        print('a)_Actualizar el valor de un vehiculo de cada plan')
        print('b)_Mostrar plan, modelo y version por un valor')
        print('c)_Mostrar el monto a pagar para licitar')
        print('d)_Modificar las cuotas a pagar')
        print('s)_Salir')
        opcion = input()
        
        if opcion == 's':
            break
            
        elif opcion == 'a':
            for i in range(len(lista)):
                lista[i].Mostrar()
                lista[i].Actualizar()
                
            print('Que desea hacer ahora: ')
        
        elif opcion == 'b':
            valor = float(input('Ingrese el valor: '))
            for i in range(len(lista)):
                if lista[i].MostrarXvalor(valor) == 1:
                    lista[i].Mostrar()
                
            print('Que desea hacer ahora: ')
    
        elif opcion == 'c':
            Codigo = int(input('Ingrese codigo del plan: '))
            for i in range(len(lista)):
                if lista[i].buscar(Codigo,opcion) == 1:
                    break
                
            print('Que desea hacer ahora: ')

        elif opcion == 'd':
            Codigo = int(input('Ingrese codigo del plan: '))
            for i in range(len(lista)):
                if lista[i].buscar(Codigo,opcion) == 1:
                    break
        
            print('Que desea hacer ahora: ')

        else:
            print('Ingreso mal la opcion. Ingrese nuevamente: ')
            
        
        
        

    