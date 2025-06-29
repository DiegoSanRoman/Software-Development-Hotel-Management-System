# UC3MTravel - Hotel Management System

**Proyecto para la asignatura de _Desarrollo de Software_ (2º curso del Grado en Ingeniería Informática, UC3M).**

Este repositorio recoge la implementación de un pequeño sistema de gestión hotelera desarrollado durante el curso. El objetivo principal ha sido aplicar prácticas de programación y testing en Python.

## Equipo
- **Diego San Román Posada**  
- **Bárbara Sánchez Moratalla**  
- **Izan Sánchez Álvaro**  

## Descripción
El proyecto está compuesto por tres funcionalidades principales:
1. **Reserva de habitación** – valida la información de la reserva y almacena los datos en `Reservations.json`.
2. **Registro de llegada** – comprueba que el huésped es el esperado y genera una llave de habitación almacenada en `Stay.json`.
3. **Checkout del huésped** – verifica la llave, comprueba la fecha de salida y registra la información en `checkOut.json`.

Todos los datos se almacenan en ficheros JSON localizados en `src/JSONfiles/JsonForFunctions`.

## Requisitos de instalación
1. Tener instalado Python 3.10 o superior.
2. Instalar las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt
   ```

## Cómo utilizar el proyecto
1. **Reservar habitación**: desde Python se puede instanciar `hotelManager` y llamar al método `roomReservation`:
   ```python
   from UC3MTravel.HotelManager import hotelManager

   manager = hotelManager()
   localizer = manager.roomReservation(5555555555554444,
                                      "Nombre Apellido",
                                      100,
                                      123456789,
                                      "single",
                                      "2024-01-01",
                                      1)
   print(localizer)
   ```
2. **Registrar llegada**: cargar un JSON con `Localizer` e `IdCard` y usar `guestArrival(path)`.
3. **Checkout**: llamar a `guestCheckout(key)` con la clave generada durante la llegada.

Existe un pequeño script `src/main/python/Main.py` para realizar pruebas manuales.

## Estructura del proyecto
```
├── src
│   ├── JSONfiles
│   │   ├── JsonForFunctions      # Ficheros de trabajo (Reservations, Stay…)
│   │   └── JsonForTests          # Casos JSON utilizados en los tests
│   ├── main
│   │   └── python
│   │       ├── Main.py
│   │       └── UC3MTravel        # Paquete con las clases de la aplicación
│   └── unittest
│       └── python                # Conjunto de pruebas unitarias
└── docs                          # Documentación y reportes
```

## Ejecutar las pruebas
Las pruebas automáticas se encuentran en `src/unittest/python`. Para ejecutarlas:
```bash
python -m unittest discover -s src/unittest/python -p "test_*.py"
```
Se utilizan `freezegun` y `unittest` para comprobar el correcto funcionamiento de cada funcionalidad.

---
¡Disfruta utilizando **UC3MTravel** y no dudes en revisar el código para más detalles!
