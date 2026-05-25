FROM nvidia/cuda:13.0.3-cudnn-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /workspace

# 使用HTTPS的官方源(避免502，需要美国节点的魔法) + 重试
RUN sed -i 's|http://archive.ubuntu.com|https://archive.ubuntu.com|g' /etc/apt/sources.list && \
    sed -i 's|http://security.ubuntu.com|https://security.ubuntu.com|g' /etc/apt/sources.list && \
    apt-get update -o Acquire::Retries=5 && \
    apt-get install -y \
        python3 \
        python3-pip \
        git \
    && rm -rf /var/lib/apt/lists/*

# 升级 pip（避免装包失败）
RUN python3 -m pip install --upgrade pip

# 安装 PyTorch 和相关库
RUN pip install --no-cache-dir \
    --pre torch torchvision --index-url https://download.pytorch.org/whl/nightly/cu130 && \
    pip install --no-cache-dir \
    transformers datasets peft accelerate