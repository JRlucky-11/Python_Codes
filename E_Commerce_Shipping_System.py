from abc import ABC, abstractmethod

class Shipping_Carrier(ABC):
    @abstractmethod
    def carrier_name(self):
        pass

    @abstractmethod
    def Calculation_rate(self, weight):
        pass
    
class FedEx(Shipping_Carrier):
    def carrier_name(self):
        return "FedEx Express"

    def Calculation_rate(self, weight):
        return 5.00 + (1.50 * weight)
        
class DHL(Shipping_Carrier):
    def carrier_name(self):
        return "DHL Global"

    def Calculation_rate(self, weight):
        if weight < 5:
            return 12.00
        else:
            return 25.00

carriers = [FedEx(), DHL()]
package_weight = 7.0

for carr in carriers:
    name = carr.carrier_name()
    rate = carr.Calculation_rate(package_weight)
    print(f"Carrier: {name}, Shipping Rate for {package_weight} kg: ${rate:.2f}")
