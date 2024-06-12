# this module hand the correlations code each correlation is a class
class Standing:
    def __init__(self, p: list | float, gg: float | int, oil_api: float | int, t: float | int):
        self.pressure = p
        self.gas_gravity = gg
        self.oil_api = oil_api
        self.temp = t

    def solution_gas_oil_ratio(self):
        """
            This function return the estimated value of Rs
        """
        def rs_standing_correlation(gg, p, oil_api, t):
            x_parament = (0.0125 * oil_api) - (0.00091*(t-460))
            param_one = (p/18.2)+1.4
            standing_rs = gg*((param_one*(10**x_parament))**1.2048)
            return standing_rs
        if isinstance(self.pressure, list):
            standing_rs = {
                "pressure": self.pressure,
                "Rs": [],
            }
            for p in self.pressure:
                standing_rs["Rs"].append(rs_standing_correlation(gg=self.gas_gravity, p=p, oil_api=self.oil_api, t=self.temp))
            return standing_rs
        else:
            return rs_standing_correlation(gg=self.gas_gravity, p=self.pressure, oil_api=self.oil_api, t=self.temp)

    def bubble_point_pressure(self, rs: float | list | int):
        """
            This function return the estimated value of Pb
        """
        def pb_standing_calculator(rs, gg, oil_api, t):
            a = 0.00091 * (t - 460) - 0.0125 * oil_api
            t_p = 10**a
            param_one = (rs/gg)**0.83
            pb = 18.2 * (param_one * t_p - 1.4)
            return pb
        if isinstance(rs, list):
            standing_pb = {
                "Rs": rs,
                "Pb": []
            }
            for r in rs:
                standing_pb["Pb"].append(pb_standing_calculator(rs=r, gg=self.gas_gravity, oil_api=self.oil_api, t=self.temp))
            return standing_pb
        else:
            return pb_standing_calculator(rs=rs, gg=self.gas_gravity, oil_api=self.oil_api, t=self.temp)

    def oil_formation_volume_factor(self, rs):
        """
            This function return the estimated value of Bo
        """
        oil_gravity = 141.5/(self.oil_api + 131.5)

        def bo_standing_calculator(rs, gg, og, t):
            param_one = (gg/og)**0.5
            param_two = (rs*param_one + 1.25*(t-460))**1.2
            bo = 0.9759 + 0.000120 * param_two
            return bo
        if isinstance(rs, list):
            standing_bo = {
                "Rs": rs,
                "Bo": []
            }
            for r in rs:
                standing_bo["Bo"].append(bo_standing_calculator(rs=r, gg=self.gas_gravity, og=oil_gravity, t=self.temp))
            return standing_bo
        else:
            return bo_standing_calculator(rs=rs, gg=self.gas_gravity, og=oil_gravity, t=self.temp)

