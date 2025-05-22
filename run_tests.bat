@echo off
echo Ejecutando pruebas basicas...
echo.
echo Prueba 1: Verificando si existe un archivo importante...
if exist index.html (
    echo index.html encontrado. Prueba PASADA.
    exit /b 0
) else (
    echo index.html NO encontrado. Prueba FALLIDA.
    exit /b 1
)