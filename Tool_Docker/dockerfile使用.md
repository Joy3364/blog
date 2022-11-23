## 1. 用途
Dockerfile 用于构建镜像
## 2. 用法
```sh
#Dockerfile 文件名必须为 Dockerfile ， build时只需要指明目录
docker build Dockerfile的目录路径 -t 仓库名:tag
```
## 3. Dockerfile命令与语法

1. FROM #指明来源包   
2. COPY #从主机复制文件到镜像
```docker
    COPY [--chown=<user>:<group>] <源路径1>...  <目标路径>
    COPY [--chown=<user>:<group>] ["<源路径1>",...  "<目标路径>"]
```
2. RUN #编译时运行命令  
```docker
    RUN <命令行命令>
    # <命令行命令> 等同于，在终端操作的 shell 命令。
    RUN ["可执行文件", "参数1", "参数2"]
    # 例如：
    # RUN ["./test.php", "dev", "offline"] 等价于 RUN ./test.php dev offline
```
3. CMD #运行时运行主线程，默认可以被覆盖  
```docker
    CMD <shell 命令> 
    CMD ["<可执行文件或命令>","<param1>","<param2>",...] 
    CMD ["<param1>","<param2>",...]  # 该写法是为 ENTRYPOINT 指令指定的程序提供默认参数
```
4. ENTRYPOINT #运行时运行主线程，默认不可以被覆盖 
```docker
# 可覆盖传参
# --entrypoint 用在命令行中会覆盖ENTRYPOINT
ENTRYPOINT ["<executeable>","<param1>","<param2>",...]
```
5. ENV #设置环境变量，全局有效  
```docker
ENV <key> <value>
ENV <key1>=<value1> <key2>=<value2>...
```
6. ARG #设置环境变量，仅在dockerfile内有效  
```docker
ARG <参数名>[=<默认值>]
```
7. 其他
```docker
VOLUME 
EXPOSE 
WORKDIR
USER
``` 


