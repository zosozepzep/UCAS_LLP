# Pandas 核心知识清单

## 目标：掌握数据读取 + 结构化处理（为 Prompt 数据集整理、D1/D2 数据清洗打基础）

---

## 一、Pandas 是什么？

- Python 里**最常用的数据处理库**(标准库无需install)

- 专门用来读取、清洗、筛选、转换表格类数据（Excel/CSV/JSON/TXT）

- 是 Prompt 数据集整理、结构化标注、数据清洗的**必备工具**

---

## 二、安装与导入

```python
# 安装
pip install pandas

# 导入（固定写法）
import pandas as pd
```

---

## 三、核心数据结构（必须掌握）

### 1. Series

- 一维数据（一列数据）

- 带索引的列表

### 2. DataFrame（最重要）

- 二维表格（行 + 列）

- 等同于 Excel 表格、CSV 表格

- 数据集处理 99% 都用它

---

## 四、数据读取（数据集第一步：读进来）

### 1. 读取 CSV 文件

```python
df = pd.read_csv("数据集.csv")
```

### 2. 读取 Excel 文件

```python
df = pd.read_excel("数据集.xlsx")
```

### 3. 读取 TXT 文本（按分隔符）

```python
df = pd.read_csv("数据.txt", sep="\t")  # 制表符分隔
```

### 4. 读取 JSON（常见 Prompt 数据集格式）

```python
df = pd.read_json("数据.json")
```

### 5. 快速查看数据

```python
df.head()        # 前5行
df.shape         # 行数、列数
df.columns       # 列名
df.info()        # 字段类型、是否缺失
df.describe()    # 数值统计
```

---

## 五、数据查看与基础操作

### 1. 查看列

```python
df["列名"]
df[["列1", "列2"]]  # 多列
```

### 2. 查看行

```python
df.iloc[0]     # 第1行
df.iloc[0:5]   # 前5行
```

### 3. 查看某个单元格

```python
df.loc[行索引, "列名"]
```

---

## 六、结构化数据处理（数据集整理核心）

### 1. 筛选行（过滤数据）

```python
# 条件筛选
df[df["列名"] > 10]
df[df["列名"] == "需要的值"]
```

### 2. 新增/修改列

```python
df["新列名"] = df["A列"] + df["B列"]
df["提示词"] = "请处理：" + df["原始文本"]
```

### 3. 删除列

```python
df = df.drop(columns=["不需要的列"])
```

### 4. 重命名列（数据集标准化必备）

```python
df = df.rename(columns={"旧名": "新名"})
```

### 5. 去重

```python
df = df.drop_duplicates()          # 全行重复
df = df.drop_duplicates(["文本"])   # 按某列去重
```

### 6. 处理缺失值

```python
df = df.dropna()          # 删除缺失行
df = df.fillna("无")      # 填充缺失值
```

### 7. 排序

```python
df = df.sort_values(by="列名", ascending=False)
```

---

## 七、字符串文本处理（Prompt 数据集高频使用）

```python
df["文本列"] = df["文本列"].str.strip()        # 去空格
df["文本列"] = df["文本列"].str.replace("a","b")# 替换
df["文本列"] = df["文本列"].str.lower()        # 转小写
df["包含关键词"] = df["文本列"].str.contains("订单")
```

---

## 八、数据分组统计（简单数据分析）

```python
df.groupby("类别列").size()
df.groupby("类别列")["数值列"].mean()
```

---

## 九、数据保存（处理完导出）

```python
df.to_csv("清洗后数据集.csv", index=False, encoding="utf-8")
df.to_excel("清洗后数据集.xlsx", index=False)
df.to_json("清洗后数据集.json", orient="records", force_ascii=False)
```

---

## 十、Pandas 做 Prompt 数据集标准流程

1. 读取原始数据（csv/json/excel）

2. 查看数据结构（head/info/columns）

3. 筛选有效数据（过滤、去重、删缺失）

4. 统一列名（prompt/response/input/output 等）

5. 生成标准格式提示词（拼接文本）

6. 导出成模型需要的格式（CSV/JSON）

---

## 十一、常用速查清单

```python
import pandas as pd

# 读取
df = pd.read_csv("data.csv")

# 查看
df.head()
df.info()

# 清洗
df = df.dropna()
df = df.drop_duplicates()

# 构造 Prompt
df["prompt"] = "用户问题：" + df["question"]

# 导出
df.to_csv("prompt_data.csv", index=False)
```
> （注：文档部分内容可能由 AI 生成）