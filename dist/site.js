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
      copyButton.querySelector("span").textContent = "地址已复制";
      status.textContent = "公司地址已复制到剪贴板";
    } catch {
      const range = document.createRange();
      range.selectNodeContents(address);
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
      copyButton.querySelector("span").textContent = "请复制选中的地址";
      status.textContent = "地址已选中，可通过系统复制功能复制";
    }
  });
}
