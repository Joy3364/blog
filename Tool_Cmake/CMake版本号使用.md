## 工程目录
```
.
├── build
│   ├── 省略
│   ├── HelloConfig.h
│   └── Makefile
├── CMakeLists.txt
├── HelloConfig.h.in
└── main.cpp
```
## CMakeLists.txt
```CMake
cmake_minimum_required(VERSION 2.8.9)    
project(Hello VERSION 1.0.0)
configfile(HelloConfig.h.in HelloConfig.h)

add_executable(Hello helloworld.cpp)    

target_include_directories(Hello PUBLIC
                            ${PROJECT_BINARY_DIR}
                            )
```

## HelloConfig.h.in
```cpp
#define Hello_VERSION_MAJOR @Hello_VERSION_MAJOR@
#define Hello_VERSION_MINOR @Hello_VERSION_MINOR@
#define Hello_VERSION_PATCH @Hello_VERSION_PATCH@
```
## main.cpp
```cpp
#include <iostream>
#include <HelloConfig.h>
int main(int argc, char** argv) {
    std::cout << "Hello, world!\n";
      if (argc < 2) {
    // report version
    std::cout << argv[0] << " Version " << Hello_VERSION_MAJOR << "."
              << Hello_VERSION_MINOR << "." << Hello_VERSION_PATCH << std::endl;
    std::cout << "Usage: " << argv[0] << " number" << std::endl;
    return 1;
  }
}
```

## 原理
cmake 在配置make过程中根据 *.in 文件生成 *.h 文件，在其中定义了版本号