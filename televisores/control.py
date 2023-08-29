from televisores.tv import TV

def __init__(self, tv):
    self.tv = tv

def enlazar(self, tele):
    self.tv = tele
    self.tv.setControl(self)

#TV
def getTv(self):
    return self.tv

def setTv(self, tele):
    self.tv = tele

#Canal
def getCanal(self):
    return self.tv.getCanal()

def setCanal(self, chanel):
    self.tv.setCanal(chanel)

#canalUP-DOWN
def canalUp(self):
    self.tv.canalUp()

def canalDown(self):
    self.tv.canalDown()

#Volumen
def getVolumen(self):
    return self.tv.volumenDown()

def setVolumen(self,volume):
    self.tv.setVolumen(volume)

#volumenUP-DOWN
def volumenUp(self):
    self.tv.volumenUp()

def volumenDown(self):
    self.tv.volumenDown()

#turnON-OFF
def turnOn(self):
    self.tv.setEstado(True)

def turnOff(self):
    self.tv.setEstado(False)



