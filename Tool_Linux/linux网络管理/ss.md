## ss 主要用来管理 linux 中的网络套接字
```
-h, --help    帮助信息
-V, —version    程序版本信息
-n, —numeric    不解析服务名称
-r, —resolve        解析主机名
-a, —all    显示所有套接字(sockets)
-l, —listening    显示监听状态的套接字(sockets)
-o, —options        显示计时器信息
-e, —extended       显示详细的套接字(sockets)信息
-m, —memory         显示套接字(socket)的内存使用情况
-p, —processes    显示使用套接字(socket)的进程
-i, —info    显示 TCP内部信息
-s, —summary    显示套接字(socket)使用概况
-4, —ipv4           仅显示IPv4的套接字(sockets)
-6, —ipv6           仅显示IPv6的套接字(sockets)
-0, —packet            显示 PACKET 套接字(socket)
-t, —tcp    仅显示 TCP套接字(sockets)
-u, —udp    仅显示 UCP套接字(sockets)
-d, —dccp    仅显示 DCCP套接字(sockets)
-w, —raw    仅显示 RAW套接字(sockets)
-x, —unix    仅显示 Unix套接字(sockets)
-f, —family=FAMILY  显示 FAMILY类型的套接字(sockets)，FAMILY可选，支持  unix, inet, inet6, link, netlink-A, —query=QUERY, —socket=QUERYQUERY := {all|inet|tcp|udp|raw|unix|packet|netlink}[,QUERY]
-D, —diag=FILE     将原始TCP套接字(sockets)信息转储到文件
-F, —filter=FILE   从文件中都去过滤器信息 FILTER := [ state TCP-STATE ] [ EXPRESSION ]

```
## ss主要使用选项
```
-a, —all    显示所有套接字(sockets)
-e, —extended       显示详细的套接字(sockets)信息
-p, —processes    显示使用套接字(socket)的进程
-t, —tcp    仅显示 TCP套接字(sockets)
```