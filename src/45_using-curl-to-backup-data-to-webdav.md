---
layout: post
title: 使用 curl 备份数据到 WebDAV
slug: using-curl-to-backup-data-to-webdav
date: 2025-12-13 08:00
status: publish
author: Leslie
categories:
  - 未分类
tags:
  - 未标记
excerpt: 
---

在 VPS 部署有状态的小项目时，数据备份是常见需求。可以借助 curl，将打包后的数据上传到支持 WebDAV 的云存储服务，并结合 cron 实现每日自动备份。

本文以坚果云为例。确保已启用 WebDAV 并准备好用户名与专用密码。

在 `/etc/cron.daily` 创建脚本 `bitwarden-backup`：

```bash
#!/bin/sh
set -e

filename="bitwarden-`date +%F`.tar.gz"

cd /opt/bitwarden
tar czf "${filename}" bitwarden-data/

curl -u "USERNAME:APP_PASSWD" -T "${filename}" \
  "https://dav.jianguoyun.com/dav/bitwarden/"

rm "${filename}"
```

赋予执行权限：

```bash
chmod a+x /etc/cron.daily/bitwarden-backup
```

建议将凭据存放于受限权限的配置文件，或改用 `curl --netrc-file` 避免明文写入脚本。

参考链接：[使用 curl 备份数据到 WebDAV](https://blog.mrchi.cc/posts/backup-to-webdav-by-curl/)

[使用 curl 备份数据到 WebDAV](https://github.com/lesnolie/Marverick/issues/45)

