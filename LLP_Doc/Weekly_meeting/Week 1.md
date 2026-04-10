## 1. 基础设施与工具链协同 (DevOps & Environment)

为了保证团队开发效率，全员需完成以下环境的深度配置：
- **网络环境**：确保具备稳定的海外网络访问能力，用于访问 Hugging Face 模型库、GitHub 及学术资源。
    
- **身份认证**：统一注册并关联 Gmail，用于 Hugging Face 账号登录及协作文档权限管理。
    
- **版本控制 (Git)**：
    
    - 全员完成 `git clone`、`add`、`commit`、`push` 流程测试。
        
    - **规范**：每次提交代码需附带简短的 Commit Message（如 `feat: add data cleaning script`）。
	    - feat: 新功能（feature）
			用于提交新功能。
			例如：feat: 增加用户注册功能
		* fix: 修复 bug
			用于提交 bug 修复。
			例如：fix: 修复登录页面崩溃的问题
			docs: 文档变更
			用于提交仅文档相关的修改。
			例如：docs: 更新README文件
		* style: 代码风格变动（不影响代码逻辑）
			用于提交仅格式化、标点符号、空白等不影响代码运行的变更。
			例如：style: 删除多余的空行
		* refactor: 代码重构（既不是新增功能也不是修复bug的代码更改）
			用于提交代码重构。
			例如：refactor: 重构用户验证逻辑
		* perf: 性能优化
			用于提交提升性能的代码修改。
			例如：perf: 优化图片加载速度
		* test: 添加或修改测试
			用于提交测试相关的内容。
			例如：test: 增加用户模块的单元测试
		* chore: 杂项（构建过程或辅助工具的变动）
			用于提交构建过程、辅助工具等相关的内容修改。
			例如：chore: 更新依赖库
		* build: 构建系统或外部依赖项的变更
			用于提交影响构建系统的更改。
			例如：build: 升级webpack到版本5
		* ci: 持续集成配置的变更
			用于提交CI配置文件和脚本的修改。
			例如：ci: 修改GitHub Actions配置文件
		* revert: 回滚
			用于提交回滚之前的提交。
			例如：revert: 回滚feat: 增加用户注册功能
- **AI 辅助开发建议**：提倡使用 LLM 工具辅助编写 Python 脚本，但禁止直接复制不理解的复杂逻辑，须确保能手动复现代码核心。
---

## 2. 团队架构与第一阶段职责 (Team Structure)

项目采用 **“垂直分工 + 水平协作”** 模式，确保各环节产出物（Artifacts）可对接：

| **角色**          | **成员** | **第一阶段核心产出 (W1-W2)**   | **KPI**               |
| --------------- | ------ | ---------------------- | --------------------- |
| **模型组 (Model)** | M1, M2 | `model_inference.py`   | 成功加载本地模型并实现单句推理       |
| **数据组 (Data)**  | D1, D2 | `cleaned_dataset.json` | 完成 500+ 条原始数据的清洗与标注   |
| **评估组 (Eval)**  | E1, E2 | `metric_results.csv`   | 实现 BLEU/PPL 的自动化批处理计算 |
| **前端组 (UI)**    | F1, F2 | `interactive_demo.py`  | 完成具备参数调节滑块的交互界面       |
| **后端组 (API)**   | B1     | `full_api.py`          | 实现前端与模型推理逻辑的低延迟联调     |
| **文档测试 (QA)**   | T1     | `week_summary.md`      | 产出项目技术白皮书及周进展简报       |

---

## 3. 开发者文档体系 (Documentation Standards)

为了保证项目的可持续性，所有成员需在 GitHub Wiki 或指定 Markdown 文件中维护以下内容：
- **Change Log (更新日志)**：
    
    - 记录解决的技术难点（如：如何解决 Transformer 版本冲突）。
        
    - 个人学习曲线记录（从零基础到掌握特定库的心得）。
        
	- **Resource Center(资源池)**：
    
    - 收录各组调研的优质开源项目、Hugging Face Course 教程链接、Prompt Engineering 技巧等。
        
- **Metric Reports (效果评估)**：
    
    - 记录每一轮微调（Fine-tuning）后的 PPL（困惑度）变化曲线。
        
    - 对比不同硬件环境下的推理速度。
---

## 4. 本周（第1周）关键里程碑 (Milestones)

### 第一阶段（基础夯实）执行表
- **Day 1-2：语法破冰**
    
    - **全员**：完成 Python 基础环境测试。
        
    - **专项**：各小组根据《每组学习目标表》安装对应的库（如 `transformers`、`streamlit`、`pandas`）。
        
- **Day 3-5：原型探索**
    
    - 模型组尝试跑通 `distilgpt2` 或 `TinyLLaMA` 的本地 Demo。
        
    - 前端组完成基于 Streamlit 的 "Hello World" 页面搭建。
        
- **Day 6-7：同步会议**
    
    - **内容**：跨小组沟通接口协议（例如后端需要确认前端发送的 JSON 格式）。
        
    - **产出**：提交第一周总结文档 `week1_summary.md`。
---

## 5. Management Tips

- **先跑通，再优化**：遵循“最小可行性产品（MVP）”原则，先保证模型能输出文字，再去研究如何提升精度。
    
- **对于BUG**：建议 T1（文档组）在第一周建立一个“Bug 常见问题汇总（FAQ）”，减少团队重复报错的解决时间。
    
- **时间控制**：每日投入控制在 **2-3 小时**，保持“小步快跑”的节奏，避免在某一复杂算法上过度停留导致进度断层。