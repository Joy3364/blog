## 1. 路由表详解
```sh
$ ip route
default via 192.168.0.1 dev enp4s0f1 onlink #该条指明默认网关
169.254.0.0/16 dev enp4s0f1 scope link metric 1000 
172.17.0.0/16 dev docker0 proto kernel scope link src 172.17.0.1 linkdown 
192.168.0.0/24 dev enp4s0f1 proto kernel scope link src 192.168.0.100 
# default   ：亦可以写为 0.0.0.0 指默认网关。一张路由表，默认网关只能有一个
# dev   ：指明ip包由哪个网口（网卡）发出。
# 目的地址  ：一条路由的主键，限定一条路由的其他修饰还包括 scope,metric,src,proto等
# scope ：指明该条路由的目的域：
#       host    ：同一主机，不必转发
#       link    ：在相同二级网络，可以不经网关直接通信
#       global  ：全局，需网关转发
# src   ：指明该路由源地址
# proto : 约束协议
# metric    ：花费
```
## 2. 路由规则
linux系统中可以有多张路由表，当进行路由时，根据路由规则选择不同的路由表  
路由规则有其优先级，最高为0，最低为32767，这意味着，路由规则最高32768条    
其中，linux有三张缺省的路由表，分别为local，main，default，缺省优先级分别为0，32766，32767  
```sh
$ ip rule
0:      from all lookup local #任意来源的ip包，去local中搜索
32766:  from all lookup main
32767:  from all lookup default
```
## 3. 路由表
linux中，每张路由表最多一个默认网关，  
路由表最多有256张，标号0-255，    
都存储在 /etc/iproute2/rt_tables，    
其中0，253，254，255已经被使用。   
```sh
$ less /etc/iproute2/rt_tables

255     local
254     main
253     default
0       unspec

# 添加路由表
$ echo "101 ChinaTel" >> /etc/iproute2/rt_tables
$ echo "102 ChinaCnc" >> /etc/iproute2/rt_tables
$ echo "103 ChinaEdu" >> /etc/iproute2/rt_tables
# 为路由表添加网关
$ ip route add default via 192.168.100.1 dev enp0s5 table ChinaTel
$ ip route add default via 192.168.110.1 dev enp0s6 table ChinaCnc
$ ip route add default via 192.168.120.1 dev enp0s7 table ChinaEdu
# 添加路由规则
$ ip rule add from 192.168.100.212 table ChinaTel
$ ip rule add from 192.168.110.212 table ChinaCnc
$ ip rule add from 192.168.120.212 table ChinaEdu
```

