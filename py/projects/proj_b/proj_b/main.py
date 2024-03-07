import numpy as np

from mycorp.lib1.mysum import mysum
from mycorp.lib1.myjoke import get_me_a_joke

from mycorp.lib2.mymult import mymult


if __name__ == "__main__":
    print("Starting proj_b main.py")
    print(np.random.rand())

    print(f"{mysum(2, 9)=}")
    print(f"{mymult(2, 3)=}")

    print(f"{get_me_a_joke()=}")
