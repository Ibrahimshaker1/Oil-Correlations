from oil_correlations.module import read_match_data_file
from correlations import Standing, Glaso, Marhoun, VasquezBeggs, Petrosky
from pprint import pprint
file = read_match_data_file("C:/Users/3D/Desktop/FYP-MY-DATA - Copy.csv")
pressure = 2620
gas = 0.855
t = 220 + 460
api = 40.7
lab_rs = 768
petroksy = Petrosky(p=[1000, 2000, pressure], t=t, gg=gas, oil_api=api)
rs = petroksy.solution_gas_oil_ratio()
pb = petroksy.bubble_point_pressure(rs=rs["Rs"])
bo = petroksy.oil_formation_volume_factor(rs=rs["Rs"])
print(f"Rs: {rs}")
print(f"Pb: {pb}")
print(f"Bo: {bo}")



if __name__ == "__main__":
    pass
