## 1. 镜像基本知识
```sh
REPOSITORY：表示镜像的仓库源

TAG：镜像的标签

IMAGE ID：镜像ID

CREATED：镜像创建时间

SIZE：镜像大小

```
## 2. 镜像相关操作
```sh
#镜像本地查询
docker images 
#镜像获取
docker pull [res]:[tag]
#镜像云端查询
docker search [res]
#删除镜像
docker rmi hello-world
#为镜像添加tag
docker tag [id] runoob/centos:[tag]
#改名
docker tag [旧id] 新名
```
## 3. 镜像创建
```sh
# 从容器中创建
docker commit -m="描述信息" -a="作者" [容器id] [仓库:Tag]
# 使用dockerfile
dockerfile 
```
## 4. 镜像查询
```sh

```
## 5.镜像导入导出
```
docker load < nginx.tar
docker save -o nginx.tar nginx:latest
```