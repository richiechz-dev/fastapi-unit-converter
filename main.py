from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel, Field


# Nos aseguramos que las salidad siempre sean de tipo float
# Base Model declara modelos o esquemas que validad y serializan automaticamente datos
# Field añade metadatos como description en este caso
class ConvertionResult(BaseModel):
    value_fahrenheit: float = Field(..., description="Temperatura en grados fahrenheit")
    value_celsius: float = Field(..., description="Temperatura en grados celsius")


app = FastAPI(title="API_fahrenheit_to_celsius")


# Seguimos el Path, operation, function
@app.get("/")
async def root():
    return {"Hola mundo"}


# Usamos Query para declarar un parametro de consulta
@app.get("/convertir/temperatura")
async def convert_fahrenheit_to_celsius(
    fahrenheit: float = Query(
        ..., description="Valor de temperatura en Fahrenheit para convertir en Celsius"
    ),
):
    """
    Convierte un valor de temperatura de Fahrenheit a Celsius
    Fórmular: C = F (F - 32) * 5 / 9
    Fórmula: F = (C * 9/5) + 32
    """

    celsius = (fahrenheit - 32) * 5 / 9

    return ConvertionResult(value_celsius=celsius, value_fahrenheit=fahrenheit)
