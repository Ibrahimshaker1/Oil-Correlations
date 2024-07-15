# Oil Correlations Package

## A simple package include the most famous oil correlation (Standing, Glaso, Marhoun, VasquezBeggs, Petrosky).
## For Estimating Oil PVT Properties

## Importend

The output and Input unit
* P: psia
* T: R°
* Rs: (scf/stb)
* Bo: (bbl/STB)
* Co: psia^-1

## About The Package

The package had two modules:

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
  
