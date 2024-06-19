# TT_sprint5

### Tema: Visualización de Datos de Vehículos - Proyecto Final del Sprint 5
Este proyecto utiliza `Streamlit` y `Plotly Express` para crear una aplicación web interactiva que permite a los usuarios visualizar datos de anuncios de venta de coches en los Estados Unidos. Los usuarios pueden generar un histograma del odómetro y un gráfico de dispersión del precio del coche en función del año del modelo y la condición del coche.

### Características
- **Histograma Interactivo**: Permite a los usuarios crear un histograma del odómetro de los coches.
- **Gráfico de Dispersión Interactivo**: Permite a los usuarios crear un gráfico de dispersión del precio del coche en función del año del modelo y la condición del coche.

### Requisitos
- Python 
- Pandas
- Plotly
- Streamlit
- Nbformat

### Uso
1. Ejecuta la aplicación Streamlit: bash - streamlit run app.py
2. Abre tu navegador web y navega a `http://localhost:8501` para ver la aplicación.

### Estructura del Proyecto
```plaintext
└── notebooks             # Carpeta que contiene my EDA.ipynb
    └── EDA.ipynb
└── .streamlit            # Carpeta que contiene la configuracion para correr el proyecto en Render
    └── config.toml
├── git.ignore            # Archivo que incluye elementos para ignorar
├──  README.md            # Este archivo README
├── app.py                # Archivo principal de la aplicación Streamlit
├── requirements.txt      # Lista de dependencias del proyecto
├── vehicles_us.csv       # Conjunto de datos de anuncios de venta de coches