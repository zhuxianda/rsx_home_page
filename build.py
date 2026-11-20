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
DOC_PAGES = 75
CONTACT_NAME = "苏宏"
CONTACT_DISPLAY = "136 7908 6363"
CONTACT_TEL = "tel:" + CONTACT_DISPLAY.replace(" ", "")
# Keep these anchors stable for links from the existing product catalogue.
PARTNERS = {
    "自由点": ("freemore", "自由点"),
    "维邦": ("vip-paper", "维邦纸业"),
    "柔贝佳": ("roubeijia", "柔贝佳"),
    "阳阳纸业": ("happy-flowers", "阳阳纸业 · 开心朵朵"),
    "桔子姑娘": ("juziguniang", "桔子姑娘"),
    "洁柔": ("c-and-s", "洁柔"),
    "厮磨工坊": ("simo", "厮磨工坊"),
    "雅思": ("oulu", "雅思 · 欧露"),
    "百惠": ("baihui", "百惠 · 柔康莱"),
    "美乐美妆连锁": ("meile", "美乐美妆连锁 · 谜库"),
    "万华大药房": ("wanhua", "万华大药房 · 卿易舒"),
    "汇鑫源·休闲庄": ("huixinyuan", "汇鑫源·休闲庄"),
    "食锦荟": ("shijinhui", "食锦荟"),
}
# Public captions follow the artwork. Product pages retain the printed catalogue names.
PARTNER_CAPTIONS = {"雅思": "雅诗纸业 · 鸥露", "汇鑫源·休闲庄": "汇鑫苑·休闲庄"}
MARK_NAMES = {"阳阳纸业": "开心朵朵", "雅思": "鸥露", "百惠": "柔康莱",
              "美乐美妆连锁": "谜库", "万华大药房": "万华大药房"}


