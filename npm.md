# npm

## 是什么？

### 全称 Node Package Manager，即node包管理器，维基https://zh.wikipedia.org/wiki/Npm

## 配置 ：`package.json`与lockfile(锁文件) 

### 目的，`生成相同的 node_modules`

### 为什么需要lockfile?

- 达成目的，存在两个主要问题，1.npm 不同版本的安装算法不一致 2.依赖包和依赖包的依赖的更新

### `package.json`与lockfile(锁文件)是什么？

- package.json文件，定义了这个项目所需要的各种模块，以及项目的配置信息
- lockfile, 锁文件，一般包括 package-lock.json 或 npm-shrinkwrap.json，以记录实际安装的各个package的具体来源和版本号

### `配合使用`

- 如果没有lockfile, npm i会生成一个
- 两者兼容，根据localfile 下载
- 两者不兼容，会根据package.json下载，并更新lockfile

### 参考，https://juejin.im/post/5d40f9a4e51d45620821ce30，https://www.zhihu.com/question/62331583

## 安装

### npm install

- 整体安装，不加后缀直接安装，如果node_modules存在，就不再重新安装了，即使有新，也是如此, -f 强制重新安装
- 单独包安装，npm install <package name>  安装模块的特定版本 use @

### npm ci

- 特点，整体安装，适合安装干净依赖的情况，快速，更严格，依赖于完整的配置，不会修改文件
- 原理，根据 package-lock.json 去安装确定的依赖，package.json 只是用来验证是不是有不匹配的版本，若有则报错

## 常用功能与命令

### 查看包版本npm list

- -g 全局，默认当前项目下的所有模块以及依赖
- npm list packagename 查看单独模块

### 切换镜像

- 临时使用，npm --registry https://registry.npm.taobao.org install express
- 永久使用，npm config set registry https://registry.npm.taobao.org(验证npm config get registry)
- 通过cnpm，npm install -g cnpm --registry=https://registry.npm.taobao.org
-  问题，使用cnpm install 之后的东西不受lockfile 控制，有点坑

*XMind: ZEN - Trial Version*