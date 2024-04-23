
import unittest    

def buscar_datos(*args, **kwargs):
    datos_encontrados = []

    if "database" in kwargs:
        database = kwargs["database"]
        for arg in args:
            found = False
            for key, data in database.items():
                if arg in data.values():
                    datos_encontrados.append(arg)
                    found = True
                    break 
            if not found:
                print(f"La palabra '{arg}' no está en la base de datos.")

    print("Datos encontrados en la base de datos:", datos_encontrados)
    return datos_encontrados

class TestBuscarDatos(unittest.TestCase):
    
    database = {
        "persona1": {
            "primer_nombre": "Miguel",
            "segundo_nombre": "Angel",
            "primer_apellido": "Borja",
        },

        "persona2": {
            "primer_nombre": "Julian",
            "primer_apellido": "Alvarez",
        },

        "persona3": {
            "primer_nombre": "Juan",
            "segundo_nombre": "Pablo",
            "primer_apellido": "Carini",
        }
    }

    def test_datos_encontrados(self):
        resultado = buscar_datos("Miguel", "Julian", database=self.database)
        self.assertEqual(resultado, ["Miguel", "Julian"])

    def test_datos_no_encontrados(self):
        resultado = buscar_datos("Dominguez", "Pedro", database=self.database)
        self.assertEqual(resultado, [])

    def test_datos_mezclados(self):
        resultado = buscar_datos("Carini", "Alvarez", "Julian", "Fernandez", database=self.database)
        self.assertEqual(resultado, ["Carini", "Alvarez", "Julian"])

unittest.main()