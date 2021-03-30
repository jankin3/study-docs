# linux文件系统

## 文件属性

### 设计思想

- 索引式文件系统. 读取文件的时候读取inode中的block 位置之后可以一口气直接找到所有的block。这里对比U盘的FAT系统需要一个个读取，因为每个block 文件里面记录着下一个block的位置，相比而言会比较慢

### 主要部分

- boot sector, superblock, inode bitmap, block bitmap, inode table, data block

### 文件 系统主要信息

- `superblock`, 记录整个文件系统的整体信息
- `inode`, 文件的权限与属性,一个文件占用一个inode, 以及block 的位置
- `block`, 数据区块, 记录文件的实际存储数据

## 目录树

### 目录和文件类似，每个目录都有一个inode 和block, inode记录的目录的属性和权限，block记录的是目录下的文件名以及文件的inode

## 日志式文件系统

### 目的:数据一致性检查

### 实现:多出一块记录区，随时记载文件系统的主要活动，可加快系统复原时间；

## 常用命令

### df

- 目的:列出文件系统的整体磁盘使用量
- 常用

	- -h 显示各文件系统的容量
	- -i -h 显示各文件系统inode使用情况

### du

- 评估文件系统的磁盘使用量
- du -h --max-depth=1 计算当前目录下的文件或者目录的大小，包括子目录

*XMind: ZEN - Trial Version*