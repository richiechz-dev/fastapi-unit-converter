# API: Fahrenheit → Celsius

Pequeña API creada con FastAPI que convierte temperaturas de Fahrenheit a Celsius y devuelve ambos valores.

## Resumen
- Endpoint principal: `GET /convertir/temperatura?fahrenheit=<valor>`
- Respuesta JSON con:
  - `value_fahrenheit` (float)
  - `value_celsius` (float)

## Requisitos
- Python 3.10+ (ajusta según tu entorno). El proyecto usa `fastapi`.
- Recomendado: crear un entorno virtual y ejecutar mediante uv.
## Instalación rápida (usando "uv" package manager)

Este proyecto puede instalarse y ejecutarse usando un gestor de paquetes llamado `uv` que sincroniza dependencias desde `pyproject.toml` mediante `uv sync`. (Nota: aquí se asume que `uv` está instalado)

1. (Opcional) Crear y activar un entorno virtual:
   - Windows PowerShell:
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   - macOS / Linux:
     ```bash
     python -m venv .venv
     source .venv/bin/activate
     ```

2. Instalar/activar `uv` (sigue las instrucciones de `uv` si aplican):
   - (`uv` se instala se puede instalar con pip):
     ```bash
     pip install uv
     ```

3. Sincronizar e instalar dependencias desde `pyproject.toml`:
   ```bash
   uv sync
   ```
## Ejecuta la aplicación:
   ```bash
   uv run fastapi dev main
   ```
## Instalación rápida (Windows)
1. Crear y activar entorno virtual:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1   # PowerShell
   # o en cmd:
   .\.venv\Scripts\activate.bat
   ```

   