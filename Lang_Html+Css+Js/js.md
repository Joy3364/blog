# 1.js数据类型
## 1.1 声明变量
```js
var name = ""; //变量可以在声明前使用（变量提升），可重复声明
let name = "";  //不可重复声明
const name = "";  //值不可改变
```
## 1.2 变量类型
1. 值类型  
   string,  
   number,  
   boolean,  
   null,  
   undefined,  
   symbol
2. 引用类型  
   object,   
   array,  
   function
# 2.js流程控制
```
for (var x in list){
    pass;
}

```
# 3.js函数
```js
function test_fun(){

}

```
# 4.js类
# 5.DOM(文档对象)
```js
// 与文档的数据交换
var tag = document.getElementById("#id");
var tag2 = document.createElementById("div");
var s = tag.innerText;
tag.innerText = "ksbdk";
tag.value = "lsnhdkl"
tag.appendChild(another_tag);
// 事件监听
<button onclick = "fun_name()">


```
# 6.BOM(浏览器对象)
```js
setInterval(fun_name,"1000") //每1秒执行一次
```
# 7.jquery
```js
// 选择器
$("#id")
$(".class")
$("tag")
$(".c1 .c2")//层选
$(".c1,.c2")//多选
$("div[value = 'sdf']")//通过属性寻找
$("#id").prev()
$("#id").next()
$("#id").siblings()
$("#id").parent()
$("#id").children()
// 事件监听
$("#id").click(
    function(){
        $(this).parent().remove();//$(this)表示事件发生的标签
        $(this).parent().removeClass();//移除样式
    }
)
