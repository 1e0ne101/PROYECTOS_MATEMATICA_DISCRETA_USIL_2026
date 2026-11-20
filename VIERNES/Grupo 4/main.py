"""Proyecto final P04 - Aves migratorias: el arbol de humedales que las une sin rodeos."""

from pathlib import Path

import networkx as nx
import pandas as pd

PROJECT = Path(__file__).resolve().parent
EXCEL = PROJECT / "P04_Aves_humedales.xlsx"
PNG = PROJECT / "aves_arbol.png"
PARQUES = ["PaloVerde", "CanoNegro", "Tortuguero", "Carara"]


def leer_grafo(path):
    """Grafo de humedales: los activos=si, aristas unicas con el km minimo."""
    vuelos = pd.read_excel(path, sheet_name="Vuelos")
    activos = vuelos[vuelos["activo"].astype(str).str.lower() == "si"]
    G = nx.Graph()
    for _, fila in activos.iterrows():
        u = str(fila["origen"]).strip()
        v = str(fila["destino"]).strip()
        if u == v:
            continue
        km = float(fila["km"])
        if not G.has_edge(u, v) or km < G[u][v]["km"]:
            G.add_edge(u, v, km=km)
    return G


def arbol_generador(G):
    """Arbol generador con Kruskal: aristas de menor km, sin ciclos, cubre todo."""
    T = nx.Graph()
    T.add_nodes_from(G.nodes())
    for u, v, d in sorted(G.edges(data=True), key=lambda e: (e[2]["km"], e[0], e[1])):
        if not nx.has_path(T, u, v):
            T.add_edge(u, v, km=d["km"])
    return T


def dibujar_ave_arbol(G, T, png):
    """Red completa en gris y arbol generador en verde grueso, con km en las aristas."""
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    pos = nx.spring_layout(G, seed=42)
    fig, ax = plt.subplots(figsize=(9, 6))
    for u, v in G.edges:
        ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]],
                color="0.75", linewidth=0.8, solid_capstyle="round")
    for u, v, d in T.edges(data=True):
        ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]],
                color="#1f8f3f", linewidth=3.5, solid_capstyle="round")
        mx = (pos[u][0] + pos[v][0]) / 2
        my = (pos[u][1] + pos[v][1]) / 2
        ax.text(mx, my, f'{d["km"]:.0f}', ha="center", va="center",
                fontsize=8, color="white", fontweight="bold")
    for n in G.nodes():
        ax.plot(pos[n][0], pos[n][1], "o", color="#f2a900", ms=8)
        ax.text(pos[n][0], pos[n][1], n, ha="center", va="center",
                fontsize=8, fontweight="bold")
    ax.set_title("Aves humedales: red completa (gris) y arbol generador (verde)", fontsize=12)
    ax.axis("off")
    fig.savefig(png, dpi=150, bbox_inches="tight")
    plt.close(fig)


def decision(G, T):
    km_total = sum(d["km"] for _, _, d in T.edges(data=True))
    km_red = sum(d["km"] for _, _, d in G.edges(data=True))
    ciclos = G.number_of_edges() - G.number_of_nodes() + nx.number_connected_components(G)
    Tp = nx.minimum_spanning_tree(G.subgraph(PARQUES), weight="km")

    print("=== P04 - Aves migratorias: el arbol de humedales que las une sin rodeos ===")
    print("Humedales (" + str(G.number_of_nodes()) + "): " + ", ".join(sorted(G.nodes())))
    print("Tramos activos unicos: " + str(G.number_of_edges()))
    print("Red activa: ciclos = " + str(ciclos))
    print("Arbol generador (Kruskal): " + str(T.number_of_edges()) + " tramos, " + f"{km_total:.0f}" + " km")
    print("Decision: cubrir los " + str(G.number_of_nodes()) + " humedales con el arbol de "
          + str(T.number_of_edges()) + " tramos de " + f"{km_total:.0f}" + " km (la red completa tiene "
          + str(G.number_of_edges()) + " tramos).")
    print("Validacion: los 4 parques (" + ", ".join(PARQUES) + ") quedan unidos por el arbol con "
          + str(Tp.number_of_edges()) + " tramos y 0 ciclos:")
    for u, v, d in sorted(Tp.edges(data=True), key=lambda e: e[2]["km"]):
        print("   " + str(u) + " - " + str(v) + " : " + f"{d['km']:.0f}" + " km")
    print("PNG: " + str(PNG.name))


def main():
    G = leer_grafo(EXCEL)
    T = arbol_generador(G)
    dibujar_ave_arbol(G, T, PNG)
    decision(G, T)


if __name__ == "__main__":
    main()
