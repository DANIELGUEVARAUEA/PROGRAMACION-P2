
from poo_clima import ClimaSemanal                  #de donde se recolecta la informacion

def ejecutar_poo():            #llamados
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    clima.mostrar_promedio()


def main():
    ejecutar_poo()        #ejecuta 


if __name__ == "__main__":
    main()
