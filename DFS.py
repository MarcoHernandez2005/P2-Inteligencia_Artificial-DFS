import time

def medir_tiempo(func):
    """Calcula el tiempo de ejecución para justificar la complejidad."""
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"\nTiempo de ejecución: {fin - inicio:.8f} segundos")
        return resultado
    return wrapper

def _dfs_recursivo(grafo, nodo, visitados=None, recorrido=None):
    """Ejecuta el DFS usando recursividad (actúa como pila LIFO)."""
    
    # 1. Primera pasada: preparamos el set (para no ciclar) y la lista (output)
    if visitados is None:
        visitados = set()
        recorrido = []

    # 2. Registramos el nodo actual como visitado
    visitados.add(nodo)
    recorrido.append(nodo)

    # 3. Revisamos los vecinos de este nodo
    for vecino in grafo.get(nodo, []):
        
        # 4. Si hay un vecino nuevo, entramos en él a fondo (recursión)
        if vecino not in visitados:
            _dfs_recursivo(grafo, vecino, visitados, recorrido)

    # 5. Sin vecinos nuevos, la función termina y retrocede (backtracking)
    return recorrido

@medir_tiempo
def dfs(grafo, inicio):
    """Función principal: Recibe el input y arranca el algoritmo."""
    return _dfs_recursivo(grafo, inicio)

# Modificacion de la entrada

if __name__ == "__main__":
    
    # 1. MODIFICA EL GRAFO: 
    # La clave (izquierda) es el nodo, y el valor (derecha) es la lista de sus vecinos.
    # en caso de lestras usa (ej. 'A': ['B', 'C']).
    grafo_examen = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [3]
    }
    
    # 2. MODIFICA EL NODO DE INICIO:
    # Cambia este valor por el nodo desde el cual se guste arrancar.
    nodo_inicio = 2
    
    print(f"\n--- Ejecución del Examen ---")
    print(f"Iniciando DFS desde el nodo: {nodo_inicio}")
    
    # Llamada a la función principal que ejecuta el algoritmo
    output = dfs(grafo_examen, nodo_inicio)
    
    # Este es el OUTPUT que se mostrará
    print(f"Output (Orden de exploración DFS): {output}")
