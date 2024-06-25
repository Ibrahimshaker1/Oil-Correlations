# this module hand the correlations code each correlation is a class
import math
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


class Glaso:
    def __init__(self, p: list | float, gg: float | int, oil_api: float | int, t: float | int):
        self.pressure = p
        self.gas_gravity = gg
        self.oil_api = oil_api
        self.temp = t

    def solution_gas_oil_ratio(self):
        """
            This function return the estimated value of Rs
        """
        def glaso_rs_calculator(gg, oil_api, t, p):
            x = 2.8869 - (14.1811 - 3.3093 * math.log10(p))**0.5
            pb_s = 10**x
            param_one = (oil_api**0.989)/((t-460)**0.172)
            g_rs = gg*(param_one*pb_s)**1.2255
            return g_rs
        if isinstance(self.pressure, list):
            glaso_rs = {
                "P": self.pressure,
                "Rs": []
            }
            for p in self.pressure:
                glaso_rs["Rs"].append(glaso_rs_calculator(gg=self.gas_gravity, oil_api=self.oil_api, t=self.temp, p=p))
            return glaso_rs
        else:
            return glaso_rs_calculator(gg=self.gas_gravity, oil_api=self.oil_api, t=self.temp, p=self.pressure)


    def bubble_point_pressure(self, rs):
        """
                    This function return the estimated value of Pb
        """
        def glaso_pb_calculator(rs, gg, t, oil_api):
            t = t - 460  # temperature must be in F
            x = (rs/gg)**0.816
            y = t**0.172
            z = oil_api**(-0.989)
            pb_star = x * y * z
            param_one = 1.7447*math.log10(pb_star)
            param_two = 0.30218*(math.log10(pb_star))**2
            log_pb = 1.7669 + param_one - param_two
            pb = 10**log_pb
            return pb
        if isinstance(rs, list):
            glaso_pb = {
                "Rs": rs,
                "pb": []
            }
            for r in rs:
                glaso_pb["pb"].append(glaso_pb_calculator(rs=r, gg=self.gas_gravity, t=self.temp, oil_api=self.oil_api))
            return glaso_pb
        else:
            return glaso_pb_calculator(rs=rs, gg=self.gas_gravity, t=self.temp, oil_api=self.oil_api)

    def oil_formation_volume_factor(self, rs):
        """
            this function return the estimated value of Bo
        """
        oil_gravity = 141.5/(self.oil_api + 131.5)

        def glaso_bo_calculator(rs, gg, og, t):
            bob_star = rs*((gg/og)**0.526) + 0.968*(t - 460)
            param_a = -6.58511 + 2.91329*math.log10(bob_star) - 0.27683*(math.log10(bob_star))**2
            bo = 1 + 10**param_a
            return bo
        if isinstance(rs, list):
            glaso_Bo = {
                "Rs": rs,
                "Bo": []
            }
            for r in rs:
                glaso_Bo["Bo"].append(glaso_bo_calculator(rs=r, gg=self.gas_gravity, og=oil_gravity, t=self.temp))
            return glaso_Bo
        else:
            return glaso_bo_calculator(rs=rs, gg=self.gas_gravity, og=oil_gravity, t=self.temp)


class Marhoun:
    def __init__(self, p: list | float, gg: float | int, oil_api: float | int, t: float | int):
        self.pressure = p
        self.gas_gravity = gg
        self.oil_api = oil_api
        self.temp = t

    def solution_gas_oil_ratio(self):
        """
            this function return
        """
        oil_gravity = 141.5/(self.oil_api + 131.5)

        def marhoun_rs_calculator(gg, og, t, p):
            rs = (185.843208*(gg**1.877840)*(og**-3.1437)*(t**-1.32657)*p)**1.398441
            return rs
        if isinstance(self.pressure, list):
            marhoun_rs = {
                "P": self.pressure,
                "Rs": []
            }
            for p in self.pressure:
                marhoun_rs["Rs"].append(marhoun_rs_calculator(gg=self.gas_gravity, og=oil_gravity, t=self.temp, p=p))
            return marhoun_rs
        else:
            return marhoun_rs_calculator(gg=self.gas_gravity, og=oil_gravity, t=self.temp, p=self.pressure)

    def bubble_point_pressure(self, rs):
        """
            this function return estimated value of Pb
        """
        oil_gravity = 141.5 / (self.oil_api + 131.5)


        def marhoun_pb_calculator(rs, gg, og, t):
            pb = ((5.38088*10**-3)*(rs**0.715082)*(gg**-1.87784)*(og**3.1427)*(t**1.32657))
            return pb
        if isinstance(rs, list):
            marhoun_pb ={
                "Rs": rs,
                "Pb": []
            }
            for r in rs:
                marhoun_pb["Pb"].append(marhoun_pb_calculator(rs=r, gg=self.gas_gravity, og=oil_gravity, t=self.temp))
            return marhoun_pb
        else:
            return marhoun_pb_calculator(rs=rs, gg=self.gas_gravity, og=oil_gravity, t=self.temp)


    def oil_formation_volume_factor(self, rs):
        """
            this function return estimated value of Bo
        """
        oil_gravity = 141.5 / (self.oil_api + 131.5)
        def marhoun_bo_calculator(rs, gg, og, t):
            f = (rs**0.74239)*(gg**0.323294)*(og**-1.20204)
            bo = 0.497069 + (0.862963*(10**-3)*t) + (0.182594*(10**-2)*f) + (0.318099*(10**-5)*(f**2))
            return bo
        if isinstance(rs, list):
            marhoun_bo = {
                "Rs": rs,
                "Bo": []
            }
            for r in rs:
                marhoun_bo["Bo"].append(marhoun_bo_calculator(rs=r, gg=self.gas_gravity, og=oil_gravity, t=self.temp))
            return marhoun_bo
        else:
            return marhoun_bo_calculator(rs=rs, gg=self.gas_gravity, og=oil_gravity, t=self.temp)



