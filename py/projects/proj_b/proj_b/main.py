import numpy as np

from mycorp.lib1.mysum import mysum
from mycorp.lib2.mymult import mymult

if __name__ == "__main__":
    print("Starting proj_b main.py")
    print(np.random.rand())

    print(f"{mysum(2, 9)=}")
    print(f"{mymult(2, 3)=}")