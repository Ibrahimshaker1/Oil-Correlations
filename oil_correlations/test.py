from oil_correlations.module import read_match_data_file
from correlations import Standing, Glaso, Marhoun, VasquezBeggs
from pprint import pprint
file = read_match_data_file("C:/Users/3D/Desktop/FYP-MY-DATA - Copy.csv")
pressure = 2620
gas = 0.855
t = 220 + 460
api = 40.7
lab_rs = 768
vb = VasquezBeggs(p=[1000, pressure], gg=gas, oil_api=api, t=t, p_s=100+14.7, t_s=75+460)
rs = vb.solution_gas_oil_ratio()
pb = vb.bubble_point_pressure(rs=rs["Rs"])
print(f"Rs: {rs}")
print(f"Pb: {pb}")



if __name__ == "__main__":
    pass
