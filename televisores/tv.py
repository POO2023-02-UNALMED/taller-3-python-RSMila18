from televisores.marca import Marca

class TV:
    def __init__(self, marca, canal, precio, estado, volumen, control):
        self.__marca = marca
        self.__canal = canal
        self.__precio = precio
        self.estado = estado
        self.__volumen = volumen
        self.__control = control
        numTV = 0

    def TV(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.canal = 1
        self.volumen = 1
        self.precio = 500
        numTV += 1
    
    #Marca
    def getMarca(self):
        return self.marca
    
    def setMarca(self, brand):
        self.marca = brand
    
    #Canal
    def getCanal(self):
        return self.canal
    
    def setCanal(self,chanel):
        if chanel > 0 and self.estado == True and chanel < 121:
            self.canal = chanel
    
    #Precio
    def getPrecio(self):
        return self.precio
    
    def setPrecio(self, price):
        self.precio = price
    
    #Volumen
    def getVolumen(self):
        return self.volumen
    
    def setVolumen(self, volume):
        if volume > -1 and self.estado == True and volume < 8:
            self.volumen = volume
    
    #Control
    def getControl(self):
        return self.control
    
    def setControl(self, r_control):
        self.control = r_control
    
    #Estado
    def getEstado(self):
        return self.estado
    
    def setEstado(self, state):
        self.estado = state

    #canalUp
    def canalUp(self):
        if self.canal < 120 and self.estado == True:
            self.canal += 1
    
    #canalDown
    def canalDown(self):
        if self.volumen > 1 and self.estado == True:
            self.volumen  -= 1
    
    #volumenUp
    def volumenUp(self):
        if self.volumen < 7 and self.estado == True:
            self.volumen += 1
    
    #volumenDown
    def volumenDown(self):
        if self.volumen > 0 and self.estado == True:
            self.volumen -= 1
    
    #numTV
    def getNumTV(numTV):
        return numTV
    
    def setNumTV(numTV, number):
        numTV = number
    
    #turnOn
    def turnOn(self):
        self.setEstado(False)
    
    #turnOff
    def turnOff(self):
        self.setEstado(False)
    

    

    