# 如是欣官网

官网地址为 [rsx.rushixinbio.com](https://rsx.rushixinbio.com/)。

## 修改与本地预览

在仓库根目录使用 Python 3 构建页面。页面模板在 `build.py`，产品数据在 `catalogue.json`，样式、脚本、图片和 PDF 在 `dist/`。

```sh
python3 build.py
python3 -m http.server 8000 --directory dist
```

打开 `http://localhost:8000/` 查看效果，将改动提交并推送到 GitHub 的 `main` 分支。

## 更新线上版本

登录 VPS 后运行以下命令。

```sh
rsx-deploy
```

部署命令会以 `rsx-web` 用户从 GitHub 拉取 `main`，在独立目录构建，检查主要页面和图册，再将 `/srv/rsx-site/current` 切换至新版本。它会输出已发布的完整提交号。同步或构建失败时，当前版本会继续提供访问。重复运行可核对并发布同一提交，并发运行会按顺序执行。

在 VPS 上可用 `readlink /srv/rsx-site/current` 查看正在提供服务的版本。需要回退时，可在本地用 `git revert` 撤销有问题的提交，推送后再运行 `rsx-deploy`。

## 服务器配置

服务器的检出目录是 `/srv/rsx-site/repo`，使用公开仓库的 HTTPS 地址只读拉取。命令入口由 `ops/rsx-deploy` 安装至 `/usr/local/bin/rsx-deploy`，每次更新都会使用仓库里的 `ops/build-release`。

Caddy 使用 `/etc/caddy/Caddyfile` 提供静态文件，并通过公网 80 端口申请和自动续期 Let's Encrypt 证书。域名的 HTTPS 流量由公网入口转至本机 18443 端口。若修改 `ops/Caddyfile`，需在 VPS 上单独验证、安装配置并重新加载 Caddy。
