# Game Of Life

"The Game of Life," originally proposed by John Conway as a mathematical modeling expiriment, is a game played by four simple rules:

- Any living cell with 2 or fewer neighbors dies, as if that cell is underpopulated.
- Any living cell with more than 3 neighbors dies, as if that cell is overpopulated.
- Any dead cell with exactly three neighbors becomes alive, as if by repopulation.
- Any cell with exactly 2 or 3 neighbors remains alive at the next generation.

This program models that simulation in a console environment, using '-' to represent dead cells, and '|' to represent living ones.
It tracks iterations, as well as steps to stagnation.
