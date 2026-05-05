# Proyecto-Vehiculos
## 📋 Requisitos Previos

Asegúrate de tener instalado lo siguiente en tu sistema antes de comenzar:
* [Python 3.14+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/)


## 🛠️ Instalación y Configuración Local

Sigue estos pasos para levantar el entorno de desarrollo en tu máquina local.

### 1. Clonar el repositorio
```bash
git clone https://github.com/AlexitoMedina/Proyecto-_Vehiculos.git
cd Proyecto-_Vehiculos
```
### 2. Crear y activar el entorno virtual
- Linux
```bash
python3.x -m venv venv
source venv/bin/activate
```
- Windows
```bash
python -m venv venv
venv\Scripts\activate
```
### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```
### 4. Copiar las variables de entorno
```bash
cp .env.example .env
```
### 5. Ejecutar el servidor 
```bash
fastapi dev
```
