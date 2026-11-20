"""Featured products transcribed from the June 2026 company catalogue."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    slug: str
    family: str
    brand: str
    name: str
    item: str
    size: str
    contents: str
    carton: str
    description: str


PRODUCTS = [
    Product("wet-blue", "wet", "家必备", "卫生湿巾", "J-8010", "180 × 180 mm", "30 片 / 包", "48 包 / 箱", "翻盖抽取包装，适合外出携带与家庭日常清洁。"),
    Product("baby", "wet", "晓宝", "婴儿手口湿巾", "5599", "180 × 140 mm", "80 片 / 包", "24 包 / 箱", "家庭装婴儿手口湿巾，采用翻盖设计，方便日常抽取。"),
    Product("makeup", "wet", "家必备", "卸妆湿巾", "J-3336", "180 × 150 mm", "30 片 / 包", "120 包 / 箱", "用于日常卸妆清洁。该系列提供绿色和粉色两种包装。"),
    Product("kitchen-wet", "wet", "家必备", "厨房湿巾", "J-5438", "260 × 200 mm", "45 片 / 包", "16 包 / 箱", "面向厨房日常擦拭场景，单片尺寸为 260 × 200 毫米。"),
    Product("pet", "wet", "家必备", "宠物湿巾", "J-6337", "180 × 190 mm", "100 片 / 包", "18 包 / 箱", "面向宠物日常清洁，采用翻盖抽取式包装。"),
    Product("dry-facial", "dry", "片片亲", "洗脸柔巾", "P-6696", "200 × 200 mm", "156 片 / 包", "16 包 / 箱", "方形巾面配抽取式包装，适合洗脸与日常擦拭。"),
    Product("dry-tissue", "dry", "片片亲", "棉柔巾", "5841", "200 × 200 mm", "60 片 / 包", "50 包 / 箱", "方形巾面，可放置于洗漱台或收纳架上，方便日常取用。"),
    Product("dry-bag", "dry", "晓宝", "亲肤棉柔巾", "5612", "200 × 200 mm", "210 g / 包", "36 包 / 箱", "束口袋包装，单包重量为 210 克，适合家庭洗护场景。"),
    Product("dry-roll", "dry", "片片亲", "卷装棉柔巾", "5810", "200 × 200 mm", "430 g / 卷", "18 卷 / 箱", "卷装棉柔巾，以卷为单位装箱，面向家庭与商业洗护场景。"),
    Product("kitchen-roll", "paper", "家必备", "厨房纸巾", "5827", "223 × 210 mm", "75 节 / 卷，2 卷 / 包", "20 包 / 箱", "双卷包装厨房纸，方便在备餐、烹饪与餐后台面整理时取用。"),
    Product("bamboo", "paper", "家必备", "抽取式面巾纸", "SH001", "155 × 190 mm", "352 张 / 包", "10 包 / 提，10 提 / 件", "采用原生竹浆，抽取式设计适用于家庭与办公场所。"),
    Product("hand-towel", "paper", "商用纸品", "抽取式擦手纸", "", "225 × 230 mm", "140 抽 / 包", "", "采用原生木浆，折叠抽取，适合公共洗手间及商业空间使用。"),
]
