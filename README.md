# Oil Correlations Package

## A simple package include the most famous oil correlation **(Standing, Glaso, Marhoun, VasquezBeggs, Petrosky)**. For Estimating Oil PVT Properties

## Imported

The output and Input unit
* P: psia
* T: R°
* Rs: (scf/stb)
* Bo: (bbl/STB)
* Co: psia^-1

## About The Package

This package had two modules:

* correlations.py
  This module include the correlation code where where every researcher is a object,
  and the correlations is a method in this object, example:
  ```
  from oil_correlations.correlations import Standing

  p = 2000
  t = 200 + 460
  gas_gravity = 0.8
  oil_api = 40
  
  standing = Standing(gg=gas_gravity, t=t, p=p, oil_api=oil_api)
  Rs = standing.solution_gas_oil_ratio()
  Pb = standing.bubble_point_pressure(rs=Rs)
  Bo = standing.oil_formation_volume_factor(rs=Rs)
  print(f"Rs: {Rs}\nPb: {Pb}\nBo: {Bo}")
  ```
  If the pressure input was a list the method will
  return a dictionary had two key and the value is a list
* module.py
  This module include only one function to read a csv file for lab data that can be use for 
  matching the file coulumns names must be (P, Rs, Bo, Co), this function will return a 
  dictionary example, 
  ```
  from oil_correlations.module import read_match_data_file
  from pprint import pprint
  file_path = "C:/Users/Desktop/FYP-MY-DATA - Copy.csv"
  data = read_match_data_file(file_path=file_path)
  pprint(data)
  ```
  data example:

  ![image](https://github.com/user-attachments/assets/84bed2cc-54df-478b-aee9-871085588cb5)

  
### How to use it
clone the repo `clone https://github.com/Ibrahimshaker1/Oil-Correlations.git`

Feel free to report for any error 
  

