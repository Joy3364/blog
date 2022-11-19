## 1 安装合适的qtcreator
    参考 http://c.biancheng.net/view/3851.html    
## 2 安装cmake 
    版本  3.23
## 3 环境变量设置  
    cmake bin目录  
    编译器 bin目录  
    qt工具 bin目录   E:\IDETools\QT\5.14.2\mingw73_64\bin  
    qt编译器 bin目录（非必要） E:\IDETools\QT\Tools\mingw730_64\bin
## 4 创建一个qt工程
    编译系统选择cmake（而非qmake）  
    正确的qtcreator才有build-system的选项
## 5 编辑CMakeLists.txt文件
### 5.1 理解自动生成的CMakeLists.txt文件的前几行
    set(CMAKE_AUTOUIC ON) #使用qt uic工具，把ui文件转为.cpp文件
    set(CMAKE_AUTOMOC ON) #使用qt moc工具，将qt扩展的c++转换为标准c++ 
    set(CMAKE_AUTORCC ON)
### 5.2 设置包路径
    set(CMAKE_PREFIX_PATH "E:/IDETools/QT/5.14.2/mingw73_64/lib/cmake/Qt5/")  
    ****************************************************************  
    #主要是寻找 .cmake 文件。    
    
    find_package(Qt5 COMPONENTS Widgets REQUIRED)  
    ****************************************************************
    #参考(https://blog.csdn.net/zhanghm1995/article/details/105466372)  
    
### 5.3 程序运行带黑框问题
     add_executable(pro_hello_qt WIN32 [文件]  
     ****************************************************************
     参考 https://www.jianshu.com/p/19765d4932a4  

## 6 缺少dll文件问题
    1 windeployqt [程序名]
    2 qt工具 bin目录   E:\IDETools\QT\5.14.2\mingw73_64\bin  环境变量添加


