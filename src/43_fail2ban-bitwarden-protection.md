---
layout: post
title: 尝试使用 Fail2ban 保护 Bitwarden
slug: fail2ban-bitwarden-protection
date: 2025-12-12 08:00
status: publish
author: Leslie
categories: 
  - stand 
tags:
  - stand 
  - stand 
excerpt: 
---


原文链接：https://blog.mrchi.cc/posts/tryout-fail2ban/ 

## 什么是 Fail2ban？

Fail2ban 是一个开源工具，通过监视应用程序日志并使用正则表达式匹配，将多次登录失败的 IP 地址通过 iptables 规则进行封禁，用于防止暴力破解攻击，适合保护 Bitwarden 等密码管理器。[web:1]

## 安装 Fail2ban

在 Debian/Ubuntu 系统上：

```
apt install fail2ban
```


## 配置前的准备

在配置 Fail2ban 之前，确保服务的 `TZ`（时区）和 `IP_HEADER`（IP 头部）环境变量设置正确，以保证日志时间戳准确且记录真实访问 IP。[web:1]

## 创建过滤器

在 `/etc/fail2ban/filter.d` 目录下创建 `bitwarden.local`：

```
[INCLUDES]
before = common.conf

[Definition]
failregex = ^.*Username or password is incorrect\. Try again\. IP: <ADDR>\. Username:.*$
ignoreregex =
```
[web:1]

该过滤器用于匹配 Bitwarden 日志中的失败登录尝试。[web:1]

## 创建 Jail

在 `/etc/fail2ban/jail.d` 目录下创建 `bitwarden.local`：

```
[bitwarden]
enabled   = true
port      = 80,443
name      = bitwarden
filter    = bitwarden
banaction = iptables-multiport
logpath   = /root/bitwarden-data/bitwarden.log
maxretry  = 3
bantime   = 14400
findtime  = 14400
```


如果实际监听端口不是 80 和 443，请相应修改 `port`，否则封禁规则不会作用在真实服务端口上。[web:1]

## 重启 Fail2ban

```
systemctl restart fail2ban
```


## 测试配置

故意输入错误密码，然后查看 Jail 状态中记录数是否增加：

```
fail2ban-client status bitwarden
```


当失败次数达到 3 次后，当前 IP 应被封禁，无法访问相应端口。[web:1]

## 解封 IP

```
fail2ban-client set bitwarden unbanip <IP_ADDRESS>
```


[尝试使用 Fail2ban 保护 Bitwarden](https://github.com/lesnolie/Marverick/issues/43)

