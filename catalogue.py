"""Product variants in their printed order in the June 2026 company catalogue."""
import json
from dataclasses import dataclass
from pathlib import Path


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

    def branded_name(self, separator=""):
        return self.name if self.name.startswith(self.brand) else self.brand + separator + self.name


records = json.loads(Path(__file__).with_name("catalogue.json").read_text(encoding="utf-8"))
PRODUCTS = [Product(**record) for record in records]
