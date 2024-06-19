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

### Instalación
1. Clona este repositorio:
2. Navega al directorio del proyecto:
3. Crea un entorno virtual (opcional, pero recomendado):
4. Instala las dependencias:

### Uso
1. Asegúrate de que tienes el archivo `vehicles_us.csv` en el directorio correcto. 
2. Ejecuta la aplicación Streamlit: bash - streamlit run app.py
3. Abre tu navegador web y navega a `http://localhost:8501` para ver la aplicación.

### Estructura del Proyecto
```plaintext
├── app.py                # Archivo principal de la aplicación Streamlit
├── vehicles_us.csv       # Conjunto de datos de anuncios de venta de coches
├── requirements.txt      # Lista de dependencias del proyecto
└── README.md             # Este archivo README
