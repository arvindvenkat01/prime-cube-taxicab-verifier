# The Prime Cube Taxicab Equation: Computational Evidence and Theoretical Analysis

**Author**: Arvind N. Venkat

This work has been archived and assigned a permanent identifier on Zenodo:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17066282.svg)](https://doi.org/10.5281/zenodo.17066282)


- DOI: `10.5281/zenodo.17066282`
- URL: `[https://zenodo.org/records/17066282](https://zenodo.org/records/17066282)`

## Abstract

We investigate the Diophantine equation `p1^3 + n^2 = p2^3 + p3^3` where `p1`, `p2`, `p3` are consecutive primes and `n` is a positive integer. Through exhaustive computational verification of all consecutive prime triples with `p3 <= 9,999,941,551`, we provide strong empirical evidence that this equation has exactly two integer solutions. The code in this repository was used to perform this large-scale verification, finding solutions `(2,3,5,12)` and `(3,5,7,21)`. These solutions exhibit the remarkable property that the ratios `n/p1` are consecutive integers (6 and 7), hinting at deeper underlying mathematical structure.


## Repository Contents

- `prime-cube-taxicab-verifier.py`: The Python script containing the computational verification algorithm.
- `result.txt`: The full output of the verification run, showing the solutions found and the total computation time.

## Prerequisites

- Python 3.8 or higher  
- Python libraries: `numpy`, `numba`


## Getting Started

To run the code and reproduce the results, you will need to have Python 3.8+ and the necessary libraries installed.

1. **Clone this repository:**
   ```
   git clone https://github.com/arvindvenkat/prime-cube-taxicab-verifier.git
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

If you use this work, please cite the paper using the Zenodo archive.

@misc{naladiga_venkat_2025_17066282,
  author       = {Naladiga Venkat, Arvind},
  title        = {The Prime Cube Taxicab Equation: Computational
                   Evidence and Theoretical Analysis
                  },
  month        = sep,
  year         = 2025,
  publisher    = {Zenodo},
  version      = {v2},
  doi          = {10.5281/zenodo.17066282},
  url          = {https://doi.org/10.5281/zenodo.17066282},
}



---

## License

The content of this repository is dual-licensed:

- **MIT License** for `prime-cube-taxicab-verifier.py`  
- **CC BY 4.0** (Creative Commons Attribution 4.0 International) for all other content (paper, results, README, etc.)
