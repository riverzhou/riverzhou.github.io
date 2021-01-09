---
layout: post
title: 搭建 Github Pages Jekyll 环境  
author: River 
category: 教程
tags:  
  - Github 
  - Jekyll 
  - 教程 
---

本地搭建一个和 Github Pages 
全兼容的 Jekyll 系统  
全面设置 Jekyll 的各种参数
评估与选择主题

<!-- more -->

---
* toc  
{:toc}

## 1. 安装 Ruby 环境    

- 测试视频    

<iframe src="//player.bilibili.com/player.html?aid=970473760&bvid=BV1Ap4y1z7ML&cid=260666207&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>


## 2. 站点的 Gemfile 设置    
Gemfile
```ruby
source 'https://mirrors.ustc.edu.cn/rubygems/'

gem 'github-pages' , group: :jekyll_plugins  
gem 'wdm' if Gem.win_platform?
```

```bash
bundle install  # 安装依赖软件包  
bundle update github-pages  # 更新依赖软件包  
```

## 3. 站点的 _config.yml 配置    
_config.yml
```yml
theme: jekyll-theme-modernist

title: 落雪的随笔小屋
author: 'River Zhou'

plugins:
  - jemoji
  - jekyll-paginate
  - jekyll-sitemap
  - jekyll-feed
  - jekyll-seo-tag
  - jekyll-redirect-from
  - jekyll-avatar
  - jekyll-mentions

kramdown:
  input: GFM
```

添加 `JEKYLL_GITHUB_TOKEN` 到环境变量 (token去github网站上申请) 

```bash
bundle exec jekyll b  # 只生成页面
bundle exec jekyll s  # 生成页面并启动 WebServer
```

## 4. 设置 IIS 环境    


## 5. 主题选择    
- jekyll-theme-modernist
*速度挺快，界面挺和谐，记事本风格，手机屏优化*    

![modernist](https://riverzhou2000.gitee.io/images/images/modernist_1.png 'modernist_1')  
![modernist](https://riverzhou2000.gitee.io/images/images/modernist_2.png 'modernist_2')  

- jekyll-theme-hacker
*速度很快，配色很有质感*    

![hacker](https://riverzhou2000.gitee.io/images/images/hacker.png 'hacker')  

- jekyll-theme-cayman
*速度很快，中庸风格， Banner 太大*    

![cyman](https://riverzhou2000.gitee.io/images/images/cayman.png 'cyman')  

- jekyll-theme-midnight
*用了 jQuery 加载很慢，配色不错， Banner 很扎眼*    

![midnight](https://riverzhou2000.gitee.io/images/images/midnight.png 'midnight')  

## 6. 图床    
- [x] gitee
- [x] github

---

