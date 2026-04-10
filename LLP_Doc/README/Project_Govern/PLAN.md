[[小模型训练小组规划（小型科研实验平台）]]
[[README/Project_Govern/README]]
#  **说明**

- 团队角色：
    - 模型组 2人（M1, M2）
    - 数据组 2人（D1, D2）
    - 评估组 2人（E1, E2）
    - 前端组 2人（F1, F2）
    - 后端组 2人（B1）
    - 文档测试组 1人（T1）
- 每人每天任务量控制在**2-3小时学习/实验**，零基础可完成。
- 每周目标：每周有一个可展示的小产出（demo或文档）。
# 第1周：环境搭建 & Python基础

| 星期   | 人员    | 学习/任务                             | 教程/资源               | 第一版代码/产出      | 阶段文件                      |
| ---- | ----- | --------------------------------- | ------------------- | ------------- | ------------------------- |
| Day1 | 全员    | 安装 Python、VSCode、Git              | 官方Python教程、VSCode官网 | Python环境可运行   | 无                         |
| Day2 | M1,M2 | Python基础语法（变量、list、dict、function） | w3schools Python    | 输出简单脚本（打印、计算） | `python_basics.py`        |
|      | D1,D2 | Python基础 + Pandas入门               | Pandas官方教程          | DataFrame小练习  | `pandas_demo.ipynb`       |
|      | E1,E2 | Python基础 + matplotlib入门           | matplotlib教程        | 绘制简单图表        | `plot_demo.py`            |
|      | F1,F2 | Python基础 + Streamlit入门            | Streamlit官方教程       | 第一个hello page | `streamlit_hello.py`      |
|      | B1    | Python基础 + Flask入门                | Flask官方教程           | 第一个hello API  | `flask_hello.py`          |
|      | T1    | Markdown基础 + 文档模板                 | Markdown教程          | 项目文档模板        | `project_doc_template.md` |
| Day3 | 全员    | Git入门，建立团队仓库                      | GitHub入门            | 克隆仓库、提交测试文件   | 仓库初始化                     |
| Day4 | M1,M2 | Transformers基础概念                  | Hugging Face Course | 阅读示例代码        | `transformers_demo.py`    |
| Day5 | D1,D2 | 文本清洗基础                            | Python regex教程      | 清理demo文本      | `text_cleaning.ipynb`     |
| Day6 | E1,E2 | BLEU概念学习                          | NLTK BLEU教程         | 手动计算1-2句      | `bleu_demo.py`            |
| Day7 | T1+全员 | 周总结会议                             | 无                   | 汇报各自进展        | `week1_summary.md`        |
# 第2周：小模型推理 & 数据集准备

| 星期   | 人员    | 学习/任务                         | 教程/资源                     | 第一版代码/产出        | 阶段文件                      |
| ---- | ----- | ----------------------------- | ------------------------- | --------------- | ------------------------- |
| Day1 | M1,M2 | 下载小语言模型（distilgpt2/TinyLLaMA） | Hugging Face模型库           | 测试生成1句话         | `model_inference.py`      |
|      | D1,D2 | 收集原始文本数据                      | WikiText, OpenWebText     | 保存json文本        | `raw_dataset.json`        |
|      | E1,E2 | BLEU计算练习                      | NLTK教程                    | 计算样例BLEU        | `bleu_test.py`            |
|      | F1,F2 | Streamlit输入输出页面设计             | Streamlit文档               | 页面布局完成          | `input_output_demo.py`    |
|      | B1    | Flask API初步实现                 | Flask教程                   | GET/POST测试      | `api_demo.py`             |
|      | T1    | 文档写作周总结                       | Markdown                  | 更新周1总结          | `week2_summary.md`        |
| Day2 | M1,M2 | 模型推理测试不同输入                    | Hugging Face pipeline     | 输出多条生成结果        | `model_inference_test.py` |
| Day3 | D1,D2 | 数据清洗（去特殊符号、空行、分词）             | Pandas+Regex              | 输出清洗后文本         | `cleaned_dataset.json`    |
| Day4 | E1,E2 | PPL概念 + 小文本实验                 | Hugging Face perplexity教程 | 输出PPL值          | `ppl_demo.py`             |
| Day5 | F1,F2 | 页面交互完善（按钮/输出区）                | Streamlit官方例子             | 可运行demo         | `interactive_demo.py`     |
| Day6 | B1    | API连接前端测试                     | Flask+Streamlit           | 页面可调用API返回结果    | `api_frontend_test.py`    |
| Day7 | T1+全员 | 周总结会议                         | 无                         | 汇报模型生成 & 数据清洗结果 | `week2_summary.md`        |
# 第3周：模型微调初步 & 数据标注

