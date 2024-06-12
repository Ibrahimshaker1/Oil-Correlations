from oil_correlations.module import read_match_data_file
from correlations import Standing
from pprint import pprint
file = read_match_data_file("C:/Users/3D/Desktop/FYP-MY-DATA - Copy.csv")
standing = Standing(p=file["P"], gg=0.855, t=(220 + 460), oil_api=40.7)
rs = standing.solution_gas_oil_ratio()
pb = standing.bubble_point_pressure(rs=rs["Rs"])
bo = standing.oil_formation_volume_factor(rs=rs["Rs"])


if __name__ == "__main__":
    pass