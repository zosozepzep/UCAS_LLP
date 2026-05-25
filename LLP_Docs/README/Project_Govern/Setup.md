# 环境搭建指南
* **VPN 配置**
	 * [Watt Toolkit](https://steampp.net/download)
	 * fast88sj.com
	 * [iKuuuVPN](https://ikuuu.de/)
	 * [Mihomo Party(Clash)](https://mihomoparty.app/#download)
* **Obsdian指南**
	 * [Download - Obsidian](https://obsidian.md/download)  
	 * [Obsidian新手不完全指南](https://forum-zh.obsidian.md/t/topic/1628)
	 * [Obsidian配置教程(仅供参考)](https://jason-effi-lab.notion.site/Obsidian-20698ac9981180229066ff67342e8232)
* **github学生认证申请**
	 * [GitHub Education](https://github.com/education)
	 * 【Github Copilot学生认证教程】 https://www.bilibili.com/video/BV1Abp1z6Eqs/?share_source=copy_web&vd_source=256ad1d02e285d08be28a97a13050b64
	 * **ps:**
		 * watt toolkit加速并不影响最后的定位验证。
		 * 将学生证的封面和个人信息页拍照，让豆包将中文替换为英文，再将两张照片放到[Home - University of Chinese Academy of Sciences](https://english.ucas.ac.cn/)上截图，作为学籍证明提交，可大幅提高成功率。
		 * 最近学生认证暂时关闭。
* **Vibe Coding**
    * **环境搭建**
    	* [Node.js](https://nodejs.org/zh-cn/download)
    	* [cc-switch.](https://github.com/farion1231/cc-switch) 
	* **Claudecode**
    	* [everything-claude-code](https://github.com/affaan-m/everything-claude-code)
    	* [claude-howto](https://github.com/luongnv89/claude-howto)
    	* [claudecode安装教程](https://www.bilibili.com/video/BV19vc5zUEeQ/?share_source=copy_web&vd_source=256ad1d02e285d08be28a97a13050b64)
    	* [Official Claude Code Plugins.](https://github.com/anthropics/claude-plugins-official)
	* **Codex**
    	* Windows端尚未适配成熟，建议安装wsl，在wsl中使用Codex;或者安装以后在Claudecode中安装codex-plugin-cc，实现两个Agent合作工作。
	* **API平台**
    	* [硅基流动 SiliconFlow](https://siliconflow.cn/)
    	* [百炼](https://www.aliyun.com/product/bailian)
    	* [Ollama Cloud](https://docs.ollama.com/api/introduction)
* **Ollama**食用指南
	* **安装** :[Download Ollama on Windows](https://ollama.com/download/windows)
		* ps:默认安装路径为C:\Users\，以下是更改安装路径教程:
		  例如，你的Ollama安装包在D:\Ollama中，打开该文件夹，在资源管理器上方的文件路径中输入cmd并打开，在窗口中输入`OllamaSetup.exe /DIR=D:\Ollama`,即可将Ollama安装在D:\Ollama\中。
		  （dby注：D盘需要管理员权限，可尝试：按Win后搜索cmd，右键点击“以管理员身份运行”，再输入：
			```shell
			D:
			cd D:\Ollama
			```
		  这样就以管理员身份进入了D盘 ）
	* **模型部署**: 
		* 1.打开Ollama，进入Settings，更改Model Location至D:\中的某个文件夹。
		* 2.打开CMD，在窗口中输入`ollama run gemma4:e4b`，等待安装成功。
		* 3.如果电脑配置不足以运行e4b，请输入`ollama run gemma4:e2b`,我们的项目是基于这两个模型开展的。
		* 4.Ollama中可以查看模型本身的配置参数。
    		``` powershell 
    		ollama show <模型名称> --system #查看系统提示词
    		ollama show <模型名称> --modefile #m模型的全部配置参数
    		```
    	 * 5.Ollama上可以下载OCR模型用于解析.pdf文档，例如glm-ocr，deepseek-ocr，配合Agent使用可以节省大量token。
* **Terminal终端以及WSL的使用(Windows)** 
	* 不建议使用CMD，这是上古时期DOS系统的残骸，只能完成部分简单的命令；
	* Powershell的兼容性更高，可以执行大部分类Unix命令。Windows默认使用的是Powershell 5.1。可以下载Powershell 7，功能更加强大。详情见[微软官方指南]https://aka.ms/PSWindows 。建议下载MSI。
	* WSL2是由微软开发、在Windows上运行的Linux内核。
		* Linux比Windows更适合开发，拥有强大而统一的shell和工具链，也可以使用docker --compose起一个容器来隔离环境，不影响系统的安全（尤其是训练模型时）。此外，Linux对Agent也更加友好，不容易出现Windows端著名的**Codex使用Git bash转义错误导致删盘**的情况。
		* /mnt 是Windows和WSL的文件交换区，但是效率比较低，其实不如直接把仓库复制到WSL里面去。使用**VScode的 remote-ssh插件**连接到WSL中进行编辑。
*  **frontend三件套（计科导也要用）**
    * [HTML, CSS, JavaScript] https://zhuanlan.zhihu.com/p/526785618?share_code=8NBaKugDf23l&utm_psn=2027159371033912095
        * 参考网站：https://developer.mozilla.org/
* **Work Flow**