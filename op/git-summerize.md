# Git

@(Notes)

#### git checkout 
`git checkout -- file`，没有--，就变成了“切换到另一个分支”的命令
命令git checkout -- readme.txt意思就是，把readme.txt文件在工作区的修改全部撤销，这里有两种情况：
一种是readme.txt自修改后还没有被放到暂存区，现在，撤销修改就回到和版本库一模一样的状态；
一种是readme.txt已经添加到暂存区后，又作了修改，现在，撤销修改就回到添加到暂存区后的状态。
场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令git checkout -- file。
场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步第一步用命令git reset HEAD file，就回到了场景1，第二步按场景1操作
  > 总之，就是让这个文件回到最近一次git commit或git add时的状态

`git checkout <name> 切换分支：`




### git reset
写法：git reset [--hard|soft|mixed|merge|keep] [<commit>或HEAD]
功能：命令既可以回退版本，也可以把暂存区的修改回退到工作区
原理：将当前的分支重设（reset）到指定的<commit>或者HEAD（默认，如果不显示指定commit，默认是HEAD，即
最新的一次提交）
--hard：重设（reset） index和working directory，自从<commit>以来在working directory中的任何改变都﻿被丢弃，并把HEAD指向<commit>。
--soft：index和working directory中的内容不作任何改变，仅仅把HEAD指向<commit>。这个模式的效果是，执行完毕后，自从<commit>以来的所有改变都会显示在git status的"Changes to be committed"中。
--mixed:仅reset index，但是不reset working directory。

###git  checkout 与git reset区别
git checkout是把`工作区文件`回到最近一次git commit`或`git add时的状态
git reset 是使用`仓库区更新工作区和暂存区`


### git stash
??? 储存在当前分支还是针对所有分支都可见
切换分支时必须commit your changes or stash them before you switch branches.
保存当前工作进度，会把暂存区和工作区的改动保存起来。执行完这个命令后，在运行git status命令，就会发现当前是一个干净的工作区，没有任何改动。使用git stash save 'message...'可以添加一些注释

git stash list
显示保存进度的列表。也就意味着，git stash命令可以多次执行。

`git stash pop` [–index] [stash_id]
git stash pop 恢复最新的进度到工作区。git默认会把工作区和暂存区的改动都恢复到工作区。
`git stash pop --index` 恢复最新的进度到工作区和暂存区。（尝试将原来暂存区的改动还恢复到暂存区）
git stash pop stash@{1}恢复指定的进度到工作区。stash_id是通过git stash list命令得到的 
通过git stash pop命令恢复进度后，会删除当前进度。
git stash apply [–index] [stash_id]
除了不删除恢复的进度之外，其余和git stash pop 命令一样。

git stash drop [stash_id]
删除一个存储的进度。如果不指定stash_id，则默认删除最新的存储进度。

git stash clear
删除所有存储的进度。


#### git rebase
git rebase master 待实践



#### git cherry-pick
简单用法：
git cherry-pick <commit id>
注意：当执行完 cherry-pick 以后，将会生成一个新的提交；这个新的提交的哈希值和原来的不同，但标识名一样；


#### git log and git reflog 
http://wjp2013.github.io/tool/git-reflog-git-log-git-cherry-pick/