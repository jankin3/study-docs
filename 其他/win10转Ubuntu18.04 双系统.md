# win10添加Ubuntu18.04 双系统

五一期间组装了一个台式机,主要用途是准备在家日常使用。本来只装了win10，然后意外就来了，五一之后由于公司的原因失业了。暂时没有个人电脑来coding，就直接在win10的基础上装了ubuntu18.04，这里记录一下，个人配置

> cpu amd 3500x
>
> 主板 迫击炮
>
> 显卡 蓝宝石580
>
> 机箱 先马m7
>
> 电源酷冷至尊GX450
>
> 内存 金士顿 2666 8*2



### 一. 为新系统腾出空间

在磁盘分区里面为Ubuntu腾出`未分配空间`，大概50+g足够，我分配了150G

###  二. 用软碟通将ubuntu的镜像写入 U 盘

本地下载了ubuntu镜像然后使用软碟通写入u盘

### 三. 进入bios，类似装win10， 选择使用制作好的u盘

### 四. 正常进入之后，开始配置

这里需要注意的是，在选择安装ubuntu的时候选择其他选项，也就是自定义安装。因为已经有了win10了，默认安装可能会混乱。

开始手动分区的步骤，选择空闲分区，也就是最开始在win10中腾出来的未分配部分

1. efi：这个就是实现你双系统的原因了，这个就是用启动 ubuntu 的目录，里面会有系统的引导，这个文件其实只有几十兆，但是我们建议将其划分为 200M 文件格式为efi，这个分区必不可少，否则后果你懂得！

   > 这里网上教程有的是按照/boot 分配的，我看了一下原理几乎一样，就是一个启动的分区

   只要保证下面启动的位置选择efi 或者/boot即可

2. swap:这个是 Linux 也就是 ubuntu 的交换区目录，这个一般的大小为内存的 2 倍左右，主
3. /:这是 linux 也就是 ubuntu 的根目录
4. /home:这是 ubuntu的其他盘，相当于windows的其他盘，所以为了让我们自己的目录大一点，剩下的全分给它，文件格式为 ext4



基本流程结束了。下面就是踩坑了

1. 开机直接进入win10， 没有选择界面

   试了网上的大多数解决方案，最终

   解决方案：bcdedit /set "{bootmgr}" path \EFI\ubuntu\grubx64.efi

   此命令的意思是大概是修改启动管理器bootmgr,到了新的路径之下

2. 网络

   我的设备是外部usb无线网卡，进入系统之后一直没网，按照网上说的按照我的无线网卡的型号各种安装驱动最终还是不行，最终买了一个支持ubuntu的无线网卡。



参考：https://www.cnblogs.com/masbay/p/10745170.html



