# API para prueba técnica

## Instalación

Todas las librerías utilizadas se encuentran en el archivo requirements.txt, para instalarlas se debe ejecutar el siguiente comando:

```
pip install -r requirements.txt
```

Además de lo anterior para que el proyecto pueda ser ejecutado se debe crear una base de datos en postgresql con el nombre de "repartes" y cambiar el usuario y password según corresponda en el archivo settings.py.

## Ejecución

Para que se pueda ver de manera más rápida el endpoint de optimización de rutas hice un comando personalizado que se puede ejecutar de la siguiente manera:

```
python manage.py seed
```

Esto generará 2 tiendas, 1 repartidor, 3 clientes, 5 cotizaciones con diferentes productos cada una.
Para ejecutar el servidor se debe ejecutar el siguiente comando:

```
python manage.py runserver
```

## Endpoints

En el siguiente apartado se muestran algunos de los endpoints que se pueden utilizar para probar la API. Para ver todos los endpoints se puede revisar el archivo urls.py.

### 1. Crear grocery

```
POST /api/groceries/
```

Ejemplo de body:

```
{
    "name": "Tienda 2",
    "api_url": "http://google.com/s",
    "lat": 1,
    "long": 6
}
```

### 2. Obtener todas las groceries

```
GET /api/groceries/
```

### 3. Crear shoppers

```
POST /api/shoppers/
```

Ejemplo de body:

```
{
  "name": "Shopper 1",
  "email": "shopper@shopper.cl",
  "capacity": 100
}
```

### 4. Obtener todos los shoppers

```
GET /api/shoppers/
```

### 5. Crear cotizaciones(quotes)

```
POST /api/quotes/
```

Ejemplo de body:

```
{
"client": 1,
"items": [
        {
        "product_id": "AXEWQ",
        "quantity": 10,
        "price": 100,
        "total_size": 28,
        "keyword": "mayonesa",
        "grocery": 1

        },
        {
            "product_id": "123",
            "quantity": 8,
            "price": 9,
            "total_size": 2,
            "keyword": "huevo",
            "grocery": 2

        }
    ]

}
```

### 6. Asignar cotizaciones

```
POST /api/quotes/assign
```

Ejemplo de body:

```
{
  "quote": 5,
  "shopper": 1
}
```

### 7. Optimizar rutas

```
GET /api/routes/?shopper=<id>
```

### Explicación para la optimización de rutas

Para optimizar las rutas lo primero que se hace es obtener todos los pedidos que tiene asignado un shopper y obtener la menor cantidad de grupos que no superen la capacidad. Este algoritmo se encuentra en el archivo route_optimization.py y se llama get_groups.
El enfoque utilizado para este algoritmo fue de two pointers, donde se tiene un puntero al principio y al final del arreglo ordenado de forma creciente. Así se van formando grupos de pedidos que no superen la capacidad del shopper.

- Se asumió que un shopper no puede asignarse un pedido que supere su capacidad.

Para la segunda parte del algoritmo se basa en como realizar el recorrido de los clientes y para esto se utilizó el algoritmo de Prim. Este algoritmo entrega el árbol de expansión mínima de un grafo, en este caso el grafo es el conjunto de clientes y el peso de las aristas es la distancia entre los clientes. Luego de esto se buscan los dos clientes en donde podría partir el recorrido, es decir, los clientes que tienen grado 1 en el árbol de expansión mínima. Luego se hace el recorrido de las tiendas utilizando el vecino más cercano y se retorna el recorrido de las tiendas y clientes.

- Se asume que el shopper primero hace el recorrido a las tiendas y luego a los clientes.

# Mejoras

- Realizar testeo de los endpoints y los algoritmos utilizando para la optimización de rutas.
- Mejorar el orden y calidad del código. Considero que hay partes en el código que se pueden mejorar y hacer más entendibles.
- Mejorar la optimización de rutas. Se puede utilizar otro algoritmo para la optimización de rutas y considerar más variables, dado que la heurística utilizada no es la mejor. (distancia euclideana)
- Merjorar el manejo del framework Django. Considero que hay partes del código que se pueden mejorar utilizando mejor el framework. (primer proyecto que realizo en Django)
