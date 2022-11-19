## 1. 运行/创建容器
```sh
docker run [docker_para] [res:image_name] [cmd] [cmd_para] 
# docker_para
    -t 指定终端 
    -i 允许交互
    -d 后台运行
    -p: 指定端口映射，格式为：主机(宿主)端口:容器端口
    --net="bridge": 指定容器的网络连接类型，支持 bridge/host/none/container: 四种类型；
    --priviledged #指定特权模式，此模式下，容器内root以真root模式运行
    --name="" 为容器指定名字
# 实例
    #从images中创建容器并运行
    docker run ubuntu:15.10 /bin/echo "Hello world" 
    #进入容器交互式终端
    docker run -i -t ubuntu:15.10 /bin/bash 
    #后台运行
    docker run -d ubuntu:15.10 /bin/sh -c "while true; do echo hello world; sleep 1; done" 
```

## 2. 停止容器
```sh
    docker stop [id]
```

## 3. 查询容器状态
```sh
    docker ps [-a]
        -a 全部容器
```

## 4. 进入运行中的容器
```sh
    #退出后中断容器
    docker attach [id] 
    #不会中断容器
    docker exec -it [id] [shell_name] 
```

## 5. 导入导出容器
```sh
    #导出
    docker export [id] > ubuntu.tar 
    #导入
    docker import [OPTIONS] file|URL|- [REPOSITORY[:TAG]]
    #实例
    #文件导入
    cat docker/ubuntu.tar | docker import - test/ubuntu:v1 
    #文件导入2
    docker import ubuntu.tar test/ubuntu:v1 
    #URL导入
    docker import http://example.com/exampleimage.tgz example/imagerepo 
```

## 7. 删除容器
```sh
    docker rm -f [id]
```