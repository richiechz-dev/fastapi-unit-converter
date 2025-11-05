from fastapi import FastAPI, Query
from pydantic import BaseModel, Field


# Nos aseguramos que las salidad siempre sean de tipo float
class ConvertionResult(BaseModel):
    value_fahrenheit: float = Field(..., description="Temperatura en grados fahrenheit")
    value_celsius: float = Field(..., description="Temperatura en grados celsius")


app = FastAPI(title="API_fahrenheit_to_celsius")


# Seguimos el Path, operation, function
@app.get("/")
async def root():
    return {"Hola mundo"}


@app.get("/convertir/temperatura")
async def convert_fahrenheit_to_celsius(
    fahrenheit: float = Query(
        ..., description="Valor de temperatura Fahrenheit a convertir"
    ),
):
    """
    Convierte un valor de temperatura de Celsius a Fahrenheit.
    Fórmula: F = (C * 9/5) + 32
    """
    celsius = (fahrenheit - 32) * 5 / 9

    return ConvertionResult(value_celsius=celsius, value_fahrenheit=fahrenheit)
