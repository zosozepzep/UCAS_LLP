# 简介
Docker 是一种领先的容器化技术，它能够将应用程序及其依赖环境打包在一起，实现“一次构建，到处运行”。如果大家能够掌握，从长远看，对我们项目的工程化帮助很大。

本指南旨在为开发者提供一套全方位的 Docker 实战参考。内容涵盖了从入门视频教程、官方文档资源，到日常开发中最常用的镜像管理、容器生命周期、多容器编排（Compose）以及系统维护命令。特别针对**深度学习用户**（如 PyTorch 环境配置、GPU 调用）和 **Windows 平台用户**（如 D 盘安装、PowerShell 操作）提供了针对性的指导和避坑指南。欢迎其他组成员补充与项目相关的Docker学习内容

---

# Docker教程
* [Docker安装+镜像加速]( https://www.bilibili.com/video/BV1xHA3euEcn/?share_source=copy_web&vd_source=256ad1d02e285d08be28a97a13050b64)
* 注意：以下操作建议全程开启代理
* 安装命令：
	* 在docker安装包所在的文件夹中，打开powershell
	* 输入`"Docker Desktop Installer.exe"  install --installation-dir="D:\Docker`
	* 等待安装成功
* 安装wsl：
	* 前置条件按照视频操作
	* `wsl --update`
	* `wsl --set-default-version 2`
	* `wsl --install -d Ubuntu-22.04`
	* 安装完成后，输入并确定Ubuntu的账号密码
	* 注意：此时wsl默认启动项为docker，要将其修改为ubuntu：
		* `exit`
		* `wsl -l -v` #  确认Ubuntu版本
		* `wsl --setdefault Ubuntu-22.04`
* 操作完毕后，按照视频教程，配置代理（如果没有代理，则配置镜像源） ，修改镜像安装位置
* ps:安装Ubuntu时，建议大家用22.04或20.04的LTS，最新的24.04可能存在不兼容问题

---

# Docker常用资源
* * [Docker Docs](https://docs.docker.com/)
* [Docker Hub](https://hub.docker.com/)
* [Previous PyTorch Versions](https://pytorch.org/get-started/previous-versions/)
* [50系显卡一定要用preview！！！](https://pytorch.org/get-started/locally/)

---

# Docker 常用命令(适用于PowerShell&CMD)
## 1. 基础信息查询
用于检查 Docker 是否正常运行以及查看版本。
*   `docker version`：查看 Docker 客户端和服务端的版本信息。
*   `docker info`：查看 Docker 的系统级信息（镜像数、容器数、存储驱动、内存限制等）。
*   `docker --help`：查看所有命令的帮助文档。

---

## 2. 镜像管理 (Images)
镜像就像是安装软件的“安装包”。
*   **拉取镜像**：`docker pull <image_name>` (例如: `docker pull nginx`)
*   **查看本地镜像**：`docker images`
*   **删除镜像**：`docker rmi <image_id_or_name>` (需先停止使用该镜像的容器)
*   **构建镜像**：`docker build -t <name>:<tag> .` (在当前目录下根据 Dockerfile 构建)
	* `docker build --no-cache -t <容器名> .` (无缓存构建镜像，适合构建报错fix后使用)
*   **清理无用镜像**：`docker image prune` (删除悬空镜像)

---

## 3. 容器生命周期管理 (Containers)
容器是镜像运行时的实例。
*   **运行容器**：`docker run [OPTIONS] <image>`
    *   `-d`：后台运行
    *   `-p 8080:80`：端口映射（主机8080:容器80）
    *   `--name my-app`：给容器起个名字
    *   `-v /host:/container`：挂载数据卷
    *   *示例：* `docker run -d -p 8080:80 --name web-server nginx`
*   **查看运行中的容器**：`docker ps`
*   **查看所有容器（包括已停止的）**：`docker ps -a`
*   **停止容器**：`docker stop <container_id_or_name>`
*   **启动已停止的容器**：`docker start <container_id_or_name>`
	* **启动并调用gpu**:`docker run -it --gpus all <容器名>`
*   **进入容器:**`docker exec -it <容器ID或名字> bash`
*   **重启容器**：`docker restart <container_id_or_name>`
*   **删除容器**：`docker rm <container_id_or_name>` (加 `-f` 可强制删除运行中的容器)

---

## 4. 容器操作与调试
当你需要进入容器内部或者查看报错信息时使用。
*   **查看日志**：`docker logs -f <container_id_or_name>` (`-f` 表示持续输出)
*   **进入容器内部执行命令**：`docker exec -it <container_id_or_name> /bin/bash` (或者 `sh`)
*   **查看容器资源占用**：`docker stats` (查看 CPU、内存、网络 IO)
*   **查看容器详细配置**：`docker inspect <container_id_or_name>`

---

## 5. 数据卷与网络 (Volumes & Networks)
*   **查看所有数据卷**：`docker volume ls`
*   **清理无用数据卷**：`docker volume prune`
*   **查看所有网络**：`docker network ls`

---

## 6. Docker Compose (多容器编排)
Docker Desktop 自带 Compose，用于管理多个关联的容器（如：Java+MySQL+Redis）。
*   **启动所有服务**：`docker compose up -d` (在包含 `docker-compose.yml` 的目录下运行)
*   **停止并移除所有服务**：`docker compose down`
*   **查看服务状态**：`docker compose ps`
*   **查看服务日志**：`docker compose logs -f`

---

## 7. 系统清理
Docker Desktop 在 Windows/Mac 上非常占用磁盘空间，定期清理很重要。
*   **一键大扫除**：`docker system prune`
    *   这会删除：所有已停止的容器、未被使用的网络、悬空的镜像。
*   **深度清理**：`docker system prune -a --volumes`
    *   这会删除：所有未被容器使用的镜像和数据卷（**慎用，会删除未运行项目的镜像**）。

---
## 8.常用技巧 (Cheat Sheet)
1.  **批量停止所有容器**：`docker stop $(docker ps -aq)`
2.  **批量删除所有已停止的容器**：`docker container prune`
3.  **快速查看容器 IP**：`docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_id>`