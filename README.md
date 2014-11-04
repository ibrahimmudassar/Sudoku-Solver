#Sudoku Solver

A simple python implementation of recursive backtracking algorithm to solve Sudoku puzzle. 
The program runs in less than a second to solve the puzzle. Tested with easy, difficult and all empty puzzle.

![Alt text](https://github.com/ipower2/Sudoku-Solver/blob/master/data/input_out.png "Sample solution")

###Dependencies:
- None: 
 - Sodukusolver and xumpy modules are sufficient to run this program.
- (Optional) Matplotlib: 
 - Matplotlib is required to graphically display the solution (shown above). Without matplotlib, the program will only generate textual output.
- (Optional) Setuptools:
 - Setuptools is recommended to run setup.py. Without setuptools, setup.py will still run by using distutils package, but does not support install_requires.
 
###Usage:
- Input: 
  - The program accepts Soduku puzzle in a .csv file. Each line should have 9 numbers separated by comma. The file should contain 9 lines.
- Execution:
  - (Optional) Execute: 'python setup.py install'. It will try to install dependencies (matplotlib).
  - Solving: Run 'python sudokusolver.py </path/to/input/file.csv>'
- Output: 
  - Solution is printed to the console
  - Solution is written to </path/to/input/file>_out.csv file
  - If matplotlib is available, screenshot of figure is saved to </path/to/input/file>_out.png file

###Other Info:
- Test: 
 - Unit tests are in tests package
- xumpy module is used to eliminate dependency on numpy
 
