from oil_correlations.module import read_match_data_file
from correlations import Standing, Glaso
from pprint import pprint
file = read_match_data_file("C:/Users/3D/Desktop/FYP-MY-DATA - Copy.csv")
glaso = Glaso(p=2377, gg=0.851, t=(250 + 460), oil_api=47.7)
rs = glaso.solution_gas_oil_ratio()
print(rs)



if __name__ == "__main__":
    pass