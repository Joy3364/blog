## 开机启动服务目录
1. /etc/init.d/
2. /etc/rc.local 
3. /etc/rcn.d/
4. /etc/rcS.d/

## 区别
1. init.d 的目录里存放完整的服务启动项，需写好start，stop等函数，并配置依赖环境
2. rc.local 主要写可以即时结束的脚本，并不一定可用，需开启
3. rcn.d 代表内核启动系统的7个阶段，每个目录存放启动脚本的链接
4. rcS.d 最先启动，存放一些基本服务
5. 启动顺序 rcS.d -> rcn.d -> rc.local

## rc.local 的启动
1. systemctl status rc-local   #查看该服务有没有启动
2. touch /etc/rc.local         #创建脚本文件
3. chmod 755 rc.local
4. systemctl start rc-local    #开启此服务

## rc.local 样本  
```sh
#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.
...

exit 0
```

## init.d 脚本的启动
1. 在 /etc/init.d/ 下建立服务脚本
2. update-rc.d 脚本名 defaults #建立到rcn.d的软连接，并附加开机启动
3. update-rc.d [] remove #删除所有软链接
4. update-rc.d [] enable/disable #开机启动使能

## init.d 脚本范例
```sh
#!/bin/sh -e
### BEGIN INIT INFO
# Provides:          startMyUwsgiWeb
# Required-Start:   
# Required-Stop:
# Should-Start:      
# Default-Start: 2 3 4 5     
# Default-Stop:
# X-Interactive:     
# Short-Description: 
### END INIT INFO
case "$1" in
        start)
                case "$?" in
                        0|1) log_end_msg 0 ;;
                        2)   log_end_msg 1 ;;
                esac
                ;;
        stop)
                log_daemon_msg "Stopping $DESC" "$NAME"
                stop_nginx
                case "$?" in
                        0|1) log_end_msg 0 ;;
                        2)   log_end_msg 1 ;;
                esac
                ;;
        restart)
                log_daemon_msg "Restarting $DESC" "$NAME"
                # Check configuration before stopping nginx
                if ! test
                .......
exit 0     
***************************************************************
 
# Provides:          startMyUwsgiWeb    指明服务名，需唯一
# Required-Start:  $local_fs            启动此服务所依赖的服务             
# Required-Stop:                        关闭此服务所依赖的服务
# Should-Start:      
# Default-Start: 2 3 4 5                在那几个级别开启此服务
# Default-Stop:                         在》》》关闭》》》
# X-Interactive:     
# Short-Description:                    简短说明
```






