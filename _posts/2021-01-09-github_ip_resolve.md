---
layout: post
title: 解析 raw.githubusercontent.com  
author: River 
category: 教程
tags:  
  - Github 
  - DNS 
  - 教程  
---

Github 的一些功能失效，比如  
raw.githubusercontent.com 不能访问  
图片和头像不能显示  
gist 功能不能使用  
问题的本质是 DNS 污染

<!-- more -->

---
* toc  
{:toc}

## 1. 问题的起源  

Github 的一些功能失效，比如  
- raw.githubusercontent.com 不能访问 
- 图片和头像不能显示 
- gist 功能不能使用  

问题的本质是 DNS 污染

## 2. 解决方案  

### 2.1. 正确解析 IP

在 https://www.ipaddress.com/ 上正确解析如下域名  
```
github-cloud.s3.amazonaws.com
gist.github.com
api.github.com
assets-cdn.github.com
github.githubassets.com
raw.githubusercontent.com  
favicons.githubusercontent.com
gist.githubusercontent.com
cloud.githubusercontent.com
avatars0.githubusercontent.com
avatars2.githubusercontent.com
avatars1.githubusercontent.com
avatars3.githubusercontent.com
camo.githubusercontent.com
user-images.githubusercontent.com
```

### 2.2 把正确的 ip 写入 hosts 文件

#### 2.2.1 hosts 文件的位置 

Windows
```
C:\Windows\System32\drivers\etc\hosts 
```

Linux
```
/etc/hosts 
```

### 2.2.2 host 文件内容

添加如下内容  
```
52.216.128.147  github-cloud.s3.amazonaws.com
52.74.223.119   gist.github.com
54.169.195.247  api.github.com
185.199.111.153 assets-cdn.github.com
185.199.109.154 github.githubassets.com
199.232.96.133  raw.githubusercontent.com  
199.232.96.133  favicons.githubusercontent.com
199.232.96.133  gist.githubusercontent.com
199.232.96.133  cloud.githubusercontent.com
199.232.96.133  avatars0.githubusercontent.com
199.232.96.133  avatars2.githubusercontent.com
199.232.96.133  avatars1.githubusercontent.com
199.232.96.133  avatars3.githubusercontent.com
199.232.96.133  camo.githubusercontent.com
199.232.96.133  user-images.githubusercontent.com
```

### 2.2.3 时效性  

`2021-01-09`  
全部有效 :ok_hand::+1:  
以后会不定期更新  

---
