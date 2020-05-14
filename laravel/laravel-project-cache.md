# laravel (v5.8)项目缓存

## 目的：缓存自然主要是加快速度，优化用户体验

## 缓存种类

### 配置缓存

- 说明：把 config 文件夹里所有配置信息合并到一个文件里，减少运行时文件的载入数量(不会随着更新而自动重载)
- 配置：php artisan config:cache，缓存位置：bootstrap/cache/config.php
- 清理：php artisan config:clear

### 路由缓存

- 说明：可以有效的提高路由器的注册效率(不会随着更新而自动重载)
- 配置：php artisan route:cache，缓存位置：bootstrap/cache/routes.php
- 清理：php artisan route:cache
- 注意：路由缓存不支持路由匿名函数编写逻辑

### 类映射加载优化

- 说明：常用加载的类合并到一个文件里，通过减少文件的加载，来提高运行效率
- 缓存文件：bootstrap/cache/compiled.php 和 bootstrap/cache/services.json
- 配置：php artisan optimize --force
- 清理：php artisan clear-compiled
- 注意：此命令要运行在 php artisan config:cache 后，因为 optimize 命令是根据配置信息（如：config/app.php 文件的 providers 数组）来生成文件的。
- 更多：v5.8中 php artisan optimize:clear, 亲测效果，几乎清理了所有的缓存

	- Compiled views cleared!
	- Application cache cleared!
	- Route cache cleared!
	- Configuration cache cleared!
	- Compiled services and packages files removed!

*XMind: ZEN - Trial Version*