### 1. Clases Abstractas (ABC)

Las clases abstractas establecen contratos de diseño estrictos. Operan como interfaces que previenen la instanciación de entidades incompletas. Fijan la obligación en las subclases de proveer una implementación concreta para los métodos marcados con `@abstractmethod`. La instanciación directa de la clase base lanza un `TypeError`.

```python
from abc import ABC, abstractmethod

class SistemaArma(ABC):
    def __init__(self, identificador: str):
        self.identificador = identificador

    @abstractmethod
    def ejecutar_ataque(self) -> str:
        pass

class ArmaFuego(SistemaArma):
    def ejecutar_ataque(self) -> str:
        return f"Disparo procesado para {self.identificador}"
```

### 2. Herencia Avanzada

Estructuración del código basada en jerarquías de especialización ("es-un"). La función `super()` inicializa el estado de las superclases sin acoplamiento rígido de nombres.

* **Herencia Simple:** Relación lineal para especializar una clase base.
* **Herencia Jerárquica:** Superclase base distribuye su núcleo lógico a múltiples ramas paralelas.
* **Herencia Multinivel:** Cadenas de derivación donde una clase hereda de una subclase.

```python
class Entidad: 
    def __init__(self, nombre: str):
        self.nombre = nombre

class Personaje(Entidad): 
    def __init__(self, nombre: str, tipo: str):
        super().__init__(nombre) 
        self.tipo = tipo

class Profesor(Personaje): 
    def __init__(self, nombre: str):
        super().__init__(nombre, "Profesor")
```

### 3. Multiherencia y MRO

Composición de clases a partir de múltiples bases ortogonales. Las colisiones de métodos o atributos se resuelven mediante *C3 Superclass Linearization*. El Method Resolution Order (MRO) define la prioridad de búsqueda: de abajo hacia arriba y de izquierda a derecha.

```python
class Desplazable:
    def operar(self):
        return "Moviendo entidad"

class Interrogable:
    def operar(self):
        return "Respondiendo preguntas"

class Jugador(Desplazable, Interrogable):
    pass

instancia = Jugador()
print(instancia.operar()) # Retorna "Moviendo entidad"
```

### 4. Polimorfismo

Eliminación de lógica condicional basada en tipos. El intérprete evalúa la naturaleza del objeto en memoria durante la ejecución para invocar la variante del método correspondiente a la subclase instanciada.

```python
class Oficina:
    def limite_interrogatorio(self) -> int: 
        return 3

class Patio:
    def limite_interrogatorio(self) -> int: 
        return 1

def ejecutar_ronda(habitacion):
    return habitacion.limite_interrogatorio()

espacios = [Oficina(), Patio(), Oficina()]
limites = [ejecutar_ronda(e) for e in espacios] # [3, 1, 3]
```

### 5. Properties (Encapsulamiento)

Mutación de métodos físicos en atributos sintácticos virtuales. Aísla la representación interna respecto a la interfaz pública. El `@setter` intercepta asignaciones directas e inyecta lógica de control y validación antes de alterar la variable subyacente.

```python
class Historial:
    def __init__(self):
        self._limite = 5
        self._entradas = [] 

    @property
    def entradas(self) -> list:
        return self._entradas

    @entradas.setter
    def entradas(self, nueva_entrada: str):
        if not isinstance(nueva_entrada, str):
            raise TypeError("La entrada debe ser texto")
        if len(self._entradas) >= self._limite:
            self._entradas.pop(0) 
        self._entradas.append(nueva_entrada)
```

### 6. Decoradores de Funciones

Patrón estructural basado en closures. Una función contenedora altera la ejecución de una función objetivo. La implementación de `*args` y `**kwargs` en la función interna garantiza la aplicación del decorador sobre métodos con parámetros variables.

```python
def forzar_mayusculas(funcion_base):
    def wrapper(*args, **kwargs):
        resultado = funcion_base(*args, **kwargs)
        if isinstance(resultado, str):
            return resultado.upper()
        return resultado
    return wrapper

@forzar_mayusculas
def obtener_nombre(sospechoso: str) -> str:
    return sospechoso
```

### 7. Estructuras de Datos Compuestas

Diseño de contenedores orientado a eficiencia algorítmica. 

* **Dict + Set:** Búsqueda, inserción y eliminación en complejidad O(1). El diccionario mapea claves hacia conjuntos. El conjunto bloquea algorítmicamente la inserción de duplicados.
* **Deque (`collections.deque`):** Lista doblemente enlazada. Garantiza inserción y extracción en O(1) en ambos extremos, a diferencia de las listas estándar (O(N) en el índice 0).

```python
from collections import deque

matriz_descartes = {
    "armas": set(),
    "habitaciones": set()
}
matriz_descartes["armas"].add("Pistola")
matriz_descartes["armas"].add("Pistola") # Duplicado ignorado automáticamente

historial_paginado = deque(maxlen=3) 
historial_paginado.append("T1")
historial_paginado.append("T2")
historial_paginado.append("T3")
historial_paginado.append("T4") # Expulsa "T1" instantáneamente (O(1))
```