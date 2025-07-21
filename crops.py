class Crop:
    def __init__(self,name,yld,n_upk,p_upk,k_upk):
        self.name = name
        self.yld = yld
        self.n_upk = n_upk
        self.p_upk = p_upk
        self.k_upk = k_upk
        self.n_req = self.n_upk * self.yld
        self.p_req = self.p_upk * self.yld
        self.k_req = self.k_upk * self.yld

    def output(self):
        output_data = {
            "Cultura": [self.name],
            "Produtividade": [self.yld],
            "N_requerido": [self.n_req],
            "P_requerido": [self.p_req],
            "K_requerido":[self.k_req]
        }
        return output_data


class Corn(Crop):
    def __init__(self,yld):
        super().__init__(
            name = "Corn",
            yld = yld,
            n_upk = 14.4,
            p_upk = 3.4,
            k_upk = 5.4
        )

class Soybean(Crop):
    def __init__(self,yld):
        super().__init__(
            name = "Soybean",
            yld = yld,
            n_upk = 0,
            p_upk = 4.5,
            k_upk = 14.2
        )

class Wheat(Crop):
    def __init__(self,yld):
        super().__init__(
            name = "Wheat",
            yld = yld,
            n_upk = 20,
            p_upk = 3.2,
            k_upk = 3.5
        )

