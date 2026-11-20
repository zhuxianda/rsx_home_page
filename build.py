"""Build the plain HTML pages. Run with Python 3 in this directory."""
from pathlib import Path
from urllib.parse import urlencode
from html import escape
from catalogue import PRODUCTS

ROOT = Path(__file__).resolve().parent / "dist"
COMPANY = "四川省如是欣生物科技有限公司"
ADDRESS = "四川省成都市大邑县青霞街道兴业七路29号"
MAP = "https://uri.amap.com/search?" + urlencode({"keyword": ADDRESS})
DOC = "assets/rushixin-profile.pdf"
ICONS = {
    "drop": '<path d="M12 2.7C9.4 6.4 5 10.8 5 15a7 7 0 0 0 14 0c0-4.2-4.4-8.6-7-12.3Z"/><path d="M8.7 14.6a3.6 3.6 0 0 0 3 3.6"/>',
    "factory": '<path d="M3 21V10l6 3V9l6 3V4h4l2 17H3Z"/><path d="M7 17h1m4 0h1m4 0h1"/>',
    "grid": '<rect x="3" y="3" width="7" height="7" rx="1.3"/><rect x="14" y="3" width="7" height="7" rx="1.3"/><rect x="3" y="14" width="7" height="7" rx="1.3"/><rect x="14" y="14" width="7" height="7" rx="1.3"/>',
    "chat": '<path d="M20.5 15a3 3 0 0 1-3 3h-7L5 21v-3H4.8a2.8 2.8 0 0 1-2.8-2.8V6.8A2.8 2.8 0 0 1 4.8 4h12.9a2.8 2.8 0 0 1 2.8 2.8Z"/><path d="M6.7 9h9M6.7 12.6H13"/>',
    "layers": '<path d="m12 3 9 5-9 5-9-5 9-5Zm-9 9 9 5 9-5M3 16l9 5 9-5"/>',
    "roll": '<ellipse cx="14" cy="9" rx="6.3" ry="6.3"/><circle cx="14" cy="9" r="1.9"/><path d="M7.7 8.9v5.6c0 2.1-1.2 3.2-3.4 3.2L2.5 21h12c3.3 0 5.8-2.3 5.8-6.1V9"/>',
    "award": '<circle cx="12" cy="9" r="6"/><path d="m8 14-1 7 5-3 5 3-1-7"/>',
    "loc": '<path d="M19.5 10c0 5.3-7.5 11.1-7.5 11.1S4.5 15.3 4.5 10a7.5 7.5 0 0 1 15 0Z"/><circle cx="12" cy="10" r="2.3"/>',
    "download": '<path d="M12 3v11m-4-4 4 4 4-4M4 15v5h16v-5"/>',
    "book": '<path d="M3 4.7C6.3 4 9 4.5 12 6.8 15 4.5 17.7 4 21 4.7v14.5c-3.3-.7-6-.2-9 2-3-2.2-5.7-2.7-9-2Zm9 2.1v14.4"/>',
    "copy": '<rect x="8" y="8" width="12" height="13" rx="2"/><path d="M16 7V3H3v13h4"/>',
    "menu": '<path d="M3 6h18M3 12h18M3 18h18"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "flask": '<path d="M9 3h6m-5 0v6l-6 9a2 2 0 0 0 1.7 3h12.6a2 2 0 0 0 1.7-3l-6-9V3M7 14h10"/>',
}
FAMILIES = {
    "wet": ("湿巾系列", "Wet wipes", "卫生护理、婴儿手口与家居清洁。", "baby"),
    "dry": ("棉柔巾系列", "Cotton soft wipes", "洗脸柔巾、抽取式与卷装棉柔巾。", "dry-facial"),
    "paper": ("生活用纸系列", "Tissue paper", "家庭用纸与商业空间纸品。", "kitchen-roll"),
    "care": ("清洁护理系列", "Home & personal care", "家居清洁与个人护理用品。", "p47-1"),
}
NAV = [("首页", "index.html"), ("产品中心", "products.html"), ("制造实力", "manufacturing.html"), ("关于如是欣", "about.html")]


def icon(key):
    return f'<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[key]}</svg>'


def brand():
    return '<a class="brand" href="index.html" aria-label="如是欣首页"><img src="assets/rsx.png" width="76" height="25" alt=""><span class="brand-type"><strong>如是欣</strong><small>RUSHIXIN BIOTECH</small></span></a>'