| 星期   | 人员    | 学习/任务        | 教程/资源               | 第一版代码/产出              | 阶段文件                 |
| ---- | ----- | ------------ | ------------------- | --------------------- | -------------------- |
| Day1 | M1,M2 | 学LoRA微调概念    | PEFT/Hugging Face教程 | 准备微调配置                | `lora_config.py`     |
| Day2 | D1,D2 | 数据标注/构建训练集   | 自己整理规则              | 输出训练json              | `train_dataset.json` |
| Day3 | E1,E2 | BLEU/PPL实验   | 自己构造测试集             | 输出对比结果                | `metric_results.csv` |
| Day4 | F1,F2 | 前端页面增加微调参数输入 | Streamlit           | 可选择temperature/length | `parameter_demo.py`  |
| Day5 | B1    | API增加微调调用接口  | Flask               | 测试接口调用                | `api_lora_test.py`   |
| Day6 | T1    | 文档更新 & 周报    | Markdown            | 文档记录微调配置              | `week3_summary.md`   |
| Day7 | 全员    | 周会议          | 无                   | 汇报微调实验可行性             | `week3_summary.md`   |
# 第4周：平台雏形整合

| 星期   | 人员     | 学习/任务           | 教程/资源        | 第一版代码/产出 | 阶段文件                        |
| ---- | ------ | --------------- | ------------ | -------- | --------------------------- |
| Day1 | 模型+数据组 | 微调小模型一轮         | PEFT/LoRA教程  | 输出生成结果   | `lora_finetune_output.json` |
| Day2 | 评估组    | 对生成结果计算BLEU/PPL | 自定义脚本        | 输出表格     | `metric_results_week4.csv`  |
| Day3 | 前端组    | 页面整合输入输出 + 参数选择 | Streamlit    | 页面可完整运行  | `full_demo_page.py`         |
| Day4 | 后端组    | API接口完善 + 前端联调  | Flask        | 页面可调用模型  | `full_api.py`               |
| Day5 | 文档组    | 写整合文档           | Markdown/PPT | 更新周报     | `week4_summary.md`          |
| Day6 | 全员     | 团队内部测试          | 无            | 测试功能完整性  | `platform_test_results.md`  |
| Day7 | 全员     | 周总结 & demo演示    | 无            | 第一个可展示版本 | `week4_demo.zip`            |
# 第5-8周任务概览（每日可按上4周类似拆分）

| 周次  | 核心任务             | 目标产出                 |
| --- | ---------------- | -------------------- |
| 第5周 | 扩展数据 & 参数实验      | 微调多组模型，生成不同参数结果      |
| 第6周 | BLEU/PPL对比 & 可视化 | 图表展示不同参数、prompt对比    |
| 第7周 | 前后端优化 & 多轮交互     | 完整交互页面，参数可调，结果可保存    |
| 第8周 | 平台演示 & PPT制作     | 最终可展示版本，包含实验结果、图表和文档 |
## 每周每日任务继续拆分成：

- 模型组：运行微调、生成输出
- 数据组：扩充训练集/测试集
- 评估组：BLEU/PPL实验、生成图表
- 前端组：页面迭代、UI优化
- 后端组：接口维护、联调
- 文档组：文档更新、PPT制作
# 阶段性必须完成的文件

| 阶段      | 文件列表                                                                                                                                |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Week1   | `python_basics.py`, `pandas_demo.ipynb`, `plot_demo.py`, `streamlit_hello.py`, `flask_hello.py`, `project_doc_template.md`          |
| Week2   | `raw_dataset.json`, `cleaned_dataset.json`, `model_inference.py`, `interactive_demo.py`, `api_frontend_test.py`, `week2_summary.md` |
| Week3   | `lora_config.py`, `train_dataset.json`, `metric_results.csv`, `parameter_demo.py`, `api_lora_test.py`, `week3_summary.md`           |
| Week4   | `lora_finetune_output.json`, `metric_results_week4.csv`, `full_demo_page.py`, `full_api.py`, `week4_summary.md`, `week4_demo.zip`   |
| Week5-8 | 各组实验输出文件 + 可视化图表 + 最终PPT/文档                                                                                                         |
