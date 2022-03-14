class Dad:
    basketball=1
    pass
class Son(Dad):
    dance=1
    def isdance(self):
        return f"Yes I dance {self.dance} number of times"
    pass
class Grandson(Son):
    dance=6
    def isdance(self):
        return f"Yes I dance very good {self.dance} number of times"
    pass

darry=Dad()
Larry=Son()
Hardik=Grandson()
print(Hardik.isdance())
print(Hardik.basketball)