# 以boost库为例
## 1. 编译boost库
```sh
# boost库安装目录结构
# C:\Users\Loner\8888\env\Cpp\CppPackage\boost
.
├── abicheck.sh
├── include
├── lib
├── vms_gtk2.opt
├── vms_gtk.opt
├── vms.opt
└── vms_x11_univ.opt
```
## 2. find_package()
```
三种模式
    
1. module 模式
    目标： Find<PackageName>.cmake
    文件来源： 由CMake官方提供，或者项目自己编写find模块
    搜索顺序：  
            a. CMAKE_ MODULE_PATH
            b. CMake自带 find*.cmake (*\share\cmake-3.23\Modules\)

2. config 模式
    目标：<lowercasePackageName>-config.cmake or <PackageName>Config.cmake
    文件来源：由第三方库自己提供.cmake文件
    搜索方式：根据环境变量与CMake变量生成匹配路径，进行搜索
    PREFIX生成：  
        a. <PackageName>_ROOT (环境变量或CMake变量) 
        b. CMAKE_PREFIX_PATH，CMAKE_FRAMEWORK_PATH，CMAKE_APPBUNDLE_PATH(CMake变量)
        c. <PackageName>_DIR，CMAKE_PREFIX_PATH，CMAKE_FRAMEWORK_PATH，CMAKE_APPBUNDLE_PATH (环境变量)
        d. 使用命令选项HINTS指定的目录
        e. 标准环境变量PATH
        f. CMake User Package Registry
        g. 平台特定CMAKE_SYSTEM_PREFIX_PATH，CMAKE_SYSTEM_FRAMEWORK_PATHCMAKE_SYSTEM_APPBUNDLE_PATH，例如linux：/usr/local,windows：c:/program file等
        h. CMake System Package Registry
        i. 使用命令选项PATHS指定的目录

3. FetchContent redirection 模式
    略
```
## 3. include
```sh
# find_package()会自动配置一些 CMake 变量，例如 PackageName_INCLUDE_DIRS 等
# 使用如下目录包含头文件
include_directories(${Boost_INCLUDE_DIRS})
```



