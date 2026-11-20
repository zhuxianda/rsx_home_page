"""English catalogue text, keyed by the printed Chinese product data."""
import re


TERMS = {
    # Catalogue sections and specification labels.
    "全部产品": "All products",
    "自有品牌": "In-house brands",
    "代工 OEM": "OEM",
    "定制": "Custom orders",
    "OEM 与定制": "OEM & custom orders",
    "商用纸品": "Commercial tissue",
    "其他品牌": "Other brands",
    "湿巾系列": "Wet wipes",
    "棉柔巾系列": "Soft dry wipes",
    "生活用纸系列": "Tissue paper",
    "清洁护理系列": "Home & personal care",
    "所属业务": "Business segment",
    "品牌 / 系列": "Brand / range",
    "合作项目": "Client",
    "产品货号": "Item number",
    "尺寸 / 尺码": "Size",
    "包装规格": "Pack size",
    "装箱规格": "Case pack",
    "材质": "Material",
    "保质期": "Shelf life",
    "执行标准": "Product standard",
    "图册条码": "Catalogue barcode",
    "包装条码": "Barcode on pack",
    # Use the displayed mark where the artwork provides a Latin-script name.
    "家必备": "Jiabibei",
    "片片亲": "Pianpianqin",
    "晓宝": "Xiaobao",
    "本该如此": "Bengai Ruci",
    "玫迪森": "Meidisen",
    "结伴同行": "Jieban Tongxing",
    "竹森林": "Zhusenlin",
    "自由点": "Freemore",
    "洁柔": "C&S",
    "维邦": "V.Poon",
    "维邦纸业": "V.Poon Paper",
    "优多邦": "Youduobang",
    "厮磨工坊": "Small Workshop",
    "柔贝佳": "Roubeijia",
    "开心朵朵": "Happy Flowers",
    "阳阳纸业": "Yangyang Paper",
    "桔子姑娘": "Juziguniang",
    "欧露": "Oulu",
    "鸥露": "Oulu",
    "雅思": "Yasi",
    "雅诗纸业": "Yashi Paper",
    "柔康莱": "Roukanglai",
    "百惠": "Baihui",
    "谜库": "MKU",
    "美乐美妆连锁": "Meile Beauty",
    "卿易舒": "Qingyishu",
    "万华大药房": "Wanhua Pharmacy",
    "汇鑫源·休闲庄": "Huixinyuan Leisure Resort",
    "汇鑫苑·休闲庄": "Huixinyuan Leisure Resort",
    "食锦荟": "Shijinhui",
    # Product names.
    "婴儿手口湿巾": "Baby hand and mouth wipes",
    "卫生湿巾": "Hygiene wipes",
    "家必备牌湿厕纸": "Jiabibei moist toilet tissue",
    "冰爽湿巾": "Cooling wipes",
    "卸妆湿巾": "Makeup remover wipes",
    "宠物湿巾": "Pet wipes",
    "清洁湿巾": "Cleaning wipes",
    "洁肤柔湿巾": "Soft skin cleansing wipes",
    "面膜补水湿巾": "Hydrating facial mask wipes",
    "皮革清洁湿巾": "Leather cleaning wipes",
    "厨房湿巾": "Kitchen cleaning wipes",
    "保湿柔纸巾": "Moisturizing soft tissues",
    "厨房纸巾": "Kitchen paper towels",
    "抽取式面巾纸": "Pop-up facial tissues",
    "冰感小毛巾": "Cooling hand towel",
    "洗脸柔巾": "Soft face towels",
    "压缩毛巾": "Compressed towels",
    "一次性浴巾面巾套装": "Disposable bath and face towel set",
    "一次性内裤": "Disposable underwear",
    "棉柔巾": "Soft dry wipes",
    "亲肤棉柔巾": "Gentle dry wipes",
    "卷装棉柔巾": "Soft dry wipes on a roll",
    "包头巾": "Hair wrap towel",
    "洗衣液": "Laundry detergent",
    "油污净": "Kitchen degreaser",
    "免冲洗洗发帽": "No-rinse shampoo cap",
    "亲肤婴儿手口湿巾": "Gentle baby hand and mouth wipes",
    "湿巾": "Wet wipes",
    "乳霜纸": "Lotion tissues",
    "水润柔肤湿巾": "Moisturizing skin wipes",
    "卷巾": "Towel roll",
    "湿厕纸": "Moist toilet tissue",
    "纯水湿巾": "Pure water wipes",
    "卷纸": "Roll tissue",
    "定制湿毛巾": "Custom wet hand towel",
    "抽取式擦手纸": "Folded paper hand towels",
    "卷式擦手纸": "Paper hand towel roll",
    "商用笑脸抽纸": "Commercial pop-up tissues, Smiley Face",
    "商用大白抽纸": "Commercial pop-up tissues, Dabai",
    # Variant descriptions in parentheses after product names.
    "绿色": "green",
    "紫色": "purple",
    "蓝色": "blue",
    "粉色": "pink",
    "10片装": "10-sheet pack",
    "独立装": "individually wrapped",
    "绿色包装": "green pack",
    "橙色包装": "orange pack",
    "蓝标": "blue label",
    "粉标": "pink label",
    "加厚": "extra thick",
    "两用抽取式": "dual-use pop-up pack",
    "底部抽": "bottom-dispensing pack",
    "抽巾": "pop-up pack",
    "男士": "men’s",
    "女士": "women’s",
    "束口袋": "drawstring bag",
    "抽取装": "pop-up pack",
    "两瓶装": "twin pack",
    "赠品": "promotional pack",
    "白色包装": "white pack",
    "黑色包装": "black pack",
    "6 包装": "6-pack",
    # Preserve the units as printed, including dimensions pending confirmation.
    "浴巾 680 × 1400，面巾 280 × 600": "Bath towel 680 × 1400, face towel 280 × 600",
    "L、XL、XXL": "L, XL, XXL",
    "98 × 125 mm / 节": "98 × 125 mm per sheet",
    "500 g × 2 瓶": "2 bottles × 500 g",
    "两年": "2 years",
    # Materials. Gram values are transcribed as given in the source.
    "原生竹浆": "Virgin bamboo pulp",
    "纯棉": "Pure cotton",
    "木浆 50%、涤纶 50%，60 g": "50% wood pulp, 50% polyester, 60 g",
    "20% 粘胶、80% 涤纶，60 g 珍珠纹": "20% viscose, 80% polyester, 60 g, pearl texture",
    "100% 原生木浆": "100% virgin wood pulp",
    "30% 粘胶、70% 涤纶，60 g 平纹": "30% viscose, 70% polyester, 60 g, plain texture",
    "50% 粘胶、50% 涤纶，60 g 平纹": "50% viscose, 50% polyester, 60 g, plain texture",
    "100% 植物源纤维，80 g 珍珠纹": "100% plant-derived fibre, 80 g, pearl texture",
    "100% 植物源纤维，90 g 珍珠纹": "100% plant-derived fibre, 90 g, pearl texture",
    "20% 粘胶、80% 涤纶，55 g 平纹": "20% viscose, 80% polyester, 55 g, plain texture",
    "50% 粘胶、50% 涤纶，60 g 珍珠纹": "50% viscose, 50% polyester, 60 g, pearl texture",
    "30% 粘胶、70% 涤纶，70 g 珍珠纹": "30% viscose, 70% polyester, 70 g, pearl texture",
    "100% 原生木浆，70 g": "100% virgin wood pulp, 70 g",
    "100% 植物源纤维，90 g 花纹": "100% plant-derived fibre, 90 g, patterned texture",
    "40% 粘胶、60% 涤纶，80 g": "40% viscose, 60% polyester, 80 g",
    "全涤纶，55 g": "100% polyester, 55 g",
    "100% 原生木浆，60 g": "100% virgin wood pulp, 60 g",
    "100% 植物源纤维，95 g 水波纹": "100% plant-derived fibre, 95 g, wave texture",
    "100% 涤纶，70 g": "100% polyester, 70 g",
    "100% 原生木浆，75 g": "100% virgin wood pulp, 75 g",
    "100% 原生竹浆": "100% virgin bamboo pulp",
    "原生木浆、进口乳霜": "Virgin wood pulp and imported lotion",
    "锦 20%、涤 80%": "20% nylon, 80% polyester",
    "100% 本色原生浆": "100% natural-colour virgin pulp",
    # Editorial notes and catalogue product descriptions.
    "图册中的尺寸单位不一致，单位待确认。":
        "The catalogue lists inconsistent units for these dimensions. Please confirm the units when ordering.",
    "图册将此货号用于湿厕纸、卷纸及保湿柔纸巾三款产品。订货时请同时核对品名和规格。":
        "The catalogue uses this item number for moist toilet tissue, roll tissue and moisturizing soft tissues. Please confirm the product name and specifications when ordering.",
    "翻盖抽取包装，适合外出携带与家庭日常清洁。":
        "A flip-top pack dispenses wipes one at a time for everyday cleaning at home or on the go.",
    "限用日期及生产批号见包装喷码。":
        "The expiry date and batch number are printed on the pack.",
    "用于日常卸妆清洁。该系列提供绿色和粉色两种包装。":
        "Wipes for everyday makeup removal, available in green or pink packaging.",
    "面向宠物日常清洁，采用翻盖抽取式包装。":
        "Wipes for everyday pet care, in a flip-top dispenser pack.",
    "面向厨房日常擦拭场景，单片尺寸为 260 × 200 毫米。":
        "Each wipe measures 260 × 200 mm for everyday kitchen cleaning.",
    "双卷包装厨房纸，方便在备餐、烹饪与餐后台面整理时取用。":
        "Two rolls per pack for food preparation, cooking and wiping down kitchen surfaces after meals.",
    "采用原生竹浆，抽取式设计适用于家庭与办公场所。":
        "Pop-up tissues made from virgin bamboo pulp for use at home or in the office.",
    "方形巾面配抽取式包装，适合洗脸与日常擦拭。":
        "Square towels in a pop-up pack for face washing and everyday cleansing.",
    "方形巾面，可放置于洗漱台或收纳架上，方便日常取用。":
        "Square towels for everyday use. Keep the pack on a bathroom counter or shelf.",
    "卷装棉柔巾，以卷为单位装箱，面向家庭与商业洗护场景。":
        "Soft dry wipes supplied by the roll for personal care at home or in commercial settings.",
    "家庭装婴儿手口湿巾，采用翻盖设计，方便日常抽取。":
        "A family-size flip-top pack of baby hand and mouth wipes for everyday use.",
    "束口袋包装，单包重量为 210 克，适合家庭洗护场景。":
        "A 210 g drawstring bag for everyday personal care at home.",
    "采用原生木浆，折叠抽取，适合公共洗手间及商业空间使用。":
        "Folded, single-dispensing hand towels made from virgin wood pulp for public washrooms and commercial spaces.",
}

