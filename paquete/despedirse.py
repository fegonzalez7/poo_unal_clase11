class Despedirse:
  def __init__(self, nombre:str):
    self.nombre  = nombre
  
  def despedirse_formal(self):
    return f"Adios {self.nombre}"
  
  def despedirse_casual(self):
    return f"Chao {self.nombre}"
  
  def despedirse_educado(self):
    return f"Hasta luego {self.nombre}"
  
  def despedirse_cordial(self):
    return f"Nos vemos {self.nombre}"