ICONS = {
    "drop": '<path d="M12 2.7C9.4 6.4 5 10.8 5 15a7 7 0 0 0 14 0c0-4.2-4.4-8.6-7-12.3Z"/><path d="M8.7 14.6a3.6 3.6 0 0 0 3 3.6"/>',
    "factory": '<path d="M3 21V10l6 3V9l6 3V4h4l2 17H3Z"/><path d="M7 17h1m4 0h1m4 0h1"/>',
    "grid": '<rect x="3" y="3" width="7" height="7" rx="1.3"/><rect x="14" y="3" width="7" height="7" rx="1.3"/><rect x="3" y="14" width="7" height="7" rx="1.3"/><rect x="14" y="14" width="7" height="7" rx="1.3"/>',
    "phone": '<path d="m5.8 3 3 4.7-1.9 2.2a15 15 0 0 0 7.2 7.2l2.2-1.9 4.7 3c-.6 2.1-2 3-4.1 2.6C9.7 19.5 4.5 14.3 3.2 7.1 2.8 5 3.7 3.6 5.8 3Z"/>',
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
NAV = [("首页", "index.html"), ("OEM 代工", "oem.html"), ("产品中心", "products.html"), ("制造实力", "manufacturing.html"), ("关于如是欣", "about.html")]


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
    <div class="nav-tools">{btn("合作洽谈", "business.html", "chat", "header-cta")}
    <details class="mobile-nav"><summary aria-label="主导航菜单">{icon("menu")}</summary><nav aria-label="移动端导航">{links}{navlink("合作洽谈","business.html")}</nav></details></div></div></header>'''


def footer():
    return f'''<footer><div class="wrap"><div class="footer-top"><div>{brand()}<p>{COMPANY}</p><a class="footer-phone" href="{CONTACT_TEL}">OEM 业务联系 · {CONTACT_NAME}　{CONTACT_DISPLAY}</a></div>
    <div class="footlinks"><a href="oem.html">OEM 代工</a><a href="products.html">产品中心</a><a href="manufacturing.html">制造实力</a><a href="about.html">关于如是欣</a><a href="business.html">合作洽谈</a></div>
    </div><div class="footer-end"><span>© 2026 {COMPANY}</span><span>{icon("loc")} 四川 · 成都大邑</span></div></div></footer>'''


def write(filename, title, description, active, content):
    ROOT.mkdir(exist_ok=True)
    title = f"{title}｜如是欣" if filename != "index.html" else f"如是欣｜湿巾、棉柔巾 OEM 代工与品牌定制"
    html = f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title><meta name="description" content="{escape(description, quote=True)}">
<meta name="theme-color" content="#fcfdfb"><link rel="icon" href="assets/favicon.png">
<link rel="stylesheet" href="styles.css"><script src="site.js" defer></script></head>
<body>{header(active)}<main id="main">{content}</main>{footer()}</body></html>'''
    (ROOT / filename).write_text(html, encoding="utf-8")


def stats():
    data = [("factory","4,500","m²","生产面积"),("layers","8","条","自动化生产线"),("roll","1,600","吨","无纺布年设计吞吐量"),("award","500","万元","固定资产投入")]
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
    return f'''<section class="wrap cta-section"><div class="cta-band"><div>{label("BUSINESS ENQUIRIES")}<h2>洽谈您的 OEM 项目</h2><p>沟通产品用途、材质、每包片数与采购数量。业务联系人为{CONTACT_NAME}。</p></div>
    {btn("电话 "+CONTACT_DISPLAY,CONTACT_TEL,"phone","on-dark")}</div></section>'''


def partner_caption(key):
    return PARTNER_CAPTIONS.get(key, PARTNERS[key][1])


def partner_wall(linked=False):
    tiles = []
    # Retain category anchors in older links while showing only brand identities.
    old_anchors = {"美乐美妆连锁": "retail-work", "汇鑫源·休闲庄": "hospitality-work"}
    for key, (anchor, _) in PARTNERS.items():
        caption = partner_caption(key)
        mark = MARK_NAMES.get(key, caption)
        alt = "" if mark == caption else mark + "标识"
        caption_id = f' id="{old_anchors[key]}"' if not linked and key in old_anchors else ""
        tile = f'<img src="assets/brand-{anchor}.webp" alt="{alt}" loading="lazy"><span{caption_id}>{caption}</span>'
        if linked:
            tiles.append(f'<li><a class="partner-mark" href="oem.html#{anchor}">{tile}</a></li>')
        else:
            tiles.append(f'<li id="{anchor}"><div class="partner-mark">{tile}</div></li>')
    group_id = "" if linked else ' id="brand-work"'
    return f'<ul class="cooperation-marks"{group_id}>{"".join(tiles)}</ul>'


def partner_strip():
    return f'''<section class="partner-section"><div class="wrap"><div class="partner-heading">
    <h2>合作品牌与客户</h2><a class="text-link" href="oem.html">了解 OEM 服务</a></div>
    {partner_wall(linked=True)}</div></section>'''


def home():
    html = f'''<section class="hero oem-home-hero"><picture><source media="(max-width: 700px)" srcset="assets/oem-samples-mobile.webp"><img class="hero-image" src="assets/oem-samples-hero.webp" alt="成卷巾材、翻盖湿巾和单片袋装的包装形式示意" fetchpriority="high"></picture>
    <div class="wrap hero-inner"><div class="hero-copy"><div class="hero-kicker">{icon("factory")} 四川成都 · 卫生用品制造</div>
    <h1>湿巾与棉柔巾<br><em>OEM 代工</em></h1>
    <p>为品牌、零售渠道与餐饮客户定制生产。<br class="desktop-only">从单片独立装到家庭多片装，按使用场景匹配材质与包装。</p>
    <div class="actions">{btn("了解 OEM 代工","oem.html","factory")}{btn("洽谈定制需求","business.html","chat","outline")}</div>
    </div></div></section>{partner_strip()}
    <section class="factory-strip"><div class="wrap"><div class="split home-works"><div class="split-photo">{photosrc("line","成都大邑基地湿巾生产线现场")}</div><div class="split-copy">
    {label("MANUFACTURING BASE")}<h2>成都大邑生产基地</h2><p>6 条湿巾自动生产线与 2 条棉柔巾自动生产线，承接单片湿巾、多片湿巾及棉柔巾生产。纸巾与湿巾生产已通过 ISO 9001 质量管理体系认证。</p>
    <div class="actions factory-actions">{btn("查看生产能力与资质","manufacturing.html",None,"outline")}<a class="text-link" href="about.html#operations">了解经营投入</a></div></div></div>{stats()}</div></section>
    <section class="wrap range-links"><div><h2>产品与规格</h2><p>查看定制产品、自有品牌及商用纸品的详细规格。</p></div><nav aria-label="产品系列">{''.join(f'<a href="products-{key}.html">{data[0]}</a>' for key,data in FAMILIES.items())}<a href="products.html">全部产品</a></nav></section>{banner()}'''
    write("index.html","",f"{COMPANY}主营湿巾、棉柔巾 OEM 代工，提供品牌、零售及餐饮定制。了解合作品牌、工厂产能与业务联系方式。","index.html",html)


def oem():
    html = f'''<section class="partnership-hero" aria-labelledby="oem-title">
    <picture class="sample-display"><source media="(max-width: 920px)" srcset="assets/oem-packaging-mobile.webp" width="1000" height="582">
    <img src="assets/oem-packaging-panorama.webp" width="2079" height="756" alt="独立小袋、便携湿巾袋和家庭翻盖装的无品牌包装示意" fetchpriority="high" decoding="async"></picture>
    <div class="wrap partnership-inner"><div class="partnership-copy">
    <p class="partnership-kicker">湿巾与棉柔巾 <span>·</span> 成都大邑</p>
    <h1 id="oem-title"><span lang="en">OEM</span> 品牌代工</h1>
    <p class="partnership-lead">为品牌、零售与餐饮客户定制生产。<br>可选单片独立装、便携袋装与家庭翻盖装。</p>
    <div class="actions">{btn("联系 OEM 业务","business.html","chat")}<a class="partner-jump" href="#portfolio">查看合作品牌</a></div>
    </div></div></section>
    <div class="partnership-facts"><dl class="wrap">
    <div><dt>生产面积</dt><dd>4,500 <small>m²</small></dd></div>
    <div><dt>自动化生产线</dt><dd>8 <small>条</small></dd></div>
    <div><dt>固定资产投入</dt><dd>500 <small>万元</small></dd></div>
    </dl></div>
    <section class="wrap partner-gallery" id="portfolio" aria-labelledby="partner-title">
    <h2 id="partner-title">合作品牌与客户</h2>
    {partner_wall()}
    </section>
    <section class="oem-services"><div class="wrap service-layout"><div class="service-photo">{photosrc("automatic-wipe-folding","自动化输送带上整齐排列的折叠巾片")}</div>
    <div class="service-copy"><h2>OEM 定制能力</h2><dl>
    <div><dt>巾材与纹理</dt><dd>按清洁场景选择巾材、克重与表面纹路。</dd></div>
    <div><dt>尺寸与装量</dt><dd>根据使用习惯确定单张尺寸、每包片数及组合装量。</dd></div>
    <div><dt>成品包装</dt><dd>可沟通单片独立装、便携袋装及家庭多片装等形式。</dd></div>
    </dl><a class="text-link" href="manufacturing.html">{icon("factory")} 查看生产与检测能力</a></div></div></section>
    {banner()}'''
    write("oem.html", "OEM 品牌代工", "如是欣湿巾与棉柔巾 OEM 代工服务、合作品牌、生产能力及业务联系方式。", "oem.html", html)


def product_card(p):
    title = escape(p.name)
    fields = [p.brand, p.name, p.item, p.barcode, p.client, p.channel, p.contents, p.size]
    if p.channel == "OEM 与定制":
        key = p.client or p.brand
        fields.extend((PARTNERS[key][1], partner_caption(key)))
    search_terms = " ".join(fields)
    subtitle = " · ".join(escape(value) for value in (p.size, p.contents) if value)
    item = f'<span class="item-code">{escape(p.item)}</span>' if p.item else ""
    channel_label = " · OEM 定制" if p.channel == "OEM 与定制" else ""
    return f'''<a class="product-card" href="product-{p.slug}.html"
    data-search="{escape(search_terms, quote=True)}" data-channel="{escape(p.channel, quote=True)}">
    <div class="product-art {p.family}">{photosrc(p.slug,p.brand+p.name+"包装")}</div>
    <div class="product-meta"><div class="card-brand"><small>{escape(p.brand)}{channel_label}</small>{item}</div>
    <h3>{title}</h3><p>{subtitle}</p></div></a>'''


def products(key=None):
    family = FAMILIES[key][0] if key else '全部产品'
    tabs = [(None, "全部产品")] + [(k, v[0]) for k, v in FAMILIES.items()]
    def tab(k, n):
        path = f"products-{k}.html" if k else "products.html"
        attr = ' aria-current="page"' if k == key else ''
        return f'<a href="{path}"{attr}>{n}</a>'
    links = ''.join(tab(k, n) for k, n in tabs)
    subset = sorted((p for p in PRODUCTS if not key or p.family == key), key=lambda p: p.channel != "OEM 与定制")
    channels = sorted({p.channel for p in PRODUCTS}, key=("自有品牌", "其他品牌", "OEM 与定制", "商用纸品").index)
    options = ''.join(f'<option>{channel}</option>' for channel in channels)
    cards = ''.join(product_card(p) for p in subset)
    html = f'''<div class="page-intro"><div class="wrap">{breadcrumbs(("产品中心",None))}{label("PRODUCT CATALOGUE")}
    <h1>产品中心</h1><p>优先展示 OEM 代工与渠道定制产品。也可按系列查看自有品牌和商用纸品，核对包装、规格及图册原页。</p><a class="text-link catalogue-projects" href="oem.html#portfolio">{icon("book")} 查看合作品牌</a></div></div>
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
    partner_link = ""
    if p.channel == "OEM 与定制":
        anchor, _ = PARTNERS[p.client or p.brand]
        partner_link = f'<a href="oem.html#{anchor}" class="text-link">查看合作品牌</a>'
    rows = [('所属业务', p.channel), ('品牌 / 系列', p.brand), ('合作项目', p.client),
            ('产品货号', p.item), ('尺寸 / 尺码', p.size), ('包装规格', p.contents),
            ('装箱规格', p.carton), ('材质', p.material), ('图册条码', p.barcode)]
    specs = ''.join(f'<div><dt>{key}</dt><dd>{escape(value)}</dd></div>' for key,value in rows if value)
    lead = f'<p class="lead">{escape(p.description)}</p>' if p.description else ''
    note = f'<p class="source-note">{escape(p.note)}</p>' if p.note else ''
    html = f'''<div class="wrap">{breadcrumbs(("产品中心","products.html"),(family,"products-"+p.family+".html"),(escape(p.name),None))}
    <section class="detail-grid"><div class="detail-art {p.family}">{photosrc(p.slug,p.brand+p.name+"包装",lazy=False)}</div>
    <div>{label(FAMILIES[p.family][1].upper())}<p class="product-brand">{escape(p.brand)}</p><h1>{escape(p.name)}</h1>{lead}
    <dl class="specs">{specs}</dl>{note}<div class="detail-references">{partner_link}<a class="source-page text-link" href="{profile_url(p.page)}">{icon("book")} 查看图册第 {p.page} 页</a></div>
    <div class="actions">{btn("洽谈 OEM 定制","business.html","chat")}{btn("查看同系列","products-"+p.family+".html",None,"outline")}</div></div></section></div>'''
    write("product-"+p.slug+".html",p.brand+" · "+p.name,p.description or f"{p.brand}{p.name}的产品包装与规格，见公司图册第 {p.page} 页。","products.html",html)


def profile_url(page):
    return f"profile-{page}.html"


def profile_pages():
    for page in range(1, DOC_PAGES + 1):
        image = f"assets/profile-pages/page-{page}.jpg"
        previous = f'<a href="{profile_url(page - 1)}" rel="prev">上一页</a>' if page > 1 else '<span aria-disabled="true">上一页</span>'
        following = f'<a href="{profile_url(page + 1)}" rel="next">下一页</a>' if page < DOC_PAGES else '<span aria-disabled="true">下一页</span>'
        page_title = f"图册第 {page} 页"
        html = f'''<section class="wrap brochure-reader">{breadcrumbs(("产品中心","products.html"),(page_title,None))}
        <div class="brochure-heading"><h1>公司与产品图册</h1><a class="text-link" href="{DOC}" download>{icon("download")} 下载原版 PDF</a></div>
        <nav class="brochure-pager" aria-label="图册翻页">{previous}<strong>第 {page} 页 / 共 {DOC_PAGES} 页</strong>{following}</nav>
        <a class="brochure-sheet" href="{image}" aria-label="查看第 {page} 页原尺寸图像"><img src="{image}" width="1440" height="810" alt="公司与产品{page_title}"></a>
        </section>'''
        write(profile_url(page), page_title, f"在线查看如是欣公司与产品{page_title}。", "products.html", html)


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
    html=f'''<div class="wrap">{breadcrumbs(("制造实力",None))}<section class="feature-hero manufacturing-hero"><div>{label("MANUFACTURING")}<h1>制造实力</h1><p class="lead">成都大邑工业园区设有湿巾与棉柔巾自动生产线及厂内实验室，支持品牌代工所需的单片、多片和家庭装生产。</p><a href="oem.html#portfolio" class="text-link catalogue-projects">查看合作品牌</a></div>
    <figure class="manufacturing-gallery"><div class="process-scenes">{gallery}</div></figure></section>{stats()}</div>
    <section class="wrap section" id="production-and-testing"><div class="section-heading"><div>{label("INSIDE THE FACTORY")}<h2>生产与检测</h2></div></div>
    <div class="process-grid"><article>{photosrc("automatic-wipe-folding","折叠成叠的湿巾沿自动化输送带排列前行")}<div><h3>自动化生产</h3><p>6 条湿巾生产线、2 条棉柔巾生产线，覆盖单片、多片及 80 片婴儿湿巾等包装规格。</p></div></article>
    <article>{photosrc("lab-wipe-microscopy","实验人员使用显微镜观察白色巾布样品")}<div><h3>厂内实验室</h3><p>配备实验操作空间与培养设备，支持卫生用品生产过程中的质量管理。</p></div></article></div></section>
    <section class="tinted"><div class="wrap section">{label("QUALITY MANAGEMENT")}<h2>企业资质</h2>
    <p class="intro-text">2023 年取得消毒产品生产企业卫生许可证，2024 年通过 ISO 9001:2015 质量管理体系认证，认证范围为卫生用品（纸巾、湿巾）的生产。</p>
    <div class="certs">{cert_html}</div></div></section>{banner()}'''
    write("manufacturing.html","制造实力","支撑 OEM 代工的大邑基地、设备投入、生产线、厂内实验室及企业资质。","manufacturing.html",html)


def about():
    timeline=[("1996","成都华达生活用纸加工厂成立，开始在成都生产生活用纸。"),("2003","在成都郫都区成立成都市豪盛华达纸业有限公司。"),("2009","在大邑县成立成都市苏氏兄弟纸业有限公司。"),("2023","四川省如是欣生物科技有限公司成立，生产基地落户大邑工业园区。"),("2024","纸巾与湿巾生产通过 ISO 9001 质量管理体系认证。")]
    events=''.join(f'<li><strong>{year}</strong><p>{what}</p></li>' for year,what in timeline)
    html=f'''<div class="wrap">{breadcrumbs(("关于如是欣",None))}<section class="feature-hero about-feature"><div>{label("ABOUT RUSHIXIN")}<h1>关于如是欣</h1><p class="lead">{COMPANY}前身为成都豪盛华达纸业有限公司。团队的纸品制造历程始于 1996 年。如今，我们在成都大邑以品牌 OEM 代工为主营业务，同时经营家必备、片片亲和晓宝三个自有品牌。</p></div>
    <figure>{photosrc("campus","大邑生产基地示意图","feature-photo",False)}<figcaption>成都大邑 · 生产基地示意图</figcaption></figure></section></div>
    <section class="operations-band" id="operations"><div class="wrap section">{label("OPERATING CAPACITY")}<h2>经营与投入</h2>
    <div class="operating-facts"><article><strong>500 <small>万元</small></strong><h3>固定资产投入</h3><p>大邑基地生产面积 4,500 平方米，配置 8 条自动化生产线。</p></article>
    <article><strong>1,600 <small>吨 / 年</small></strong><h3>设计无纺布吞吐量</h3><p>湿巾与棉柔巾生产并行，适配品牌客户的不同包装规格。</p></article>
    <article><strong>4,000 <small>万元</small></strong><h3>设计产能可达产值</h3><p>公司图册按设计产能列示的可达产值。</p></article></div><a class="text-link" href="{profile_url(3)}">{icon("book")} 查看图册经营资料</a></div></section>
    <section class="tinted"><div class="wrap section history"><div>{label("OUR HISTORY")}<h2>发展历程</h2></div><ol class="timeline">{events}</ol></div></section>
    <section class="wrap section"><div class="section-heading"><div>{label("OUR BRANDS")}<h2>三大自有品牌</h2></div></div>
    <div class="brand-grid"><article><h3>家必备</h3><p>涵盖卫生湿巾、婴儿手口湿巾、厨房湿巾与生活用纸。</p></article><article><h3>片片亲</h3><p>面向日常清洁与洗护，提供湿巾、洗脸柔巾与棉柔巾。</p></article><article><h3>晓宝</h3><p>以婴儿手口湿巾、卫生湿巾及亲肤棉柔巾服务家庭日常护理。</p></article></div></section>{banner()}'''
    write("about.html","关于如是欣","了解如是欣的成都纸品制造历程与三大自有品牌。","about.html",html)


def business():
    html = f'''<div class="oem-intro"><div class="wrap">{breadcrumbs(("合作洽谈",None))}
    <div class="oem-intro-grid business-intro"><div>{label("BUSINESS ENQUIRIES")}<h1>OEM 合作洽谈</h1>
    <p class="lead">品牌代工、渠道专供或餐饮定制，均可直接联系业务负责人。已有目标产品的客户，可以带上图册货号或包装规格沟通。</p>
    <a class="text-link catalogue-projects" href="oem.html#portfolio">{icon("book")} 查看合作品牌</a></div>
    <div class="business-card" id="contact"><span>OEM 业务联系人</span><h2>{CONTACT_NAME}</h2>
    <a class="business-phone" href="{CONTACT_TEL}" aria-label="拨打{CONTACT_NAME}的业务电话 {CONTACT_DISPLAY}">{icon("phone")}{CONTACT_DISPLAY}</a></div></div></div></div>
    <section class="wrap section">{label("PROJECT BRIEF")}<h2>洽谈时可提供的信息</h2>
    <div class="spec-options"><article><h3>产品与用途</h3><p>说明品牌与使用场景，例如门店零售、随赠护理品或餐厅独立装湿毛巾。</p></article>
    <article><h3>巾材与包装</h3><p>提供意向材质、单张尺寸、每包片数及包装形式，也可参考图册中的案例或货号。</p></article>
    <article><h3>采购与交付</h3><p>提供预计采购量、收货地区和期望交货时间，便于双方讨论项目安排。</p></article></div></section>
    <section class="contact-area"><div class="wrap contact-grid"><div>{label("COMPANY ADDRESS")}<h2>成都大邑生产基地</h2><p>{COMPANY}</p><address>{icon("loc")}<span id="address">{ADDRESS}</span></address>
    <div class="actions">{btn("在高德地图查看",MAP,"loc","outline")}<button class="text-link js-copy" type="button" hidden>{icon("copy")}<span>复制地址</span></button></div><p class="sr-only" id="copy-status" role="status"></p></div>
    <div class="download-card">{icon("book")}<h3>公司与产品图册</h3><p>第 55–71 页收录品牌代工与定制项目的包装、材料和规格。</p>
    <div class="brochure-links"><a class="text-link" href="{profile_url(1)}">{icon("book")} 在线阅览</a><a class="text-link" href="{DOC}" download>{icon("download")} 下载 PDF 图册 <small>{DOC_PAGES} 页</small></a></div></div></div></section>'''
    write("business.html","OEM 合作洽谈",f"联系{COMPANY}业务负责人{CONTACT_NAME}，沟通湿巾、棉柔巾与纸品 OEM 项目。","business.html",html)


if __name__ == "__main__":
    home()
    oem()
    products()
    for key in FAMILIES:
        products(key)
    for product in PRODUCTS:
        detail(product)
    profile_pages()
    manufacturing()
    about()
    business()
