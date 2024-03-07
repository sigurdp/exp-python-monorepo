import mycorp.server_schemas.schema_x as schema_x

from .business_logic import execute_main_logic

from proj_a.utils.util_1 import add1
from .utils.util_2 import add2


def main():
    print("Executing main() in proj_a")

    mystuff = schema_x.Stuff(mystr="XXX", myints=[10, 20, 30])
    print(f"{mystuff=}")

    print(f"{add1(2)=}")
    print(f"{add2(2)=}")

    execute_main_logic()


# As it is currently wired, this must be run using:
#  python -m proj_a.app_main
# or it can be run using the run_main.py script in the parent directory:
#  python run_main.py
#
# See:
# https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time/14132912#14132912

if __name__ == "__main__":
    print("Starting proj_a app_main.py")
    main()
