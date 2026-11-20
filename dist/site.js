const english = document.documentElement.lang === "en";
const languageSwitch = document.querySelector(".language-switch");

function syncLanguageLink() {
  if (!languageSwitch) return;
  const target = new URL(languageSwitch.href);
  target.search = location.search;
  target.hash = location.hash;
  languageSwitch.href = target.href;
}
syncLanguageLink();
window.addEventListener("hashchange", syncLanguageLink);
window.addEventListener("pageshow", syncLanguageLink);

const menu = document.querySelector(".mobile-nav");
if (menu) {
  document.addEventListener("click", (event) => {
    if (menu.open && !menu.contains(event.target)) menu.open = false;
  });
  document.addEventListener("keydown", (event) => {
    if (menu.open && event.key === "Escape") {
      menu.open = false;
      menu.querySelector("summary").focus();
    }
  });
}

const copyButton = document.querySelector(".js-copy");
if (copyButton && navigator.clipboard?.writeText) {
  copyButton.hidden = false;
  copyButton.addEventListener("click", async () => {
    const address = document.getElementById("address");
    const status = document.getElementById("copy-status");
    try {
      await navigator.clipboard.writeText(address.textContent.trim());
      copyButton.querySelector("span").textContent = english ? "Address copied" : "地址已复制";
      status.textContent = english ? "Company address copied to clipboard" : "公司地址已复制到剪贴板";
    } catch {
      const range = document.createRange();
      range.selectNodeContents(address);
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
      copyButton.querySelector("span").textContent = english ? "Copy selected address" : "请复制选中的地址";
      status.textContent = english ? "Address selected. Use your device’s copy command." : "地址已选中，可通过系统复制功能复制";
    }
  });
}

const filterBar = document.querySelector(".catalogue-filter");
if (filterBar) {
  const query = document.getElementById("product-query");
  const channel = document.getElementById("product-channel");
  const count = document.getElementById("visible-count");
  const empty = document.querySelector(".empty-results");
  const categoryLinks = document.querySelectorAll(".catalogue-tools .filters a");
  const url = new URL(window.location.href);
  const normalize = (value) => value.normalize("NFKC").toLowerCase().replace(/[\s·-]+/g, "");
  const cards = Array.from(document.querySelectorAll(".product-card"), (card) => ({
    node: card,
    terms: normalize(card.dataset.search),
    channel: card.dataset.channel,
    previousChannel: card.dataset.previousChannel,
  }));

  query.value = url.searchParams.get("q") || "";
  if (url.searchParams.get("channel") === "其他品牌") {
    channel.add(new Option(english ? "Other brands (now under OEM)" : "其他品牌（已归入代工 OEM）", "其他品牌"));
  }
  channel.value = url.searchParams.get("channel") || "";
  if (channel.selectedIndex < 0) channel.selectedIndex = 0;

  function withFilters(href) {
    const target = new URL(href);
    for (const [key, value] of [["q", query.value.trim()], ["channel", channel.value]]) {
      if (value) target.searchParams.set(key, value);
      else target.searchParams.delete(key);
    }
    return target;
  }

  function filterProducts(updateUrl) {
    const words = query.value.trim().split(/\s+/).map(normalize);
    let matched = 0;
    for (const card of cards) {
      const matches = (!channel.value || channel.value === card.channel || channel.value === card.previousChannel) &&
        words.every((word) => card.terms.includes(word));
      card.node.hidden = !matches;
      if (matches) matched++;
    }
    count.textContent = String(matched);
    empty.hidden = matched !== 0;
    for (const link of categoryLinks) link.href = withFilters(link.href).href;
    if (updateUrl && /^https?:$/.test(location.protocol)) {
      history.replaceState(history.state, "", withFilters(location.href));
      syncLanguageLink();
    }
  }

  filterBar.hidden = false;
  filterProducts(false);
  query.addEventListener("input", () => filterProducts(true));
  channel.addEventListener("change", () => filterProducts(true));
  empty.querySelector("button").addEventListener("click", () => {
    query.value = "";
    channel.selectedIndex = 0;
    filterProducts(true);
    query.focus();
  });
}
