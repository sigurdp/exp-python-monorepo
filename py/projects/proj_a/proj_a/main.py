import mycorp.server_schemas.schema_x as schema_x

if __name__ == "__main__":
    print("Starting proj_a main.py")

    mystuff = schema_x.Stuff(mystr="XXX", myints=[10, 20, 30])
    print(f"{mystuff=}")
