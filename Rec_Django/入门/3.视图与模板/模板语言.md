# !!!!不要忽视空格，也不要增加多余的空格
## 1. variables
`{{ var_name }}`
## 2. filter
`{{ var_name|filter_1|filter_2:filter_arg }}`
## 3. tag
```django
{% if var_name1 %}
    some html
{% elif var_name2 %}
    some html
{% else %}
    some html
{% endif %}
```
## 4. regular tag
```django
{# for #}
{% for a in b %}
    some html
{% endfor %}

{# 模板继承 #}
{% extends template_url %}
{# block #}
{% block block_name %}
{% endblock %}

{# 模板语言变量自动转义开启与关闭 <>'"& #}
{% autoescape off %}
    Hello {{ name }}
{% endautoescape %}

{# 是否进行模板渲染 #}
{% verbatim %}
    something
{% endverbatim %}

{# tag 输出结果存为其他变量 #}
<tr>
    <td class="{% cycle 'row1' 'row2' as rowcolors %}">...</td>
    <td class="{{ rowcolors }}">...</td>
</tr>
<tr>
    <td class="{% cycle rowcolors %}">...</td>
    <td class="{{ rowcolors }}">...</td>
</tr>
```
## 5. custom filter/tag
1. 在 app/templatetags/ 建立filter/tag的 py 文件
2. 在py文件中编写相关函数
3. 使用 django.template.Library() 将tag_name与function进行注册
### 5.1 filter
```python
from django import template
register = template.Library()

# 函数式注册
def cut(value, arg): # 接受至多2个，至少1个参数
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')

register.filter('cut', cut)

# 装饰器注册
# filter(name = None,filter_func = None, **flag)
@register.filter
def cut(value, arg):
    return value.replace(arg, '') 

@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg, '')
```
### 5.2 tag
```python
import datetime
from django import template

register = template.Library()

@register.simple_tag
def current_time(format_string): # 接受任意数量的参数
    return datetime.datetime.now().strftime(format_string)
```
```django
{# 自定义Tag的使用,注意如何传参 #}
{% load py文件 %}
{% current_time "yy-mm-dd" %}
```
```python
# 接受context作为arg的Tag
@register.simple_tag(takes_context=True)
def current_time(context, format_string):#第一个参数必须为context
    timezone = context['timezone']
    return your_get_current_time_method(timezone, format_string)
```
```python
# 按照指定template输出的的Tag

"""
Tag使用
{% show_results poll %}
Tag实际输出
<ul>
  <li>First choice</li>
  <li>Second choice</li>
  <li>Third choice</li>
</ul>

指定输出模板 results.html
<ul>
{% for choice in choices %}
    <li> {{ choice }} </li>
{% endfor %}
</ul>
@register.inclusion_tag('results.html')
def show_results(poll):
    ...
"""
@register.inclusion_tag('results.html') #注册时指定模板
def show_results(poll): #函数只需要返回对应数据
    choices = poll.choice_set.all()
    return {'choices': choices}
```

