# Diapositivas P04 — Aves migratorias: el árbol de humedales que las une sin rodeos

Grupo 4 — Exposición: viernes 4 de diciembre de 2026, 7:30 p.m.

---

## Diapositiva 1: Titulo
**Aves migratorias: el árbol de humedales que las une sin rodeos**
Grupo 4 — Exposición: viernes 4 de diciembre de 2026, 7:30 p.m.

---

## Diapositiva 2: Integrantes
- Navarro Barboza Max Alejandro
- Picado Godínez Fiorella Ximena
- Vaca Rojas Leonel Andrés

Todas las personas hablan: dividir el discurso entre los 3 integrantes.

---

## Diapositiva 3: Plataforma y entrega
- Plataforma oficial UISIL: escrito + diapositivas (escrito ≤10 páginas, APA 7, ≥5 fuentes; presentación ≤10 diapositivas).
- Repositorio del curso: `github.com/Franciscocamposk/PROYECTOS_MATEMATICA_DISCRETA_USIL_2026` — hacer fork, poner todo en `VIERNES/Grupo 4/` (main.py, Excel, README.md, requirements.txt, pruebas) y enviar pull request.
- Dato del Excel: 1637 registros (datos simulados didácticos, no oficiales).

---

## Diapositiva 4: El modelo
1. Grafo de humedales: tramos activos (hoja `Vuelos`, `activo == "si"`).
2. Árbol generador: Kruskal (BFS vale según el enunciado).
3. PNG: red completa en gris + árbol generador en verde grueso, con los km en las aristas.
4. Decisión que imprime el programa: qué tramos bastan y cuántos km se ahorran.

---

## Diapositiva 5: Datos del grafo
- 8 humedales: PaloVerde, CanoNegro, Tortuguero, Carara (parques); Tarcoles, Ostional, Golfo, Nicoya (estuarios).
- Tramos activos únicos: 28. Ciclos en la red: 21.

---

## Diapositiva 6: Árbol generador (Kruskal)
- 7 tramos, 249 km en total.
- Arma el árbol mínimo conexo; sin ciclos.

---

## Diapositiva 7: Validación — los 4 parques
Los 4 humedales (PaloVerde, CanoNegro, Carara, Tortuguero) quedan unidos por un árbol con 3 tramos y 0 ciclos:
- CanoNegro – PaloVerde: 42 km
- CanoNegro – Carara: 50 km
- CanoNegro – Tortuguero: 72 km

---

## Diapositiva 8: Decisión del cliente
> Cubrir los 8 humedales con el árbol de 7 tramos de 249 km (la red completa tiene 28 tramos).

---

## Diapositiva 9: Cómo ejecutar
1. Instalar: `pip install -r requirements.txt`
2. Ejecutar en la carpeta del proyecto: `python main.py`
3. Verificar: `python pruebas/test_arbol.py` (4 pruebas, todas pasan).
4. Resultado: `aves_arbol.png` + decisión impresa (el programa debe ejecutarse en vivo en la exposición).

---

## Diapositiva 10: Notas para la exposición
- Ejecutar `python main.py` en vivo; sin el PNG vale cero. No se aceptan capturas en lugar de la ejecución.
- Escrito: APA 7, ≤10 páginas, ≥5 fuentes; presentación: ≤10 diapositivas.
- Si el programa falla, detenerse y ejecutar de nuevo antes de seguir.
- Material entregable: main.py, requirements.txt, README.md, pruebas/, aves_arbol.png, Escrito_P04_Aves_humedales.pdf y P04_Aves_humedales.xlsx.
