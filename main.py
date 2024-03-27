import paquete.saludar as saludar
import paquete.despedirse as despedirse

def main():
  nombre = "Juan"
  saludo = saludar.Saludar(nombre)
  despedida = despedirse.Despedirse(nombre)
  print(saludo.saludar_casual())
  print(saludo.saludar_formal())
  print(saludo.saludar_educado())
  print(saludo.saludar_cordial())
  print(despedida.despedirse_formal())
  print(despedida.despedirse_casual())
  print(despedida.despedirse_educado())
  print(despedida.despedirse_cordial())

if __name__ == "__main__":
  main()  