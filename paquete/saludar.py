class Saludar():
  def __init__(self, nombre:str):
      self.nombre = nombre
  def saludar_casual(self):
    return f"Hola {self.nombre}"
  def saludar_formal(self):
    return f"Buenos días {self.nombre}"
  def saludar_educado(self):
    return f"Un placer saludarte {self.nombre}"
  def saludar_cordial(self):
    return f"Que gusto verte {self.nombre}"