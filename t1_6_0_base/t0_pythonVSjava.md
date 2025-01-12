# python vs java

## 语言类型
- java 是静态类型语言；python 是动态类型语言。

## 编写上

### 变量的使用
语言类型的不同体现在变量的使用上

什么意思？即所谓静态类型就是变量需要 `先声明再使用`。动态类型 `不需要事先声明直接使用`。

举例：
java 中声明变量，先声明变量的类型，再为变量赋值。
```
int var = 0;
```

python 中无需事先声明，拿来就能用
```
var = 0
```

### 区分代码块

java 用 `大括号` 区分同一个块的语句，python 用 `缩进` 区分

### 忘记括号
java 中语句的结束强制使用 ";" 为结尾。python中也可以使用分号，但不建议使用。python 通常使用换行标识语句的结束

### 或与非
java 是 `&& || !`; python 是 `and or not`


## 定义上 

### main方法
java 需要定义main方法，python 可以不定义

### 输出语句
java 大量使用 "+" 拼接字符串的方式。python 中打印变量需要使用 "占位符"。
```
print("this is a %s"% ("dog"))
```

### 组数和列表
java中数组定义数组用大括号 "{}"; python中定义数组使用中括号 "[]"。
java 数组的元素都是相同类型的。python 中组数的元素可以相同，也可以不同。

```
-- java
int[] array = {1, 2, 3}

-- python
array = [1, 2, 3]

array = [1, "a", "test"]
```

### 类

#### 类方法中表示当前实例的变量
java 是 `this.xxx`; python 是 `self.xxx`

#### 继承
java 是 `class A extends B {}`; python 是 `class A(B){}`

### 类型检查
```
-- Java：instanceof
//用法：变量 instanceof 类型
//返回true或false；

boolean isDouble = n instanceof Double;

-- Python：isinstance
//用法：isinstance(变量,类型)
//返回True或False
isDouble = isinstance(n,double) 
```


### 判断变量是否为null
```
-- java
if(a == null) {
    // 语句
}

-- python
if not a:
    // 语句
```

### 条件语句，循环语句

java 使用 `大括号` ，python 使用 `冒号`

for 循环
```
-- java
for (n : arr) {
    // 循环体
}

-- python
for n in arr:
    // 循环体
```

if 条件
```
-- java
if(条件) {
    // 执行语句1
}else if(条件2) {
    // 执行语句2
}else{
    // 执行语句3
}

-- python
if 条件：
    // 执行语句1
elif 条件2:
    // 执行语句2
else
    // 执行语句3
```

### 异常处理
```
-- java
try {
    //可能出错的语句
}
catch(Exception1 e){
    //捕获到1类错误时的后续处理
}

-- python
try:
    //可能出错的语句
except xxxError:
    // 捕获异常是的后续处理
```


### 其他

Java的缩进不是必须的，只是为了格式好看；Python中的缩进则是必须且重要的
