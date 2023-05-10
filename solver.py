"""A solver for the 1D diffusion equation."""

import numpy as np

#spacing format for print statements
np.set_printoptions(formatter={"float": "{: 6.1f}".format})


#function to solve for concentration after diffusion
def solve1d(concentration, spacing, time_step, diffusivity):
    flux = - diffusivity * np.diff(concentration) / spacing
    concentration[1:-1] -= time_step * np.diff(flux) / spacing
    return concentration
    

#function to run solved1d
def _example():
    D = 100
    Lx = 10
    dx = 0.5
    C1 = 500
    C2 = 0
    C = np.empty(Lx)
    C[: int(Lx/2)] = C1
    C[int(Lx/2) :] = C2
    dt = dx * dx /D/2.1
    print(C)
    
    #loop
    for _ in range(1,5):
        C = solve1d(C, dx, dt, D)
        print(C)

    
if __name__ == "__main__":
    _example()