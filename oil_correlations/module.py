# this module include functions to read the user data assuming the data hand .csv suffix

def read_match_data_file(file_path: str) -> list:
    """
        this function take the file path as and input and return the columns as a list
        the columns must named (P, Rs, Bo, Co)
        where:
            P: pressure (psia)
            Rs: Solution Gas Oil Ratio (scf/stb)
            Bo: Formation Volume Factor
            Co: Oil Compressibility (psia^-1)
        * the pressure columns is required
        example:
        match_data = read_match_data_file(file_path='C:/Users/Data')
    """
    with open(file_path, "r") as file:
        file_data = file.readlines()
    match_data = {
        "columns": [],
        "P": [],
        "Rs": [],
        "Bo": [],
        "Co": []

    }
    for line in file_data:
        line = line.rstrip("\n")
        if "ï»¿" in line:
            if "P" not in line:
                raise SystemExit("Pressure column is required in match data called 'Pressure or P'")
            else:
                columns_name = line.replace("ï»¿", "")
                columns_name_list = columns_name.split(",")
                match_data["columns"] = columns_name_list[:]
                del columns_name
                del columns_name_list
        else:
            line_data = line.split(",")
            match_data["P"].append(float(line_data[0]))
            if line_data[1] != "":
                match_data["Rs"].append(float(line_data[1]))
            if line_data[2] != "":
                match_data["Bo"].append(float(line_data[2]))
            if line_data[3] != "":
                match_data["Co"].append(float(line_data[3]))
    return match_data



