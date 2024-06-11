# this module include functions to read the user data assuming the data hand .csv suffix

def read_data_file(file_path: str) -> list:
    # """
    #     this function take the file path as and input and return the columns as a list
    #     the columns should named (P, Rs, Bo, Co, U)
    #     where:
    #         p: pressure (psia)
    #         Rs: Solution Gas Oil Ratio (scf/stb)
    #         Bo: Formation Volume Factor
    #         Co: Oil Compressibility (psia^-1)
    #         U: viscosity (cp)
    #     example:
    #     P, Rs, Bo, Co, U = read_data_file(file_path='C:/Users/Data')
    #     print(P)
    #     [1000, 2000, 2500, ...]
    # """
    path = file_path
    new_path = ""
    if "\\" in path:
        new_path = path.replace("\\", "/")
        return new_path
    else:
        return path





