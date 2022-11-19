## systemctl （以下两个命令的整合）
1. service
2. chkconfig

## systemd 主要命令
1. systemctl list-units     列出所有运行的服务
2. systemctl list-unit-files 查看所有服务是否能开机启动
3. systemctl enable/disable sshd  修改服务为开机启动
4. systemctl list-dependencies sshd 查看依赖关系
  
