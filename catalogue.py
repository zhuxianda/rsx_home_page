"""Product variants in their printed order in the June 2026 company catalogue."""
import json
from dataclasses import dataclass
from pathlib import Path


OWN_BRANDS = {"家必备": "jiabibei", "片片亲": "pianpianqin", "晓宝": "xiaobao"}


@dataclass(frozen=True)
class Product:
    slug: str
    page: int
    channel: str
    family: str
    brand: str
    name: str
    item: str = ""
    size: str = ""
    contents: str = ""
    carton: str = ""
    description: str = ""
    client: str = ""
    material: str = ""
    barcode: str = ""
    note: str = ""
    barcode_label: str = "图册条码"
    standard: str = ""
    shelf_life: str = ""
    previous_channel: str = ""

    def branded_name(self, separator=""):
        return self.name if self.name.startswith(self.brand) else self.brand + separator + self.name

    @property
    def catalogue_group(self):
        if self.channel == "自有品牌" and self.brand in OWN_BRANDS:
            return self.brand
        if self.channel in ("定制", "商用纸品"):
            return self.channel
        return "代工 OEM"

    @property
    def business_type(self):
        # Existing business filters and bookmarked URLs group both kinds of contract work.
        return "OEM 与定制" if self.catalogue_group in ("代工 OEM", "定制") else self.channel


records = json.loads(Path(__file__).with_name("catalogue.json").read_text(encoding="utf-8"))
PRODUCTS = [Product(**record) for record in records]