def btn(label, href, symbol=None, style=""):
    graphic = icon(symbol) if symbol else ""
    return f'<a class="button {style}" href="{escape(href, quote=True)}">{graphic}{label}</a>'


def label(en):
    return f'<div class="eyebrow" lang="en"><i></i>{en}</div>'


def header(active):
    def navlink(title, path):
        attr = ' aria-current="page"' if active == path else ''
        return f'<a href="{path}"{attr}>{title}</a>'
    links = "".join(navlink(*entry) for entry in NAV)
    return f'''<a class="skip" href="#main">跳至主要内容</a><header class="site-header"><div class="wrap header-inner">
    {brand()}<nav class="desktop-nav" aria-label="主导航">{links}</nav>
    <div class="nav-tools">{btn("商务合作", "business.html", "chat", "header-cta")}
    <details class="mobile-nav"><summary aria-label="主导航菜单">{icon("menu")}</summary><nav aria-label="移动端导航">{links}{navlink("商务合作","business.html")}</nav></details></div></div></header>'''


def footer():
    return f'''<footer><div class="wrap"><div class="footer-top"><div>{brand()}<p>{COMPANY}</p></div>
    <div class="footlinks"><a href="products.html">产品中心</a><a href="manufacturing.html">制造实力</a><a href="about.html">关于如是欣</a><a href="business.html">商务合作</a></div>
    </div><div class="footer-end"><span>© 2026 {COMPANY}</span><span>{icon("loc")} 四川 · 成都大邑</span></div></div></footer>'''


def write(filename, title, description, active, content):
    ROOT.mkdir(exist_ok=True)
    title = f"{title}｜如是欣" if filename != "index.html" else f"如是欣｜湿巾、棉柔巾与生活用纸专业制造"
    html = f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title><meta name="description" content="{escape(description, quote=True)}">
