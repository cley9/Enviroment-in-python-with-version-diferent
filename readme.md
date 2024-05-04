## Estructura del proyecto in python
```py
Proyecto/
│
├── Entorno Version/             # Directorio del entorno virtual
│   ├── Test py/                 # Contiene los Scripts del entorno virtual
│   │   ├── Scripts/             # Scripts del entorno virtual
│   │   └── ...
│
├── src/                         # Código fuente de tu aplicación
│   ├── __init__.py               # script main for that ejecute todo los py
│   ├── modulo1.py                # Tu script de Python
│   ├── modulo2.py
│   └── ...
│
├── tests/                       # Pruebas unitarias
│   ├── __init__.py
│   ├── test_modulo1.py
│   └── ...
│
├── docs/                        # Documentación
│
├── requirements.txt             # Dependencias del proyecto
│
└── README.md                    # Información general del proyecto
```

## Requisitos:
Note: This project is in python 3.8
- Instala python en windows 11 la version a usar
- Crear el entorno virtual with the version of python `py -3.8-32 -m venv venv`
- Active el entorno `.\venv\Scripts\activate`
- Instale las dependencias of file requirements.txt `pip install -r “requirements.txt”`
- Ejecute el archivo python `py .\src\traductor.py`
- Escriba algo en la terminal
