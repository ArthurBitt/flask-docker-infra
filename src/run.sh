#!/bin/bash

echo "=== Instalando Flask ==="
pip install flask

echo "=== Instalando Redis ==="
pip install redis


echo "=== Iniciando servidor Flask ==="
python3 app.py

echo "=== Servidor finalizado ==="
bash 