<meta name="theme-color" content="#fcfdfb"><link rel="icon" href="assets/favicon.png">
<link rel="stylesheet" href="styles.css"><script src="site.js" defer></script></head>
<body>{header(active)}<main id="main">{content}</main>{footer()}</body></html>'''
    (ROOT / filename).write_text(html, encoding="utf-8")


def stats():
    data = [("factory","4,500","m²","生产面积"),("layers","8","条","自动化生产线"),("roll","1,600","吨","无纺布年设计吞吐量"),("award","3","个","自有品牌")]
    return '<div class="stats">' + ''.join(f'<div class="stat"><span class="stat-icon">{icon(key)}</span><div><div class="number">{num}<small>{unit}</small></div><div class="stat-desc">{desc}</div></div></div>' for key,num,unit,desc in data) + '</div>'


def breadcrumbs(*items):
    parts = ['<a href="index.html">首页</a>']
    for name, path in items:
        parts.append(f'<a href="{path}">{name}</a>' if path else f'<span aria-current="page">{name}</span>')
    return '<nav class="crumbs" aria-label="面包屑">' + '<span aria-hidden="true">/</span>'.join(parts) + '</nav>'


def photosrc(slug, alt, cls="", lazy=True):
    loading = ' loading="lazy"' if lazy else ""
    return f'<img class="{cls}" src="assets/{slug}.webp" alt="{alt}"{loading} decoding="async">'


def banner():
    return f'''<section class="wrap cta-section"><div class="cta-band"><div>{label("OEM PARTNERSHIPS")}<h2>品牌定制与商用合作</h2><p>从品牌湿巾到餐饮定制湿毛巾，为不同使用场景匹配规格与包装。</p></div>
    {btn("了解合作方式","business.html","chat","on-dark")}</div></section>'''


def home():
    cards = ''.join(f'''<a class="family {key}" href="products-{key}.html">
    <div class="family-copy"><small lang="en">{en}</small><h3>{name}</h3><p>{desc}</p></div>
    <div class="family-art">{photosrc(photo,name+"产品包装")}</div><span class="open-icon">{icon("plus")}</span></a>''' for key,(name,en,desc,photo) in FAMILIES.items())
    html = f'''<section class="hero"><picture><source media="(max-width: 700px)" srcset="assets/cotton-mobile.webp"><img class="hero-image" src="assets/cotton-hero.webp" alt="棉柔巾层叠与珍珠纹理意象" fetchpriority="high"></picture>
    <div class="wrap hero-inner"><div class="hero-copy">
    <div class="hero-kicker">{icon("drop")} 专业清洁卫生用品制造商</div>
    <h1>一片柔软，<br><em>一份洁净。</em></h1>
    <p>如是欣专注湿巾、棉柔巾与生活用纸制造，<br class="desktop-only">为家庭日常护理与品牌定制提供多样选择。</p>
    <div class="actions">{btn("探索产品系列","products.html","grid")}{btn("了解制造实力","manufacturing.html","factory","outline")}</div>
    </div></div></section><section class="wrap stats-wrap" aria-label="企业实力数据">{stats()}</section>
    <section class="wrap section home-products"><div class="section-heading"><div>{label("PRODUCT COLLECTION")}<h2>产品系列</h2></div>
    <a class="text-link" href="products.html">{icon("grid")} 查看全部产品</a></div><div class="families">{cards}</div></section>
    <section class="factory-strip"><div class="wrap split"><div class="split-photo">{photosrc("line","如是欣湿巾自动生产线现场")}</div><div class="split-copy">
    {label("MANUFACTURING")}<h2>走进如是欣工厂</h2><p>在四川成都大邑，6 条湿巾自动生产线和 2 条棉柔巾自动生产线，承担从单片湿巾到多片家庭装的生产。</p>
    <p>工厂设有实验室，纸巾与湿巾生产取得 ISO 9001 质量管理体系认证。</p>{btn("查看工厂与资质","manufacturing.html",None,"outline")}</div></div></section>{banner()}'''
    write("index.html","",f"{COMPANY}，展示自有品牌湿巾、棉柔巾及生活用纸产品、制造实力与 OEM 定制业务。","index.html",html)


def product_card(p):
    title = escape(p.name)
    search_terms = " ".join((p.brand, p.name, p.item, p.barcode, p.client, p.channel, p.contents, p.size))
    subtitle = " · ".join(escape(value) for value in (p.size, p.contents) if value)
    item = f'<span class="item-code">{escape(p.item)}</span>' if p.item else ""
    return f'''<a class="product-card" href="product-{p.slug}.html"
    data-search="{escape(search_terms, quote=True)}" data-channel="{escape(p.channel, quote=True)}">
    <div class="product-art {p.family}">{photosrc(p.slug,p.brand+p.name+"包装")}</div>
    <div class="product-meta"><div class="card-brand"><small>{escape(p.brand)}</small>{item}</div>
    <h3>{title}</h3><p>{subtitle}</p></div></a>'''


def products(key=None):
    family = FAMILIES[key][0] if key else '全部产品'
    tabs = [(None, "全部产品")] + [(k, v[0]) for k, v in FAMILIES.items()]
    def tab(k, n):
        path = f"products-{k}.html" if k else "products.html"
        attr = ' aria-current="page"' if k == key else ''
        return f'<a href="{path}"{attr}>{n}</a>'
    links = ''.join(tab(k, n) for k, n in tabs)
    subset = [p for p in PRODUCTS if not key or p.family == key]
    channels = sorted({p.channel for p in subset}, key=("自有品牌", "其他品牌", "OEM 与定制", "商用纸品").index)
    options = ''.join(f'<option>{channel}</option>' for channel in channels)
    cards = ''.join(product_card(p) for p in subset)
    html = f'''<div class="page-intro"><div class="wrap">{breadcrumbs(("产品中心",None))}{label("PRODUCT CATALOGUE")}
    <h1>产品中心</h1><p>浏览自有品牌、OEM 定制及商用纸品。产品按图册顺序排列，可查看每款的包装、规格和图册原页。</p></div></div>
    <section class="wrap catalogue"><div class="catalogue-tools"><nav class="filters" aria-label="产品系列">{links}</nav>
    <a class="text-link" href="{DOC}" download>{icon("download")} 下载完整图册</a></div>
    <h2 class="sr-only">{family}</h2>
    <div class="catalogue-filter" hidden><label class="search-field"><span class="sr-only">在当前系列搜索产品</span>
    <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 5 5"/></svg>
    <input id="product-query" type="search" placeholder="搜索品牌、品名、货号或条码"></label>
    <select id="product-channel" aria-label="产品业务类型"><option value="">全部业务类型</option>{options}</select></div>
    <p class="result-count" role="status"><span id="visible-count">{len(subset)}</span> 个产品及包装规格</p>
    <div class="product-grid">{cards}</div><div class="empty-results" hidden><h3>没有匹配的产品</h3>
    <p>可以换个关键词，或清除条件后浏览当前系列。</p><button class="text-link" type="button">清除筛选</button></div></section>'''
    filename = f"products-{key}.html" if key else "products.html"
    write(filename,"产品中心" if not key else family,f"{family}包装、规格及装箱信息。","products.html",html)


def detail(p):
    family = FAMILIES[p.family][0]
    rows = [('所属业务', p.channel), ('品牌 / 系列', p.brand), ('合作项目', p.client),
            ('产品货号', p.item), ('尺寸 / 尺码', p.size), ('包装规格', p.contents),
            ('装箱规格', p.carton), ('材质', p.material), ('图册条码', p.barcode)]
    specs = ''.join(f'<div><dt>{key}</dt><dd>{escape(value)}</dd></div>' for key,value in rows if value)
    lead = f'<p class="lead">{escape(p.description)}</p>' if p.description else ''
    note = f'<p class="source-note">{escape(p.note)}</p>' if p.note else ''
    html = f'''<div class="wrap">{breadcrumbs(("产品中心","products.html"),(family,"products-"+p.family+".html"),(escape(p.name),None))}
    <section class="detail-grid"><div class="detail-art {p.family}">{photosrc(p.slug,p.brand+p.name+"包装",lazy=False)}</div>
    <div>{label(FAMILIES[p.family][1].upper())}<p class="product-brand">{escape(p.brand)}</p><h1>{escape(p.name)}</h1>{lead}
    <dl class="specs">{specs}</dl>{note}<a class="source-page text-link" href="{DOC}#page={p.page}">{icon("book")} 查看图册第 {p.page} 页</a>
    <div class="actions">{btn("商务合作","business.html","chat")}{btn("查看同系列","products-"+p.family+".html",None,"outline")}</div></div></section></div>'''
    write("product-"+p.slug+".html",p.brand+" · "+p.name,p.description or f"{p.brand}{p.name}的产品包装与规格，见公司图册第 {p.page} 页。","products.html",html)


def manufacturing():
    certs=[("license","营业执照"),("iso","质量管理体系认证证书"),("permit","消毒产品生产企业卫生许可证")]
    cert_html=''.join(f'<figure class="certificate"><a href="assets/{slug}.webp" aria-label="查看{name}大图">{photosrc(slug,name)}</a><figcaption>{name}</figcaption></figure>' for slug,name in certs)
    scenes = [
        ("process-unwinding", "产线放卷", "多组无纺布卷沿导辊送入生产设备"),
        ("process-fabric", "巾面纹理", "棉柔巾的纤维与珍珠纹在导辊上展开"),
        ("process-inspection", "厚度检测", "戴手套的技术人员使用测厚仪检查巾布样品"),
    ]
    gallery = ''.join(
        f'<div class="process-scene">{photosrc(slug, alt, lazy=False)}<span>{title}</span></div>'
        for slug, title, alt in scenes
    )
    html=f'''<div class="wrap">{breadcrumbs(("制造实力",None))}<section class="feature-hero manufacturing-hero"><div>{label("MANUFACTURING")}<h1>制造实力</h1><p class="lead">位于成都大邑工业园区的生产基地，集湿巾、棉柔巾自动化生产与实验室检测于一体。</p></div>
    <figure class="manufacturing-gallery"><div class="process-scenes">{gallery}</div><figcaption>工艺场景示意 · AI 生成</figcaption></figure></section>{stats()}</div>
    <section class="wrap section" id="production-and-testing"><div class="section-heading"><div>{label("INSIDE THE FACTORY")}<h2>生产与检测</h2></div><small class="process-image-note">配图为 AI 场景示意</small></div>
    <div class="process-grid"><article>{photosrc("automatic-wipe-folding","折叠成叠的湿巾沿自动化输送带排列前行")}<div><h3>自动化生产</h3><p>6 条湿巾生产线、2 条棉柔巾生产线，覆盖单片、多片及 80 片婴儿湿巾等包装规格。</p></div></article>
    <article>{photosrc("lab-wipe-microscopy","实验人员使用显微镜观察白色巾布样品")}<div><h3>厂内实验室</h3><p>配备实验操作空间与培养设备，支持卫生用品生产过程中的质量管理。</p></div></article></div></section>
    <section class="tinted"><div class="wrap section">{label("QUALITY MANAGEMENT")}<h2>企业资质</h2>
    <p class="intro-text">2023 年取得消毒产品生产企业卫生许可证，2024 年通过 ISO 9001:2015 质量管理体系认证，认证范围为卫生用品（纸巾、湿巾）的生产。</p>
    <div class="certs">{cert_html}</div></div></section>{banner()}'''
    write("manufacturing.html","制造实力","如是欣大邑制造基地的自动化生产线、厂内实验室及企业资质。","manufacturing.html",html)


def about():
    timeline=[("1996","成都华达生活用纸加工厂成立，开始在成都生产生活用纸。"),("2003","在成都郫都区成立成都市豪盛华达纸业有限公司。"),("2009","在大邑县成立成都市苏氏兄弟纸业有限公司。"),("2023","四川省如是欣生物科技有限公司成立，生产基地落户大邑工业园区。"),("2024","纸巾与湿巾生产通过 ISO 9001 质量管理体系认证。")]
    events=''.join(f'<li><strong>{year}</strong><p>{what}</p></li>' for year,what in timeline)
    html=f'''<div class="wrap">{breadcrumbs(("关于如是欣",None))}<section class="feature-hero about-feature"><div>{label("ABOUT RUSHIXIN")}<h1>关于如是欣</h1><p class="lead">{COMPANY}前身为成都豪盛华达纸业有限公司。我们的纸品制造历程始于 1996 年，今天在西岭雪山下的大邑工业园区，生产湿巾、棉柔巾与生活用纸。</p></div>
    <figure>{photosrc("campus","大邑生产基地示意图","feature-photo",False)}<figcaption>成都大邑 · 生产基地示意图</figcaption></figure></section></div>
    <section class="tinted"><div class="wrap section history"><div>{label("OUR HISTORY")}<h2>发展历程</h2></div><ol class="timeline">{events}</ol></div></section>
    <section class="wrap section"><div class="section-heading"><div>{label("OUR BRANDS")}<h2>三大自有品牌</h2></div></div>
    <div class="brand-grid"><article><h3>家必备</h3><p>涵盖卫生湿巾、婴儿手口湿巾、厨房湿巾与生活用纸。</p></article><article><h3>片片亲</h3><p>面向日常清洁与洗护，提供湿巾、洗脸柔巾与棉柔巾。</p></article><article><h3>晓宝</h3><p>以婴儿手口湿巾、卫生湿巾及亲肤棉柔巾服务家庭日常护理。</p></article></div></section>{banner()}'''
    write("about.html","关于如是欣","了解如是欣的成都纸品制造历程与三大自有品牌。","about.html",html)


def business():
    cases=[("oem-wipes","品牌 OEM","维邦卫生湿巾","180 × 180 mm，60 片装，55 g 平纹巾布。"),("oem-pharmacy","零售渠道定制","万华大药房定制湿厕纸","原生木浆材质，提供 40 片家庭装与 8 片便携装。"),("oem-dining","餐饮定制","餐厅独立装湿毛巾","250 × 250 mm 单片包装，按餐饮场景定制外袋。")]
    cards=''.join(f'<article class="case-card"><div class="case-image">{photosrc(slug,name)}</div><div><small>{kind}</small><h3>{name}</h3><p>{desc}</p></div></article>' for slug,kind,name,desc in cases)
    html=f'''<div class="page-intro"><div class="wrap">{breadcrumbs(("商务合作",None))}{label("OEM PARTNERSHIPS")}<h1>商务合作</h1><p>提供品牌 OEM 代工、零售渠道定制与商用纸品生产服务。</p></div></div>
    <section class="wrap section"><div class="section-heading"><div>{label("SELECTED PROJECTS")}<h2>定制案例</h2></div><a class="text-link" href="products.html?channel=OEM+%E4%B8%8E%E5%AE%9A%E5%88%B6">查看全部定制产品</a></div><div class="case-grid">{cards}</div></section>
    <section class="contact-area"><div class="wrap contact-grid"><div>{label("COMPANY ADDRESS")}<h2>公司地址</h2><p>{COMPANY}</p><address>{icon("loc")}<span id="address">{ADDRESS}</span></address>
    <div class="actions">{btn("在高德地图查看",MAP,"loc","outline")}<button class="text-link js-copy" type="button" hidden>{icon("copy")}<span>复制地址</span></button></div><p class="sr-only" id="copy-status" role="status"></p></div>
    <div class="download-card">{icon("book")}<h3>公司与产品图册</h3><p>浏览自有品牌、产品货号、装箱规格及更多定制案例。</p><a class="text-link" href="{DOC}" download>{icon("download")} 下载 PDF 图册 <small>75 页</small></a></div></div></section>'''
    write("business.html","商务合作","品牌 OEM 代工、零售与商用定制案例，公司地址及产品图册。","business.html",html)


if __name__ == "__main__":
    home()
    products()
    for key in FAMILIES:
        products(key)
    for product in PRODUCTS:
        detail(product)
    manufacturing()
    about()
    business()
