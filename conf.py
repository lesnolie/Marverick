# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 30
template ={
    "name": "Galileo",
    "type": "local",
    "path": "../MyTheme/Galileo/" # could also use relatetive path to Maverick
}
enable_jsdelivr = {
    "enabled": False,
    "repo": "lesnolie/Marverick@gh-pages"
}

# 站点设置
site_name = "不愧不忘"
site_logo = "${static_prefix}logo.jpg"
site_build_date = "2021-03-29T16:51+08:00"
author = "LESLIE"
email = "lesliezhang08@gmail.com"
author_homepage = "https://blog.lesliemm.xyz"
description = "我喜欢猫"
key_words = ['ilxyz', 'LESLIE']
language = 'zh-CN'
external_links = [
    {
        "name": "",
        "url": "",
        "brief": ""
    },
    {
        "name": "",
        "url": "",
        "brief": ""
    }
]
nav = [
    {
        "name": "",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
   ]
social_links = [
    {
        "name": "",
        "url": "",
        "icon": ""
    },
    {
        "name": "",
        "url": "",
        "icon": ""
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
