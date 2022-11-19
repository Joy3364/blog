# linux进程相关概念
## 1. 程序与进程
进程是执行中的程序  
## 2. PID与PPID
PPID 父进程PID  
## 3. 进程的调用 fork and exec
一个进程调用另外一个进程，先复制自己（fork），再执行（exec）
## 4. 常驻进程 （服务）
daemon
## 5. 任务（jobs）
每个任务都是目前bash的子进程
## 6. 线程状态
## 7. pri与nice
pri优先级  
由于优先级不可以直接修改，需要为nice赋值，内核在合适的时候为进程切换优先级
newpri = oldpro + nice
root用户 nice -20~19  
普通用户 nice 0-19

# 进程/任务管理相关命令
## 1. 任务管理
```sh
* jobs    
    * -l 列出任务的pid  
    * -s 列出暂停的任务  
    * -r 列出运行的任务  

* fg %jobnumber 将任务放到前台执行    

* bg %jobnumber 任务后台继续执行  
``` 
## 2. kill
```sh
* kill -[] %jobnumber
    9 SIGKILL 强制终止
    1 SIGHUP 重启
    15 SIGTERM 正常退出
    19 SIGSTOP 暂停
    2 SIGINT 中断
* kill -[] PID
    同上
```
## 3. ps 静态查看进程
```sh
ps -l 查看本终端所有进程
ps aux 查看所有进程
ps -le 查看所有进程
```
## 4. top 动态查看进程

## 5. ctrl z/d/c
1. ctrl z 发送暂停信号
2. ctrl d 发送一个二进制值 EOF
3. ctrl c 发送强制终止信号
## 6. ‘&’ 后台任务
```sh
cmd & #表示命令放到后台执行，但是 stdin 与 stdout 还是会被刷新，故通常与 > 搭配使用 
```
## 7. nice与renice
```sh
nice -n nice值 任务 #新建任务，其优先级将会继承其bash
renice  nice值 PID #重新赋予nice值

