## 1. 容器运行
```sh
docker run [docker_para] [image_name] [cmd] [cmd_para] 
 
[docker_para]
    -t 指定终端 
    -i 允许交互
    -d 后台运行

#   1. 一次性运行  
    docker run ubuntu:15.10 /bin/echo "Hello world" 
#   2. 交互式bash  
    docker run -i -t ubuntu:15.10 /bin/bash   
    ctrl+d or exit 退出
#   3. 后台运行  
    docker run -d ubuntu:15.10 /bin/sh -c "while true; do echo hello world; sleep 1; done" 
```
## 2. 容器查询

```
docker ps
    -a 全部容器
```

## 3. 容器停止
```
    docker stop [id]  
```

## 4. 进入容器
```sh
    docker attach [id] #退出后中断容器
    docker exec -it [id] [shell_name] #不会中断容器
```
## 5. 导入导出容器
```sh
#导出
    docker export 1e560fca3906 > ubuntu.tar 
#导入
    #文件导入
    cat docker/ubuntu.tar | docker import - test/ubuntu:v1 
    #文件导入2
    docker import ubuntu.tar test/ubuntu:v1 
    #URL导入
    docker import http://example.com/exampleimage.tgz example/imagerepo 
```
## 6. 容器删除
```sh
    docker rm -f [id]
```


