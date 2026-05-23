class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None  

# 1. Lista Simple
class ListaSimple:
    def __init__(self):
        self.cabeza = None
    
    def insertar(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
    
    def eliminar(self, dato):
        actual = self.cabeza
        previo = None
        while actual and actual.dato != dato:
            previo = actual
            actual = actual.siguiente
        if actual:
            if previo:
                previo.siguiente = actual.siguiente
            else:
                self.cabeza = actual.siguiente
            return True
        return False
    
    def mostrar(self):
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " -> ".join(elementos) if elementos else "Vacía"

# 2. Lista Ordenada
class ListaOrdenada:
    def __init__(self):
        self.cabeza = None
    
    def insertar(self, dato):
        nuevo = Nodo(dato)
        if not self.cabeza or dato < self.cabeza.dato:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente and actual.siguiente.dato < dato:
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
    
    def eliminar(self, dato):
        actual = self.cabeza
        previo = None
        while actual and actual.dato != dato:
            previo = actual
            actual = actual.siguiente
        if actual:
            if previo:
                previo.siguiente = actual.siguiente
            else:
                self.cabeza = actual.siguiente
            return True
        return False
    
    def mostrar(self):
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " -> ".join(elementos) if elementos else "Vacía"

# 3. Pila (LIFO)
class Pila:
    def __init__(self):
        self.tope = None
    
    def push(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo
    
    def pop(self):
        if self.tope:
            dato = self.tope.dato
            self.tope = self.tope.siguiente
            return dato
        return None
    
    def mostrar(self):
        actual = self.tope
        elementos = []
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " | ".join(elementos) if elementos else "Vacía"

# 4. Cola (FIFO)
class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
    
    def encolar(self, dato):
        nuevo = Nodo(dato)
        if not self.final:
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo
    
    def desencolar(self):
        if self.frente:
            dato = self.frente.dato
            self.frente = self.frente.siguiente
            if not self.frente:
                self.final = None
            return dato
        return None
    
    def mostrar(self):
        actual = self.frente
        elementos = []
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " <- ".join(elementos) if elementos else "Vacía"

# 5. Lista Doblemente Enlazada (LDE)
class LDE:
    def __init__(self):
        self.cabeza = None
    
    def insertar(self, dato):
        nuevo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
    
    def eliminar(self, dato):
        actual = self.cabeza
        while actual and actual.dato != dato:
            actual = actual.siguiente
        if actual:
            if actual.anterior:
                actual.anterior.siguiente = actual.siguiente
            else:
                self.cabeza = actual.siguiente
            if actual.siguiente:
                actual.siguiente.anterior = actual.anterior
            return True
        return False
    
    def mostrar(self):
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " <-> ".join(elementos) if elementos else "Vacía"

# 6. Lista Circular (Simple)
class ListaCircular:
    def __init__(self):
        self.cabeza = None
    
    def insertar(self, dato):
        nuevo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo
            nuevo.siguiente = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.siguiente = self.cabeza
    
    def eliminar(self, dato):
        if not self.cabeza:
            return False
        actual = self.cabeza
        previo = None
        while True:
            if actual.dato == dato:
                if previo:
                    previo.siguiente = actual.siguiente
                else:
                    # Eliminar cabeza
                    if actual.siguiente == self.cabeza:
                        self.cabeza = None
                    else:
                        temp = self.cabeza
                        while temp.siguiente != self.cabeza:
                            temp = temp.siguiente
                        temp.siguiente = actual.siguiente
                        self.cabeza = actual.siguiente
                return True
            previo = actual
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        return False
    
    def mostrar(self):
        if not self.cabeza:
            return "Vacía"
        elementos = []
        actual = self.cabeza
        while True:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        return " -> ".join(elementos) + " -> (vuelve a cabeza)"

# MENÚ PRINCIPAL
def menu():
    listas = {
        '1': ("Lista Simple", ListaSimple()),
        '2': ("Lista Ordenada", ListaOrdenada()),
        '3': ("Pila", Pila()),
        '4': ("Cola", Cola()),
        '5': ("LDE", LDE()),
        '6': ("Lista Circular", ListaCircular())
    }
    
    while True:
        print("\n" + "="*50)
        print("MENÚ PRINCIPAL - LISTAS ENLAZADAS")
        print("="*50)
        for key, (nombre, _) in listas.items():
            print(f"{key}. {nombre}")
        print("0. Salir")
        
        opcion = input("Seleccione tipo de lista: ")
        if opcion == '0':
            print("¡Hasta luego!")
            break
        elif opcion in listas:
            nombre, lista = listas[opcion]
            submenu(nombre, lista)
        else:
            print("Opción inválida")

def submenu(nombre, lista):
    while True:
        print(f"\n--- {nombre} ---")
        print("1. Insertar elemento")
        print("2. Eliminar elemento")
        print("3. Mostrar lista")
        print("4. Volver al menú principal")
        
        if nombre == "Pila":
            print("5. Pop (extraer)")
        elif nombre == "Cola":
            print("5. Desencolar")
        
        op = input("Opción: ")
        
        if op == '1':
            dato = input("Valor a insertar: ")
            if nombre == "Pila":
                lista.push(dato)
            elif nombre == "Cola":
                lista.encolar(dato)
            else:
                lista.insertar(dato)
            print(f"{dato} insertado.")
        
        elif op == '2':
            dato = input("Valor a eliminar: ")
            if nombre == "Pila":
                print("Para pila use 'Pop' (opción 5)")
            elif nombre == "Cola":
                print("Para cola use 'Desencolar' (opción 5)")
            else:
                if lista.eliminar(dato):
                    print(f"{dato} eliminado.")
                else:
                    print(f"{dato} no encontrado.")
        
        elif op == '3':
            print("Contenido:", lista.mostrar())
        
        elif op == '4':
            break
        
        elif op == '5' and nombre == "Pila":
            dato = lista.pop()
            if dato:
                print(f"Pop: {dato}")
            else:
                print("Pila vacía")
        
        elif op == '5' and nombre == "Cola":
            dato = lista.desencolar()
            if dato:
                print(f"Desencolado: {dato}")
            else:
                print("Cola vacía")
        
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()