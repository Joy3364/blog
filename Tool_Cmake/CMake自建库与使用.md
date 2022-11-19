## 生成静态或动态库（shared or static）
```
project(directory_test)

include_directories(include)

file(GLOB SOURCES "src/*.cpp")

add_library(testStudent SHARED ${SOURCES})
```
## 使用库
cmake_minimum_required(VERSION 2.8.9)
project (TestLibrary)

set ( PROJECT_LINK_LIBS libtestStudent.so )

link_directories( ~/exploringBB/extras/cmake/studentlib_shared/build )

include_directories(~/exploringBB/extras/cmake/studentlib_shared/include)

add_executable(libtest libtest.cpp)

target_link_libraries(libtest ${PROJECT_LINK_LIBS} )