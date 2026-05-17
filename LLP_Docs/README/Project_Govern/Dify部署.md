* 全程开启代理
* 进入powershell
*   `wsl`  # 一定要将默认启动项改为ubuntu
	`cd ~`
	`git clone https://github.com/langgenius/dify.git`
	`cd dify/docker`
	`cp .env.example .env`
	`docker compose up -d 
* 一键启动配置：`start-dify`
	* `echo "alias start-dify='cd ~/dify/docker && docker compose up -d'" >> ~/.bashrc
	* `source ~/.bashrc`
* 一键停止配置：`stop-dify`
	* `echo "alias stop-dify='cd ~/dify/docker && docker compose down'" >> ~/.bashrc`
	* `source ~/.bashrc`