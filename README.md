# Consulta de Tiempos de Llegada Autobuses EMT Madrid

![Language](https://img.shields.io/badge/language-Python-blue)  
![Status](https://img.shields.io/badge/status-inprogress-green)  

Este es un proyecto en **Flask** que permite consultar los tiempos estimados de llegada de los autobuses de la **EMT Madrid** en una parada específica y para una línea determinada.

## 📌 Características
- Consulta en tiempo real de tiempos de llegada de autobuses.
- Integración con la API pública de **EMT Madrid**.
- Interfaz simple basada en **HTML y Flask**.

## 🛠️ Instalación
### 1️⃣ Clonar el repositorio
```bash
  git clone https://github.com/tuusuario/API_EMT_Mad.git
  cd API_EMT_Mad
```
### 2️⃣ Crear y activar un entorno virtual (opcional pero recomendado)
```bash
  python -m venv venv
  source venv/bin/activate  # En macOS y Linux
  venv\Scripts\activate     # En Windows
```
### 3️⃣ Instalar dependencias
```bash
  pip install -r requirements.txt
```
### 4️⃣ Configurar variables de entorno
Crear un archivo `.env` en la raíz del proyecto y agregar la clave de acceso a la API de EMT Madrid:
```
ACCESS_TOKEN=TU_CLAVE_DE_EMT
```

## 🚀 Uso
1️⃣ Ejecutar la aplicación:
```bash
  python app.py
```
2️⃣ Acceder a la interfaz web en el navegador:
```
  http://127.0.0.1:5000/
```
3️⃣ Ingresar el número de parada y la línea de autobús para consultar los tiempos de llegada.

## 🏗️ Estructura del Proyecto
```
/
├── templates/
│   ├── index.html
├── .env
├── app.py
├── requirements.txt
└── README.md
```

## 🤝 Contribución
¡Las contribuciones son bienvenidas! Para contribuir, sigue estos pasos:
1. Haz un **fork** del proyecto.
2. Crea una nueva **rama** (`feature-nueva-funcionalidad`).
3. Realiza tus cambios y haz un **commit** (`git commit -m "Añadida nueva funcionalidad"`).
4. Haz un **push** a tu rama (`git push origin feature-nueva-funcionalidad`).
5. Abre un **Pull Request**.

## 📄 Licencia
Este proyecto está bajo la licencia **MIT**.
