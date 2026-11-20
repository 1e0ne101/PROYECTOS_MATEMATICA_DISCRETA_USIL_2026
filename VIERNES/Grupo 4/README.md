# P04 - Aves migratorias: el arbol de humedales que las une sin rodeos

- Grupo 4 - Viernes - Exposición: 4 de diciembre de 2026, 7:30 p.m.
- Integrantes: Navarro Barboza Max Alejandro, Picado Godínez Fiorella Ximena, Vaca Rojas Leonel Andrés
- Plataforma oficial: UISIL (escrito + diapositivas). Repositorio del curso: github.com/Franciscocamposk/PROYECTOS_MATEMATICA_DISCRETA_USIL_2026

## Datos

`P04_Aves_humedales.xlsx` (1637 registros): hoja `Humedales` (8 humedales) y hoja `Vuelos`
(origen, destino, km, activo). Datos simulados didácticos.

## Modelo

Grafo de humedales con los tramos activos, arbol generador con Kruskal y decisión para
el cliente (ver `main.py`).

## Ejecutar

```
python main.py
```

Genera `aves_arbol.png` (red completa en gris, árbol generador en verde, km en las
aristas) e imprime la decisión. Pruebas básicas: `python pruebas/test_arbol.py`.
