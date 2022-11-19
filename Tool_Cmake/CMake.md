# CMAKE 基本使用

## 变量
```
############################################################
#创建变量
set(name value)
############################################################
#引用变量
${ValueName}
############################################################
```
## 基本架构
```
cmake_minimum_required(VERSION 2.8.9)    
project(hello)    
add_executable(hello helloworld.cpp)    
```
## 全局包含与局部包含
```
############################################################
include_directories("path")
target_include_directories(main.out PUBLIC
                            "${PROJECT_SOURCE_DIR}/include_part")
############################################################
include_directories("path") 必须在add_executable()前使用
target_include_directories 在add_executable()后使用
```
## 多文件编译
```
cmake_minimum_required(VERSION 2.8.9)
project(directory_test)

include_directories(include)

file(GLOB SOURCES "src/*.cpp")

add_executable(testStudent ${SOURCES})
```
## 生成静态或动态库（shared or static）
```
############################################################
project(directory_test)

include_directories(include)

file(GLOB SOURCES "src/*.cpp")

add_library(testStudent SHARED ${SOURCES})
############################################################
库生成在build的子目录下，如同lib****.so
```
## 使用库
```
############################################################
cmake_minimum_required(VERSION 2.8.9)
project (TestLibrary)

set ( PROJECT_LINK_LIBS libtestStudent.so )

link_directories( ~/exploringBB/extras/cmake/studentlib_shared/build )

include_directories(~/exploringBB/extras/cmake/studentlib_shared/include)

add_executable(libtest libtest.cpp)

target_link_libraries(libtest ${PROJECT_LINK_LIBS} )
############################################################
库名可以为lib****.so,也可以直接为***
```
## 总工程与子工程
```
############################################################
# 总 CMakeLists.txt
cmake_minimum_required(VERSION 3.0.0)
project(HELLOCMAKE VERSION 0.1.0)
include_directories("include_global")

file(GLOB SRC "./src/*.cpp")

add_subdirectory("shared_lib")

add_executable(main.out ${SRC})

target_include_directories(main.out PUBLIC
                            "${PROJECT_SOURCE_DIR}/include_part")

target_link_directories(main.out PUBLIC
                            "${PROJECT_BINARY_DIR}/shared_lib")

target_link_libraries(main.out pt2)
############################################################
# 子 CMakeLists.txt
add_library(pt2 SHARED pt2)
############################################################
```
## 常用变量
```
1. CMAKE_BINARY_DIR
   PROJECT_BINARY_DIR
   <projectname>_BINARY_DIR
   这三个变量指代的内容是一致的,如果是 in source 编译,指得就是工程顶层目录,如果是 out-of-source 编译,指的是工程编译发生的目录。PROJECT_BINARY_DIR 跟其他指令稍有区别,现在,你可以理解为他们是一致的。

2. CMAKE_SOURCE_DIR
   PROJECT_SOURCE_DIR
   <projectname>_SOURCE_DIR
   这三个变量指代的内容是一致的,不论采用何种编译方式,都是工程顶层目录。
也就是在 in source 编译时,他跟 CMAKE_BINARY_DIR 等变量一致。
PROJECT_SOURCE_DIR 跟其他指令稍有区别,现在,你可以理解为他们是一致的。

3. CMAKE_CURRENT_SOURCE_DIR
   指的是当前处理的 CMakeLists.txt 所在的路径,比如上面我们提到的 src 子目录。

4. CMAKE_CURRRENT_BINARY_DIR
   如果是 in-source 编译,它跟 CMAKE_CURRENT_SOURCE_DIR 一致,如果是 out-of-source 编译,他指的是 target 编译目录。
   使用我们上面提到的 ADD_SUBDIRECTORY(src bin)可以更改这个变量的值。
   使用 SET(EXECUTABLE_OUTPUT_PATH <新路径>)并不会对这个变量造成影响,它仅仅修改了最终目标文件存放的路径。

5. CMAKE_CURRENT_LIST_FILE
   输出调用这个变量的 CMakeLists.txt 的完整路径

6. CMAKE_CURRENT_LIST_LINE
   输出这个变量所在的行

7. CMAKE_MODULE_PATH
   这个变量用来定义自己的 cmake 模块所在的路径。如果你的工程比较复杂,有可能会自己编写一些 cmake 模块,这些 cmake 模块是随你的工程发布的,为了让 cmake 在处理CMakeLists.txt 时找到这些模块,你需要通过 SET 指令,将自己的 cmake 模块路径设置一下。
   比如
   SET(CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)
   这时候你就可以通过 INCLUDE 指令来调用自己的模块了。

8. EXECUTABLE_OUTPUT_PATH 和 LIBRARY_OUTPUT_PATH
   分别用来重新定义最终结果的存放目录,前面我们已经提到了这两个变量。

9. PROJECT_NAME
   返回通过 PROJECT 指令定义的项目名称。
```