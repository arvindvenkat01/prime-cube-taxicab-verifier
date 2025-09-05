# A Diophantine Equation on Consecutive Prime Cubes: Computational Evidence for Exactly Two Solutions

**Author**: Arvind N. Venkat

This work has been archived and assigned a permanent identifier on Zenodo:
- DOI: `[to be created]`
- URL: `[to be created]`

## Abstract

We investigate the Diophantine equation `p1^3 + n^2 = p2^3 + p3^3` where `p1`, `p2`, `p3` are consecutive primes and `n` is a positive integer. Through exhaustive computational verification of all consecutive prime triples with `p3 <= 9,999,941,551`, we provide strong empirical evidence that this equation has exactly two integer solutions. The code in this repository was used to perform this large-scale verification, finding solutions `(2,3,5,12)` and `(3,5,7,21)`. These solutions exhibit the remarkable property that the ratios `n/p1` are consecutive integers (6 and 7), hinting at deeper underlying mathematical structure.

## Repository Contents

- `prime_cube_square_solutions.py`: The Python script containing the computational verification algorithm.
- `results.txt`: The full output of the verification run, showing the solutions found and the total computation time.


## Getting Started

To run the code and reproduce the results, you will need to have Python 3.8+ and the necessary libraries installed.

1. **Clone this repository:**
   ```
   git clone [https://github.com/arvindvenkat/prime-cube-taxicab-verifier.git](https://github.com/arvindvenkat/prime-cube-taxicab-verifier.git)
   ```
2. **Install required dependencies:**  
    The script requires `numpy`and `numba`.

    ```
    pip install numpy numba
    ```


3. **Run the verification script:**

    ```
    python prime-cube-taxicab-verifier.py
    ```



## Citation

If you use this work, please cite the paper using the Zenodo archive. Replace the placeholder DOI before publishing:

@misc{Venkat2025_GoldbachVerification,
author = {Arvind N. Venkat},
title = {A Structural Decomposition Framework for the Goldbach Conjecture: Algorithmic Optimization via Residue Class Analysis},
year = {2025},
publisher = {Zenodo},
doi = {10.5281/zenodo.17038291},
url = {https://doi.org/10.5281/zenodo.17038291}
}


---

## License

The content of this repository is dual-licensed:

- **MIT License** for `prime-cube-taxicab-verifier.py`  
- **CC BY 4.0** (Creative Commons Attribution 4.0 International) for all other content (paper, results, README, etc.)
