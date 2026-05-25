"""
matrix_rain.py — Efeito Matrix em Python puro (terminal)
Execute:  python matrix_rain.py
Sair:     pressione  q  ou  Ctrl+C
"""

import curses
import random
import time

CHARS = (
    "01アイウエオカキクケコサシスセソタチツテト"
    "ナニヌネノハヒフヘホABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789∑∆≈∞⌀"
)


def init_colors():
    """Configura pares de cores disponíveis no terminal."""
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN,  -1)   # verde normal
    curses.init_pair(2, curses.COLOR_WHITE,  -1)   # branco (caractere líder)
    curses.init_pair(3, 2,                   -1)   # verde escuro (rastro)


def make_drops(cols, rows):
    """Cria as colunas de gotas com posições e velocidades aleatórias."""
    return [
        {
            "y":     random.uniform(0, rows),
            "speed": random.uniform(0.3, 1.2),
            "len":   random.randint(6, 20),
        }
        for _ in range(cols)
    ]


def draw_frame(stdscr, drops, rows, cols):
    """Desenha um frame completo da chuva Matrix."""
    stdscr.erase()

    for x, drop in enumerate(drops):
        head_y = int(drop["y"])

        for i in range(drop["len"]):
            y = head_y - i
            if y < 0 or y >= rows:
                continue

            char = random.choice(CHARS)

            if i == 0:
                # Caractere líder: branco e brilhante
                attr = curses.color_pair(2) | curses.A_BOLD
            elif i < 3:
                # Topo do rastro: verde brilhante
                attr = curses.color_pair(1) | curses.A_BOLD
            elif i < drop["len"] // 2:
                # Meio do rastro: verde normal
                attr = curses.color_pair(1)
            else:
                # Fim do rastro: verde escuro/dim
                attr = curses.color_pair(3) | curses.A_DIM

            try:
                stdscr.addstr(y, x, char, attr)
            except curses.error:
                pass  # ignora bordas do terminal

        # Avança a gota
        drop["y"] += drop["speed"]

        # Reinicia quando sair da tela
        if drop["y"] - drop["len"] > rows:
            drop["y"]   = random.uniform(-drop["len"], 0)
            drop["speed"] = random.uniform(0.3, 1.2)
            drop["len"]  = random.randint(6, 20)

    stdscr.refresh()


def main(stdscr):
    curses.curs_set(0)          # esconde o cursor
    stdscr.nodelay(True)        # não bloqueia em getch()
    stdscr.timeout(50)          # refresh a cada ~50ms

    init_colors()

    rows, cols = stdscr.getmaxyx()
    drops = make_drops(cols, rows)

    while True:
        # Verifica redimensionamento
        new_rows, new_cols = stdscr.getmaxyx()
        if new_rows != rows or new_cols != cols:
            rows, cols = new_rows, new_cols
            drops = make_drops(cols, rows)

        draw_frame(stdscr, drops, rows, cols)

        key = stdscr.getch()
        if key in (ord("q"), ord("Q"), 27):  # q ou ESC para sair
            break

        time.sleep(0.04)


if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass
    print("\nMatrix desativada. Até logo.")