# Singular and plural display labels for the units that occur in pack and case
# quantities. Measure symbols keep the same spelling at every quantity.
UNITS = {
    "片": ("sheet", "sheets"), "张": ("sheet", "sheets"), "节": ("sheet", "sheets"),
    "抽": ("pull", "pulls"), "粒": ("compressed towel", "compressed towels"),
    "个": ("piece", "pieces"), "包": ("pack", "packs"), "卷": ("roll", "rolls"),
    "瓶": ("bottle", "bottles"), "桶": ("container", "containers"),
    "提": ("bundle", "bundles"), "组": ("set", "sets"), "盒": ("box", "boxes"),
    "件": ("case", "cases"), "箱": ("carton", "cartons"),
    "g": ("g", "g"), "kg": ("kg", "kg"),
}
QUANTITY = re.compile(r"(\d+(?: \+ \d+)?) (\w+)(?: / (\w+))?")
CHINESE = re.compile(r"[\u3400-\u9fff]")


def translate_field(value: str) -> str:
    """Translate one source field; raise on missing copy when building the site."""
    if value in TERMS:
        return TERMS[value]
    if not CHINESE.search(value):
        return value

    variant = re.fullmatch(r"(.+)（(.+)）", value)
    if variant:
        name, option = variant.groups()
        return f"{translate_field(name)} ({translate_field(option)})"

    if "，" in value:
        return ", ".join(translate_field(part) for part in value.split("，"))
    if " · " in value:
        return " · ".join(translate_field(part) for part in value.split(" · "))

    quantity = QUANTITY.fullmatch(value)
    if quantity:
        count, unit, per = quantity.groups()
        if unit == "层" and not per:
            return f"{count}-ply"
        if unit in UNITS and (not per or per in UNITS):
            display_unit = UNITS[unit][0 if count == "1" else 1]
            denominator = f" per {UNITS[per][0]}" if per else ""
            return f"{count} {display_unit}{denominator}"

    raise ValueError(f"Missing English catalogue translation for {value!r}")
