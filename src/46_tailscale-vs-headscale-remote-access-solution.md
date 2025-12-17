---
layout: post
title: Tailscale 与 Headscale 的区别：如何选择远程访问方案
slug: tailscale-vs-headscale-remote-access-solution
date: 2025-12-17 08:00
status: publish
author: Leslie
categories:
  - 未分类
tags:
  - 未标记
excerpt: 
---

如果你想在外面访问家里的电脑，或者让多个设备之间互相通信，**Tailscale** 是一个非常好的选择。不过在使用之前，你需要了解 Tailscale 和它的开源替代品 **Headscale** 之间的区别。

## Tailscale 是什么

Tailscale 是基于 **WireGuard** 协议的组网工具，通过 P2P（点对点）打洞技术让你的设备直接连接。

它的工作原理是这样的：

1. 两台设备都连接到 Tailscale 的控制服务器
2. 控制服务器交换双方的网络信息（IP、端口、NAT 类型等）
3. 设备之间尝试 P2P 直连
4. 如果直连失败，流量会通过 DERP 中继服务器转发

**重点**：如果双方都有 **公网 IPv6**，那么几乎可以 100% 直连成功，速度完全取决于你两端的网络质量。

### 关于速度

举个例子：你家里的宽带上传是 50Mbps，你在外面用手机连回家。这种情况下，你手机的下载速度最多就是 50Mbps，因为瓶颈在家里的上传速度。这个和用什么工具没关系，物理限制。

## Headscale 是什么

**Headscale** 是 Tailscale 控制服务器的开源实现。客户端还是用 Tailscale 官方的，只是把控制服务器换成自己搭建的。

### Tailscale vs Headscale 对比

| 对比项 | Tailscale 官方 | Headscale 自建 |
|--------|---------------|---------------|
| 控制服务器 | 官方托管 | 自己部署 |
| 设备数量 | 免费 100 台 | 无限制 |
| 用户数量 | 免费 3 人 | 无限制 |
| 数据安全 | 元数据经过官方 | 完全自控 |
| 维护成本 | 零维护 | 需要自己升级维护 |
| 服务器成本 | 免费 | 需要购买服务器 |

## Headscale 的坑

我之前部署过 Headscale，踩过一些坑：

### 1. 可以只用 IP 部署

网上有教程说必须用域名，其实不是。Headscale 可以只用 IP 部署

### 2. 服务器必须支持 IPv6

如果你想让设备之间 IPv6 直连，那你的 Headscale 服务器（DERP服务器）也必须有 IPv6。否则客户端拿不到对方的 IPv6 地址，就没法直连。

这点很重要，买服务器的时候要确认 IPv6 支持。

### 3. 建议部署 Web UI

Headscale 本身是命令行操作，设备授权、管理都要敲命令。建议部署一个 Web UI（比如 headscale-ui），这样在浏览器里就能完成授权操作，方便很多。

## 如何选择

### 适合用 Tailscale 官方的情况

- 个人使用，设备不超过 100 台
- 不想折腾服务器
- 能正常访问 Tailscale 服务（没被墙）

### 适合用 Headscale 的情况

- 公司/团队使用，设备数量多
- 对数据隐私有要求
- 愿意花时间维护
- Tailscale 官方被墙

## 我的选择

目前我用的是 Headscale。当时选择自建主要是担心官方服务不稳定。

不过现在回头看，作为个人用户，维护 Headscale 的成本其实挺高的。光是版本升级就要处理配置格式变化、数据库迁移等问题。

所以等现在的服务器到期后，我打算直接换成 **Tailscale 官方**。

原因很简单：

1. 我的设备都有 IPv6，可以直连，速度和自建一样
2. 直连成功后，DERP 服务器位置根本不重要
3. 省去维护成本，更省心

如果你也是个人使用，并且网络环境支持 IPv6 直连，推荐直接用 Tailscale 官方。省事。

[Tailscale 与 Headscale 的区别：如何选择远程访问方案](https://github.com/lesnolie/Marverick/issues/46)

