from oil_correlations.module import read_match_data_file
from correlations import Standing, Glaso, Marhoun
from pprint import pprint
file = read_match_data_file("C:/Users/3D/Desktop/FYP-MY-DATA - Copy.csv")
pressure = 4239
gas = 0.848
t = 180 + 460
api = 27.3
lab_rs = 807
marhoun = Marhoun(p=[1000, 2000, 3000], gg=gas, oil_api=api, t=t)
rs = marhoun.solution_gas_oil_ratio()
pb = marhoun.bubble_point_pressure(rs=rs["Rs"])
bo = marhoun.oil_formation_volume_factor(rs=rs["Rs"])
print(f"Rs: {rs}")
print(f"Pb: {pb}")
print(f"Bo: {bo}")


if __name__ == "__main__":
    pass
