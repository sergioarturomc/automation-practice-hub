# Test Automation Practice Hub

Proyecto de práctica de **QA Automation** desarrollado con **Python, Selenium WebDriver y Pytest**, utilizando **Test Automation Practice** como entorno de pruebas.

**Página utilizada:** https://testautomationpractice.blogspot.com/

## 🎯 Objetivo

El objetivo fue **explorar y practicar cómo se pueden estructurar diferentes tipos de pruebas automatizadas**, entendiendo cómo debería verse y organizarse un proyecto de automatización en un entorno real.

Busqué experimentar con diferentes elementos, interacciones y escenarios de una aplicación web para conocer mejor las posibilidades de **Selenium, Pytest y Page Object Model (POM)**.

## 🛠️ Tecnologías

* Python
* Selenium WebDriver
* Pytest
* Page Object Model (POM)
* HTML Reports
* Screenshots

## 🔍 Pruebas automatizadas

Se practicaron diferentes interacciones y elementos web, incluyendo:

* Formularios y campos de entrada
* Radio buttons y checkboxes
* Dropdowns
* Tablas
* Alertas y ventanas
* Mouse hover y doble clic
* Drag & Drop
* Sliders
* Upload de archivos

## 📂 Estructura

```text
pages/          → Page Objects
test/           → Pruebas automatizadas
reports/        → Reportes HTML
screenshots/    → Evidencias
utils/          → Utilidades
data.py         → Datos de prueba
pytest.ini      → Configuración
requirements.txt
```

## ▶️ Ejecución

```bash
pip install -r requirements.txt
pytest
```

Para generar el reporte:

```bash
pytest --html=reports/reporte.html
```

## 🤖 Uso de AI

Durante el desarrollo utilicé **AI como herramienta de apoyo al aprendizaje**, principalmente para aclarar conceptos, entender errores y revisar algunas soluciones cuando encontraba dificultades. La implementación, ejecución y validación de las pruebas fueron realizadas como parte de mi práctica.

## 📌 Aprendizaje

Este proyecto me permitió familiarizarme más con la **automatización de pruebas UI**, la organización de un proyecto mediante **Page Object Model**, el uso de **Pytest** y la generación de reportes y evidencias.
