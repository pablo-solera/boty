# ⏱️ TimerTask Auto Time Logger

Automatiza el registro de horas en **TimerTask**.

Este script inicia sesión automáticamente con tus credenciales y registra **8 horas de trabajo en el día actual**.  
Pensado para ahorrar tiempo y evitar olvidos en el reporte diario.

---

## ✨ Qué hace

- Abre TimerTask
- Realiza el login
- Navega hasta el día actual
- Introduce 8 horas
- Guarda el parte

---

## 🚀 Instalación

### 1. Clonar el repositorio
```bash
git clone <repo>
cd <repo>
```

### 2. Crear entorno virtual
```bash
python -m venv venv
```

### 3. Activar
```bash
source .venv/bin/activate
```

### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 5. Instalar navegadores de Playwright
```bash
playwright install
```

## 🔐 Credenciales
Crea un archivo `.env` en la raiz del proyecto a partir de `.env.example` y rellenalo con tus datos.

## ▶️ Uso
```bash
python main.py
```