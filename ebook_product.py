class StoreProduct:
    def __init__(self, sku, price):
        self.sku = sku
        self.price = price
    
    def display_catalog_info(self):
        print(f"SKU: [{self.sku}] || Price: $[{self.price}]")
    
class DigitalAsset:
    def __init__(self, file_size_mb):
        self.file_size_mb = file_size_mb
    
    def generate_download_link(self):
        print(f"Download Successfully || Size: [{self.file_size_mb}Mb]")

class EBookProduct(StoreProduct, DigitalAsset):
    def __init__ (self, sku, price, file_size_mb):
        StoreProduct.__init__(self, sku, price)
        DigitalAsset.__init__(self, file_size_mb)
    
ebook1 = EBookProduct(sku="BK-101", price=19.99, file_size_mb=15.5)
ebook1.display_catalog_info()
ebook1.generate_download_link()