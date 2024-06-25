# TSP Solver using Genetic Algorithm

This repository contains a Python implementation of a Traveling Salesman Problem (TSP) solver using a Genetic Algorithm (GA). The TSP is a classic problem in the field of combinatorial optimization, where the goal is to find the shortest possible route that visits a set of given cities exactly once and returns to the original city.

## Overview

The TSP solver employs a Genetic Algorithm to iteratively evolve a population of candidate solutions towards an optimal or near-optimal solution. The GA operates by mimicking the process of natural selection, where individuals with higher fitness (i.e., shorter route distance) are more likely to survive and produce offspring.

## Files

- **genetic_algorithm.py**: Contains the implementation of the Genetic Algorithm, including functions for generating random populations, calculating fitness, performing crossover and mutation operations, and sorting populations based on fitness.
- **tsp.py**: Implements the main TSP solver using Pygame for visualization. It initializes the problem, creates the initial population, and iteratively evolves the population while visualizing the best solution found so far.
- **draw_functions.py**: Provides functions for drawing cities, paths, and plots using Pygame.

## Usage

To run the TSP solver, execute the `tsp.py` script using Python. The solver allows you to choose between different problem instances:

- Randomly generated cities
- Default predefined problems with 10, 12, or 15 cities
- `att48` benchmark dataset (uncomment relevant code in `tsp.py`)

You can customize parameters such as population size, number of generations, and mutation probability directly in the `tsp.py` script.

## Dependencies

- Python 3.x
- Pygame (for visualization)

Ensure Pygame is installed before running the solver. You can install Pygame using pip:

```bash
pip install pygame
```

## Acknowledgments

This TSP solver was developed as a learning project and draws inspiration from various online resources and academic materials on Genetic Algorithms and the Traveling Salesman Problem. Special thanks to the authors of those resources for sharing their knowledge.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to contribute to this repository by providing enhancements, bug fixes, or additional features. If you encounter any issues or have suggestions for improvements, please open an issue on the repository. Happy solving!