class URLs:
    BASE = "https://qa-scooter.praktikum-services.ru"
    DZEN = "https://dzen.ru/?yredirect=true"
    
    @property
    def MAIN(self):
        return f"{self.BASE}/"
    
    @property
    def ORDER(self):
        return f"{self.BASE}/order"
    
    @property
    def TRACK(self):
        return f"{self.BASE}/track"

URL = URLs()