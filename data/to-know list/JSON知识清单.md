# JSON 核心知识清单

## 目标：掌握 JSON 数据的解析、生成、验证等操作。

---

## 一、JSON 是什么？

**JSON（JavaScript Object Notation）** 是一种**轻量级、纯文本**的数据交换格式，**独立于编程语言**，几乎所有主流语言（Python、Java、JS、Go 等）都支持解析和生成 JSON。
它的核心作用：**在不同程序/系统之间传递、存储结构化数据**，比 XML 更简洁、易读、体积更小。

---

## 二、JSON 文件的基本特征

1. 后缀名为 `.json`（例如：`config.json`、`data.json`）
2. 纯文本格式，可用记事本、VS Code 直接打开编辑
3. 数据结构清晰，人类和机器都能轻松识别
4. 无注释（标准 JSON 不支持 `//` 或 `/* */` 注释）

---

## 三、JSON 核心语法规则（必记）

### 1. 数据格式

JSON 数据以 **键值对（key: value）** 为基础，键必须用**双引号**包裹，值支持多种数据类型。

### 2. 支持的数据类型

| 类型  | 说明             | 示例                       |
| --- | -------------- | ------------------------ |
| 字符串 | 必须用双引号       | `"name": "小明"`           |
| 数字  | 整数/浮点数，无引号       | `"age": 20, "score": 95.5` |
| 布尔值 | true / false（小写） | `"isStudent": true`        |
| 空值  | null（小写）         | `"address": null`          |
| 对象  | 用 `{}` 包裹，嵌套键值对  | `{"city": "北京"}`           |
| 数组  | 用 `[]` 包裹，多个值    | `"hobby": ["唱","跳","RAP","篮球"]`    |

### 3. 严格语法禁忌

1. **键名必须用双引号**（单引号/无引号都不合法）
2. **字符串必须用双引号**（禁止单引号）
3. 最后一个键值对/数组元素**不能加逗号**
4. 不支持注释、函数、undefined
5. 区分大小写（true ≠ True）

---

## 四、标准 JSON 代码示例

### 1. 简单对象格式

```json
{
 "name": "DwuanBoyoung",
 "age": 19,
 "isGraduated": false,
 "QQ": 78837968,
 "hobbies": ["coding", "travelling", "mapping"],
 "education": {
     "school": "UCAS(双非)",
     "major": "CS"
 }
}
```

### 2. 数组格式（多个对象）

```json
[
 {
 "id": 1,
 "product": "购机补助",
 "price": 8000
 },
 {
 "id": 2,
 "product": "投湖窝囊费",
 "price": 500
 }
]
```

---

## 五、JSON 与 JavaScript 对象的区别

很多人会混淆两者，核心差异如下：
| 对比项 | JSON | JavaScript 对象 |
|--------|------|----------------|
| 键名 | 必须双引号 | 可省略引号、支持单引号 |
| 字符串 | 必须双引号 | 支持单引号/双引号 |
| 注释 | 不支持 | 支持 |
| 函数/undefined | 不支持 | 支持 |
| 用途 | 数据传输、存储 | 程序内部使用 |

---

## 六、JSON 的常见使用场景

1. **配置文件**：项目配置（如 `package.json`、`settings.json`）
2. **接口数据传输**：前端 ↔ 后端 API 交互最常用格式
3. **数据存储**：轻量级数据持久化（代替数据库小文件存储）
4. **跨语言数据交换**：Python 写的数据，Java/JS 可直接解析

---

## 七、主流编程语言操作 JSON

### 1. Python 读写 JSON

```python
import json
# 字典转 JSON 字符串
data = {"name": "李四", "age": 25}
json_str = json.dumps(data, ensure_ascii=False)
# JSON 字符串转字典
parsed_data = json.loads(json_str)
# 写入 JSON 文件
with open("data.json", "w", encoding="utf-8") as f:
 json.dump(data, f, ensure_ascii=False, indent=2)
```

### 2. JavaScript 操作 JSON

```javascript
// 对象转 JSON 字符串
const data = { name: "王五", age: 30 };
const jsonStr = JSON.stringify(data);
// JSON 字符串转对象
const parsedData = JSON.parse(jsonStr);
```

---

## 八、JSON 校验工具

编写 JSON 时容易语法出错，推荐在线校验工具：

1. [JSONlint](https://jsonlint.com/)
2. [JSON Formatter](https://jsonformatter.curiousconcept.com/)
   粘贴代码即可一键检查语法错误、格式化排版。

---

## 九、JSON 优缺点总结

### PROS

- 轻量简洁，体积小，传输快
- 跨语言、跨平台通用
- 结构清晰，易读易写
- 解析速度快，生态成熟

### CONS

- 不支持注释
- 不支持复杂数据类型（日期、二进制需转字符串）
- 无法存储函数逻辑

---

### 总结

1. JSON 是**通用数据交换格式**，纯文本、跨语言、轻量级
2. 核心语法：**双引号键名、6种数据类型、无注释、严格格式**
3. 主要用于：配置文件、接口传输、轻量数据存储
4. 所有主流编程语言都内置 JSON 解析库，上手极快
